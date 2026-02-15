
Network Anomaly Detection using Machine Learning
📌 Project Overview

This project focuses on detecting DDoS attacks using the CICIDS 2017 network intrusion dataset. The model classifies network traffic as either normal (BENIGN) or malicious (DDoS).

📊 Dataset Used

CICIDS 2017 Dataset
File: Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv

⚠ Dataset not included due to large size.
Download from:
https://www.unb.ca/cic/datasets/ids-2017.html

⚙ Steps Performed

Data Loading using Pandas

Data Cleaning (Removed NaN & Infinite values)

Feature Selection (Removed IP & Timestamp columns)

Target Encoding (BENIGN → 0, DDoS → 1)

Train-Test Split (80-20)

Model Training using Random Forest

Performance Evaluation using Accuracy & Confusion Matrix

🤖 Model Used

Random Forest Classifier

Why Random Forest?

Handles large datasets efficiently

Reduces overfitting

Works well with tabular data

📈 Evaluation Metrics

Accuracy Score

Confusion Matrix

Classification Report
