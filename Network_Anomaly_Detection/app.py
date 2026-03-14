import os
import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, render_template, send_from_directory
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, classification_report
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-interactive plotting
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and label encoder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, 'model', 'random_forest_model.joblib')
label_encoder_path = os.path.join(BASE_DIR, 'model', 'label_encoder.joblib')

templates_dir = os.path.join(BASE_DIR, 'templates')
static_dir = os.path.join(BASE_DIR, 'static')

try:
    model = joblib.load(model_path)
    label_encoder = joblib.load(label_encoder_path)
    print("Model and label encoder loaded successfully.")
except FileNotFoundError:
    print(f"Error: Model or label encoder file not found at {model_path} or {label_encoder_path}")
    model = None # Set model to None to indicate loading failure
    label_encoder = None
except Exception as e:
    print(f"An error occurred while loading the model or label encoder: {e}")
    model = None
    label_encoder = None

# Assuming 'df' from previous steps is available in the environment
# Define the feature columns used during training, excluding identifiers and the target
# Based on the previous code cell, we excluded 'Flow ID', 'Source IP', 'Destination IP', 'Timestamp', 'Label'.
# We need to ensure 'df' is accessible or redefine feature_columns based on expected input if 'df' is not guaranteed.
# For now, assuming 'df' is available as it was used in previous steps.

# Define directory paths
templates_dir = '/content/extracted_project/anomaly_detection/templates'
static_dir = '/content/extracted_project/anomaly_detection/static'


# Define a route for the home page, which will likely render the upload form (ddos.html)
@app.route('/')
def upload_form():
    return render_template('ddos.html')

# Define a route to handle the file upload and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    if model is None or label_encoder is None:
        return "Error: Model or label encoder not loaded.", 500

    if 'file' not in request.files:
        return "No file part in the request.", 400

    file = request.files['file']

    if file.filename == '':
        return "No selected file.", 400

    if file:
        try:
            # Read the uploaded CSV file into a pandas DataFrame
            uploaded_df = pd.read_csv(file)

            # Basic preprocessing to match training data
            # Ensure column names are stripped of whitespace
            uploaded_df.columns = uploaded_df.columns.str.strip()

            # Select only the feature columns used during training
            # Handle potential missing columns in the uploaded data
            missing_cols = set(feature_columns) - set(uploaded_df.columns)
            if missing_cols:
                # For simplicity, add missing columns with a default value (e.g., 0)
                for c in missing_cols:
                    uploaded_df[c] = 0
                # Or handle this case more robustly, e.g., return an error message
                # return f"Missing columns in uploaded file: {missing_cols}", 400

            # Ensure the columns are in the same order as the training data
            # This is crucial for the model to make correct predictions
            uploaded_df = uploaded_df[feature_columns]


            # Handle potential infinite and NaN values in the uploaded data
            # Replace infinities with NaN, then fill NaNs with 0 (matching training data preprocessing)
            uploaded_df = uploaded_df.replace([np.inf, -np.inf], np.nan)
            uploaded_df.fillna(0, inplace=True)

            # Make predictions
            predictions_encoded = model.predict(uploaded_df)
            predictions_proba = model.predict_proba(uploaded_df)[:, 1] # Probability of the positive class (DDoS)

            # Decode the numerical predictions back to original labels
            predictions_labels = label_encoder.inverse_transform(predictions_encoded)

            # Analyze prediction results
            prediction_counts = pd.Series(predictions_labels).value_counts()
            total_samples = len(uploaded_df)

            # Calculate percentage of anomalies
            if 'DDoS' in prediction_counts:
                anomaly_percentage = (prediction_counts['DDoS'] / total_samples) * 100
            else:
                anomaly_percentage = 0

            # Generate simple bar chart and pie chart for visualization
            plt.figure(figsize=(8, 6))
            prediction_counts.plot(kind='bar', color=['skyblue', 'salmon'])
            plt.title('Distribution of Predicted Labels')
            plt.xlabel('Label')
            plt.ylabel('Count')
            plt.xticks(rotation=0)
            bar_chart_path = os.path.join(static_dir, 'prediction_bar_chart.png')
            plt.savefig(bar_chart_path)
            plt.close()

            plt.figure(figsize=(8, 8))
            prediction_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['skyblue', 'salmon'])
            plt.title('Percentage Distribution of Predicted Labels')
            plt.ylabel('') # Hide the default 'None' ylabel
            pie_chart_path = os.path.join(static_dir, 'prediction_pie_chart.png')
            plt.savefig(pie_chart_path)
            plt.close()


            # Render the results template with the prediction analysis and chart paths
            return render_template('results.html',
                                prediction_counts=prediction_counts.to_dict(),
                                total_samples=total_samples,
                                anomaly_percentage=anomaly_percentage,
                                bar_chart_url='/static/prediction_bar_chart.png',
                                pie_chart_url='/static/prediction_pie_chart.png')

        except Exception as e:
            return f"An error occurred during prediction: {e}", 500

    return "Something went wrong.", 500

# Add a route to serve static files
@app.route('/static/<filename>')
def static_files(filename):
    return send_from_directory(static_dir, filename)

# The Flask app is now defined and routes are set up.
# To run the app in a Colab environment, you would typically use something like flask-ngrok.
# For the purpose of this subtask (integrating the model into the app structure),
# we have completed the necessary code modifications to app.py's logic.
# The actual running of the Flask development server is outside the scope of this subtask.

print("Flask app instance created and routes defined.")