🏥 ClinRAG™
AI-Powered Clinical Trial Recruitment Intelligence Platform
📌 Overview

ClinRAG™ is an AI-powered Clinical Trial Recruitment and Eligibility Screening System designed to automate the process of matching patients with relevant clinical trials and identifying eligible patients for ongoing trials.

The platform integrates:

Electronic Health Record (EHR) data

ClinicalTrials.gov live API

Rule-based AI eligibility engine

Risk scoring mechanism

Retrieval-style eligibility reasoning

ClinRAG simulates a real-world healthcare AI system used by hospitals, research institutions, and pharmaceutical companies to improve clinical trial recruitment efficiency.

🎯 Problem Statement

Clinical trial recruitment is one of the biggest bottlenecks in medical research.

Before ClinRAG:

Manual screening of patient records

High recruitment failure rates

Poor patient awareness of trials

Time-consuming eligibility verification

After ClinRAG:

Automated patient-trial matching

AI-generated eligibility reasoning

Risk-level assessment

Ranked trial recommendations

Scalable recruitment engine

🧠 System Modes
🟢 Mode 1: Patient → Trial Screening

Input:

Patient EHR JSON

Selected medical condition

Output:

Ranked list of matching trials

Eligibility status

AI reasoning

Risk score

Confidence level

🔵 Mode 2: Trial → Patient Recruitment

Input:

Disease name

Selected clinical trial

Output:

List of eligible patients

Age & condition details

Matching score

Recruitment-ready shortlist

🏗 System Architecture
User Input
   ↓
Disease / Patient Selection
   ↓
ClinicalTrials.gov API Fetch
   ↓
Trial Normalization & Parsing
   ↓
Eligibility Matching Engine
   ↓
RAG-style Explanation Generator
   ↓
Risk Scoring Module
   ↓
Streamlit UI Display
📂 Project Structure
ClinRAG/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
│
├── src/
│   ├── data_loader.py
│   ├── disease_normalizer.py
│   ├── dynamic_trial_fetcher.py
│   ├── trial_matcher.py
│   ├── reverse_trial_matcher.py
│   ├── rag_eligibility_engine.py
│   ├── risk_scoring.py
│   ├── risk_disclosure.py
│   └── audit_logger.py
│
├── data/
│   ├── ehr_samples/            # Synthetic EHR JSON patient records
│   ├── icd_mapping/            # ICD-10 mapping files
│   ├── guidelines/             # Clinical guideline PDFs
│   └── regulations/            # Regulatory documents
📊 Datasets Used
1️⃣ Clinical Trials Data

Source: ClinicalTrials.gov API

Format: JSON

Contains:

Trial ID (NCT)

Conditions

Eligibility criteria

Age requirements

Retrieved dynamically via REST API.

2️⃣ Electronic Health Records (EHR)

Synthetic patient JSON files

Includes:

Age

Gender

Diagnosed conditions

Medical history

Used to simulate hospital patient database.

3️⃣ ICD-10 Mapping

ICD-10 CM Codes (2025 edition)

Used for disease normalization and matching.

🤖 Models & Algorithms Used
1️⃣ Rule-Based Matching Algorithm

Implemented in:

src/trial_matcher.py
Matching Logic:

Condition similarity (substring-based matching)

Age eligibility filtering

Score calculation:

+3 for condition match

+1 for minimum age match

+1 for maximum age match

Outputs ranked list of trials.

2️⃣ Reverse Recruitment Engine

Implemented in:

src/reverse_trial_matcher.py

Iterates through entire EHR dataset

Applies eligibility matching logic

Returns ranked list of eligible patients

3️⃣ RAG-Style Eligibility Reasoning

Implemented in:

src/rag_eligibility_engine.py

Generates:

Age reasoning

Condition reasoning

Structured eligibility explanation

Simulates Retrieval-Augmented Generation behavior without external LLM dependency.

4️⃣ Risk Scoring System

Implemented in:

src/risk_scoring.py

Classifies risk into:

Low

Moderate

High

Based on:

Age compliance

Condition match strength

Eligibility confidence

📥 System Inputs
Patient Screening Mode

Patient JSON file

Selected condition

Trial Recruitment Mode

Disease name

Selected trial ID

📤 System Outputs

Ranked trials

Eligibility status

Matching score

AI-generated explanation

Risk level

Confidence score

Eligible patient list

🖥 Technologies Used
Technology	Purpose
Python	Backend logic
Streamlit	Web application UI
JSON	Data storage
ClinicalTrials API	Live trial retrieval
ICD-10 Mapping	Disease normalization
Rule-based AI	Eligibility logic
🚀 Installation Guide
1️⃣ Clone Repository
git clone https://github.com/Mahesh5862/Data-Science-Projects.git
cd Data-Science-Projects/ClinRAG
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows:

venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Application
streamlit run app.py
🌍 Deployment

Platform: Streamlit Cloud

Main Module:

ClinRAG/app.py

Python Version:

3.11
👥 Target Users

Hospitals

Pharmaceutical companies

Clinical research organizations

Healthcare data scientists

Medical researchers

Healthcare AI developers

📈 Real-World Applications

Automated clinical trial recruitment

Patient eligibility pre-screening

Trial feasibility analysis

Healthcare decision-support systems

AI-based research analytics

⚠️ Limitations

Synthetic EHR dataset

Rule-based matching (no deep NLP embeddings)

Depends on ClinicalTrials API availability

Not connected to live hospital EHR systems

🔮 Future Improvements

Transformer-based medical embeddings

Semantic similarity matching

Integration with real hospital EHR APIs

Secure authentication system

Cloud-native deployment (AWS/Azure)

Role-based access control

Advanced AI-driven eligibility scoring

🏆 Why This Project Is Valuable

Solves a real healthcare bottleneck

Demonstrates full-stack AI integration

Combines API integration + data engineering + logic engine

Deployable and scalable

Industry-relevant use case

Strong portfolio project for Data Science / AI roles

👨‍💻 Author

Mahesh (Mahi)
Data Science & AI Enthusiast
RGUKT Basar

📜 License

Educational and Research Use Only
