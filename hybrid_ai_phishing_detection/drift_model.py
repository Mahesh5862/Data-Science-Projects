from sklearn.ensemble import IsolationForest
import numpy as np

class DriftDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.2, random_state=42)

    def train(self, feature_list):
        self.model.fit(feature_list)

    def predict(self, features):
        score = self.model.decision_function([features])
        return float(score[0])
