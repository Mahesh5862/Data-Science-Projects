import streamlit as st
from phishing_model import PhishingDetector

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="Hybrid AI Phishing Detection",
    page_icon="🛡️",
    layout="centered"
)

# ------------------------------
# Custom CSS Styling
# ------------------------------
st.markdown("""
<style>
body {
    background-color: #0E1117;
}
.main-title {
    font-size: 40px;
    font-weight: 800;
    color: #00E5FF;
    text-align: center;
}
.sub-title {
    font-size: 18px;
    color: #A0A0A0;
    text-align: center;
    margin-bottom: 30px;
}
.section-header {
    font-size: 24px;
    font-weight: 600;
    color: #FFB703;
    margin-top: 30px;
}
.risk-card {
    background-color: #1F2937;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Title Section
# ------------------------------
st.markdown('<div class="main-title">🛡 Hybrid AI Phishing Detection System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Supervised ML + Transformer Semantic Intelligence + Explainable AI</div>', unsafe_allow_html=True)

# ------------------------------
# AI Explanation Generator
# ------------------------------
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
        advice = "Avoid clicking links or transferring funds. Verify the request through official channels."
    elif 40 <= final_score < 70:
        advice = "Be cautious. Confirm the authenticity before responding."
    else:
        advice = "The message appears safe, but always stay alert."

    return " ".join(explanation), advice


# ------------------------------
# Load & Train Model
# ------------------------------
@st.cache_resource
def load_model():
    model = PhishingDetector()
    model.train("phishing_dataset.csv")
    return model

detector = load_model()

# ------------------------------
# User Input Section
# ------------------------------
st.markdown('<div class="section-header">✉ Analyze Message</div>', unsafe_allow_html=True)

user_input = st.text_area("Enter message to analyze:", height=150)

if st.button("🚀 Analyze Message"):

    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # ML Probability
        ml_probability = detector.predict_proba(user_input)
        ml_score = ml_probability * 100

        # Transformer Semantic
        semantic_similarity = detector.semantic_score(user_input)
        semantic_score = semantic_similarity * 100

        # Hybrid Score
        final_score = int(min(100, (0.6 * ml_score) + (0.4 * semantic_score)))

        # Risk Card
        st.markdown(f"""
        <div class="risk-card">
            <h2 style="color:#00E5FF;">🔐 Final Hybrid Risk Score</h2>
            <h1 style="color:#FF4B4B;">{final_score}%</h1>
        </div>
        """, unsafe_allow_html=True)

        st.progress(final_score / 100)

        # Individual Scores
        col1, col2 = st.columns(2)
        col1.metric("📊 ML Score", f"{round(ml_score,2)}%")
        col2.metric("🧠 Transformer Score", f"{round(semantic_score,2)}%")

        # Classification
        if final_score < 35:
            st.success("🟢 Likely Normal Communication")
        elif 35 <= final_score < 60:
            st.warning("🟡 Suspicious Communication")
        else:
            st.error("🔴 High Probability Phishing Detected!")

        # AI Explanation
        explanation, advice = generate_explanation(user_input, final_score)

        st.markdown('<div class="section-header">🤖 AI Explanation</div>', unsafe_allow_html=True)
        st.write(explanation)

        st.markdown('<div class="section-header">🛡 Prevention Advice</div>', unsafe_allow_html=True)
        st.write(advice)

        # Influential Words
        if hasattr(detector, "explain_prediction"):
            important_words = detector.explain_prediction(user_input)

            st.markdown('<div class="section-header">🔍 Top Influential Words (ML Layer)</div>', unsafe_allow_html=True)
            for word, score in important_words:
                st.write(f"{word} → {round(score, 3)}")

# ------------------------------
# Model Performance Section
# ------------------------------
st.markdown("---")
st.markdown('<div class="section-header">📊 Model Performance (Test Set)</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Accuracy", f"{round(detector.accuracy * 100, 2)}%")
col2.metric("Precision", f"{round(detector.precision * 100, 2)}%")
col3.metric("Recall", f"{round(detector.recall * 100, 2)}%")
col4.metric("F1 Score", f"{round(detector.f1 * 100, 2)}%")

st.markdown('<div class="section-header">📉 Confusion Matrix</div>', unsafe_allow_html=True)
st.write(detector.conf_matrix)
