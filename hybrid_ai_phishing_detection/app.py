import streamlit as st
from phishing_model import PhishingDetector

st.set_page_config(page_title="hybrid_ai_phishing_detection", layout="centered")

st.title("🛡️ hybrid_ai_phishing_detection")

st.markdown("""
This system uses:
- TF-IDF + Logistic Regression (Statistical ML)
- Transformer Semantic Similarity
- Hybrid Risk Aggregation
- Explainable AI
- AI Risk Explanation & Prevention Layer
""")

# -------------------------
# AI Explanation Generator
# -------------------------
def generate_explanation(text, final_score):
    text_lower = text.lower()
    explanation = []
    advice = ""

    if "urgent" in text_lower or "immediately" in text_lower:
        explanation.append("The message creates urgency, which is a common phishing tactic.")

    if "bank" in text_lower or "transfer" in text_lower or "funds" in text_lower:
        explanation.append("It includes financial transaction language, increasing phishing risk.")

    if "click" in text_lower or "link" in text_lower:
        explanation.append("It encourages clicking links, which may redirect to malicious sites.")

    if "verify" in text_lower or "account" in text_lower:
        explanation.append("It requests account verification, which is often used in phishing scams.")

    if not explanation:
        explanation.append("The message does not contain strong phishing indicators.")

    if final_score >= 70:
        advice = "Avoid clicking links or transferring funds. Verify the request through official channels before taking action."
    elif 40 <= final_score < 70:
        advice = "Be cautious. Confirm the authenticity of the request before responding."
    else:
        advice = "The message appears safe, but always remain aware of potential phishing tactics."

    return " ".join(explanation), advice


# -------------------------
# Load & Train Model
# -------------------------
@st.cache_resource
def load_model():
    model = PhishingDetector()
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "phishing_dataset.csv")
    
    model.train(DATA_PATH)
    return model

detector = load_model()

# -------------------------
# User Input Section
# -------------------------
st.markdown("## ✉ Analyze Message")

user_input = st.text_area("Enter message to analyze:")

if st.button("Analyze"):

    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # -------- ML Probability --------
        ml_probability = detector.predict_proba(user_input)
        ml_score = ml_probability * 100

        # -------- Transformer Semantic Similarity --------
        semantic_similarity = detector.semantic_score(user_input)
        semantic_score = semantic_similarity * 100

        # -------- Hybrid Final Score --------
        final_score = int(min(100, (0.6 * ml_score) + (0.4 * semantic_score)))

        st.subheader(f"🔐 Final Hybrid Risk Score: {final_score}%")
        st.progress(final_score / 100)

        st.write(f"📊 ML Probability Score: {round(ml_score,2)}%")
        st.write(f"🧠 Transformer Semantic Score: {round(semantic_score,2)}%")

        # -------- Classification --------
        if final_score < 35:
            st.success("🟢 Likely Normal Communication")
        elif 35 <= final_score < 60:
            st.warning("🟡 Suspicious Communication")
        else:
            st.error("🔴 High Probability Phishing Detected!")

        # -------- AI Explanation Layer --------
        explanation, advice = generate_explanation(user_input, final_score)

        st.markdown("### 🤖 AI Explanation")
        st.write(explanation)

        st.markdown("### 🛡 Prevention Advice")
        st.write(advice)

        # -------- Explainable ML Words --------
        if hasattr(detector, "explain_prediction"):
            important_words = detector.explain_prediction(user_input)

            st.markdown("### 🔍 Top Influential Words (ML Layer)")
            for word, score in important_words:
                st.write(f"{word} → {round(score, 3)}")

# -------------------------
# Metrics Section
# -------------------------
st.markdown("---")
st.markdown("## 📊 Model Performance (Test Set)")

st.write(f"Accuracy: {round(detector.accuracy * 100, 2)}%")
st.write(f"Precision: {round(detector.precision * 100, 2)}%")
st.write(f"Recall: {round(detector.recall * 100, 2)}%")
st.write(f"F1 Score: {round(detector.f1 * 100, 2)}%")

st.markdown("### 📉 Confusion Matrix")
st.write(detector.conf_matrix) 
