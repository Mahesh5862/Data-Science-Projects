import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class PhishingDetector:

    def __init__(self):
        # ML Layer
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression(max_iter=1000)

        # Transformer Layer
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.phishing_embeddings = []

        # Metrics
        self.accuracy = None
        self.precision = None
        self.recall = None
        self.f1 = None
        self.conf_matrix = None

    def train(self, filepath):
        data = pd.read_csv(filepath)
        X = data["text"]
        y = data["label"]

        # Train-Test Split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)

        # Train ML model
        self.model.fit(X_train_vec, y_train)

        predictions = self.model.predict(X_test_vec)

        # Metrics
        self.accuracy = accuracy_score(y_test, predictions)
        self.precision = precision_score(y_test, predictions)
        self.recall = recall_score(y_test, predictions)
        self.f1 = f1_score(y_test, predictions)
        self.conf_matrix = confusion_matrix(y_test, predictions)

        # Store phishing embeddings for semantic comparison
        phishing_texts = data[data["label"] == 1]["text"]
        self.phishing_embeddings = self.embedding_model.encode(
            phishing_texts.tolist()
        )

    # -------- ML Probability --------
    def predict_proba(self, text):
        X_input = self.vectorizer.transform([text])
        probability = self.model.predict_proba(X_input)[0][1]
        return probability

    # -------- Transformer Semantic Similarity --------
    def semantic_score(self, text):
        input_embedding = self.embedding_model.encode([text])
        similarity_scores = cosine_similarity(
            input_embedding, self.phishing_embeddings
        )
        max_similarity = np.max(similarity_scores)
        return float(max_similarity)

    # -------- Explainability (ML layer) --------
    def explain_prediction(self, text):
        X_input = self.vectorizer.transform([text])
        feature_names = self.vectorizer.get_feature_names_out()
        coefficients = self.model.coef_[0]

        feature_index = X_input.nonzero()[1]
        word_scores = []

        for index in feature_index:
            word_scores.append((feature_names[index], coefficients[index]))

        word_scores = sorted(
            word_scores,
            key=lambda x: abs(x[1]),
            reverse=True
        )

        return word_scores[:5]
