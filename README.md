Mahesh (Mahi)
B.Tech Computer Science
Focused on Machine Learning, AI Systems & Cybersecurity

📌 Repository Overview

This repository contains multiple end-to-end Data Science and AI projects built from scratch using Python and Machine Learning.

Each project follows the complete ML lifecycle:

Data Collection → Data Cleaning → Feature Engineering → 
Model Training → Evaluation → Deployment

The projects demonstrate practical implementation of:

Supervised Machine Learning

Transformer-based Semantic Intelligence

Hybrid AI Systems

Explainable AI (XAI)

Cybersecurity Applications

Cloud Deployment using Streamlit

📂 Repository Structure
Data-Science-Projects/
│
├── hybrid_ai_phishing_detection/
├── Network_Anomaly_Detection/
├── Diabetes_Prediction/
├── Titanic_Modeling/
├── Titanic_Data_Preprocessing/
├── sales_prediction/
└── README.md
🔐 1️⃣ Hybrid AI Phishing Detection System
📌 Overview

A Hybrid AI Cybersecurity system that detects phishing messages using a multi-layer AI architecture.

🧠 AI Architecture
🔹 Layer 1 — Statistical Machine Learning

TF-IDF Vectorization

Logistic Regression Classifier

🔹 Layer 2 — Transformer Semantic Intelligence

Sentence Transformer embeddings

Semantic similarity scoring

🔹 Layer 3 — Hybrid Risk Aggregation

Final Risk Score is computed using weighted combination:

Final Score = 0.6 × ML Score + 0.4 × Semantic Score
🔹 Layer 4 — Explainable AI

Top influential word extraction

Risk explanation generator

Prevention advice layer

📊 Dataset Used

Custom phishing dataset:

phishing_dataset.csv

Columns:

text

label (0 = Normal, 1 = Phishing)

📈 Evaluation Metrics

Accuracy

Precision

Recall

F1 Score

Confusion Matrix

🌐 Deployment

Deployed using Streamlit Cloud.

Live Demo:
(Insert your Streamlit app link here)

🌐 2️⃣ Network Anomaly Detection Using Machine Learning
📌 Project Overview

This project detects DDoS attacks using the CICIDS 2017 intrusion detection dataset.

The model classifies network traffic as:

BENIGN (0)

DDoS (1)

📊 Dataset Used

CICIDS 2017 Dataset
File Used:

Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv

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

Model Evaluation using Accuracy & Confusion Matrix

🤖 Model Used

Random Forest Classifier

Why Random Forest?

Handles large tabular datasets efficiently

Reduces overfitting

Strong performance for structured intrusion data

📈 Evaluation Metrics

Accuracy Score

Confusion Matrix

Classification Report

🩺 3️⃣ Diabetes Prediction
📌 Overview

Predicts whether a patient has diabetes based on medical attributes.

Techniques Used:

Logistic Regression

Data Preprocessing

Train-Test Split

Model Evaluation

🚢 4️⃣ Titanic Survival Prediction
📌 Overview

Predicts passenger survival using classification models.

Techniques Used:

Data Cleaning

Feature Engineering

Logistic Regression

Exploratory Data Analysis (EDA)

📊 5️⃣ Sales Prediction
📌 Overview

Regression-based model to predict sales based on business features.

🧠 Technologies Used Across Projects

Python

Pandas

NumPy

Scikit-learn

Sentence Transformers

PyTorch

Streamlit

Matplotlib

Seaborn

🔎 Machine Learning & AI Concepts Applied

Supervised Learning

Classification

Regression

Feature Engineering

TF-IDF Vectorization

Logistic Regression

Random Forest

Transformer Embeddings

Semantic Similarity

Hybrid AI Architecture

Explainable AI (XAI)

Cloud Deployment

🎯 Key Highlights

✅ Built Hybrid AI Cybersecurity system
✅ Implemented Transformer semantic intelligence
✅ Designed multi-layer AI architecture
✅ Deployed ML system to cloud (Streamlit)
✅ Built DDoS detection model using real intrusion dataset
✅ Implemented full ML pipeline from preprocessing to deployment

📦 Installation Guide

To run any project locally:

git clone https://github.com/Mahesh5862/Data-Science-Projects.git
cd Data-Science-Projects/project-folder-name
pip install -r requirements.txt
streamlit run app.py
🚀 Future Improvements

Add REST API endpoints

Add Docker containerization

Improve UI dashboards

Add real-time detection pipeline

Integrate advanced LLM-based explanation engine

👨‍💻 About Me

Mahesh
Aspiring AI & Cybersecurity Engineer
Interested in:

Machine Learning

AI Security Systems

Transformer-based Intelligence

Applied Cyber Defense

⭐ Final Note

This repository demonstrates practical application of Machine Learning and AI in:

Cybersecurity (Phishing & DDoS Detection)

Healthcare Prediction

Business Analytics

Predictive Modeling

All projects are built with real-world structure and deployment practices.
