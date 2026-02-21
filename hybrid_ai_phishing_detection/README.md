Hybrid AI Phishing Detection System
(Supervised ML + Transformer Semantic Intelligence)



🛡️ Hybrid AI Phishing Detection System
Supervised Machine Learning + Transformer-Based Semantic Analysis
📌 Project Overview

This project implements a Hybrid AI-based Phishing Detection System that analyzes user-entered messages and predicts phishing risk using a combination of:

TF-IDF + Logistic Regression (Supervised Machine Learning)

Transformer-based Semantic Similarity

Hybrid Risk Aggregation Model

Rule-based AI Explanation Layer

Word-level Explainable AI

The system classifies messages into:

🟢 Likely Normal Communication

🟡 Suspicious Communication

🔴 High Probability Phishing

The final risk score is computed using both statistical probability and semantic similarity.

🧠 AI Type Used in This Project

This project belongs to:

✔ Supervised Machine Learning
✔ NLP-Based Classification
✔ Transformer Embedding-Based Semantic Analysis
✔ Hybrid AI System

It is NOT:

✘ Large Language Model (LLM)
✘ Generative AI
✘ Fine-tuned Transformer classifier

The transformer is used only for sentence embeddings and semantic similarity.

⚙️ System Architecture

User Input
→ TF-IDF Vectorization
→ Logistic Regression → ML Probability Score
→ Sentence Transformer → Semantic Similarity Score
→ Hybrid Risk Aggregation
→ AI Explanation + Prevention Advice
→ Word-Level Feature Importance

📊 Dataset Used

File:

data/phishing_dataset.csv

Structure:

text	label
Message content	0 or 1

Label Encoding:

0 → Normal

1 → Phishing

The dataset is used to train and evaluate the Logistic Regression model.

🤖 Models & Algorithms Used
1️⃣ TF-IDF Vectorizer

Converts text into numerical feature vectors.

Captures word importance.

Used as input to Logistic Regression.

2️⃣ Logistic Regression (Supervised ML)

Binary classification algorithm.

Outputs phishing probability between 0 and 1.

Used as the statistical prediction layer.

3️⃣ Transformer Semantic Similarity

Model Used:

sentence-transformers/all-MiniLM-L6-v2

Source:
https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

Purpose:

Generates sentence embeddings.

Measures semantic similarity between user input and phishing-like patterns.

Produces contextual risk score.

4️⃣ Hybrid Risk Aggregation

Final Score formula:

Final Score = (0.6 × ML Score) + (0.4 × Semantic Score)

This balances:

Statistical classification

Contextual semantic similarity

5️⃣ AI Explanation Layer

The explanation module is rule-based and detects:

Urgency language (urgent, immediately)

Financial transaction words (bank, transfer, funds)

Link-related terms (click, link)

Account verification phrases (verify, account)

It generates:

Human-readable explanation

Prevention advice based on risk level

6️⃣ Explainable AI (ML Layer)

The system extracts:

Top influential words

Logistic Regression coefficient impact

This improves transparency and interpretability.

📈 Model Evaluation Metrics

The system evaluates performance using:

Accuracy

Precision

Recall

F1 Score

Confusion Matrix

These metrics are calculated on a held-out test set.

📂 Project Structure
AI_Phishing_Detection/
│
├── app.py
├── phishing_model.py
├── data/
│   └── phishing_dataset.csv
├── requirements.txt
└── README.md
🚀 Installation & Setup
1️⃣ Create Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate
2️⃣ Install Dependencies
pip install streamlit
pip install pandas
pip install scikit-learn
pip install sentence-transformers

Or:

pip install -r requirements.txt
3️⃣ Run Application
python -m streamlit run app.py

The application will open in your browser.

🧪 Example Test Inputs
🟢 Normal

Please review the attached document and share feedback.

🟡 Suspicious

Please verify your account information before tomorrow.

🔴 High Risk

URGENT: Transfer funds immediately to the bank account provided. Click the link now.

📊 What This Project Demonstrates

✔ Hybrid AI architecture
✔ Supervised ML for phishing detection
✔ Transformer-based semantic scoring
✔ Risk aggregation model
✔ Explainable AI
✔ Real-time phishing risk analysis
✔ Streamlit deployment

⚖ What Exists in This Project

✔ TF-IDF + Logistic Regression
✔ Transformer semantic similarity
✔ Hybrid scoring system
✔ Rule-based explanation
✔ Word-level interpretability
✔ Performance metrics display

❌ What Does Not Exist

❌ Fine-tuned BERT model
❌ LLM-based reasoning
❌ Generative AI text generation
❌ Real-time email server integration
❌ Enterprise deployment

🧠 Conclusion

This project combines classical supervised machine learning and transformer-based semantic intelligence to build a hybrid phishing detection system with explainability and risk advisory features.

It demonstrates practical application of NLP, ML, and hybrid AI architecture in cybersecurity.