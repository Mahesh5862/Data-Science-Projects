import nltk
import numpy as np
from collections import Counter
import math
import string

# Safe download (will not redownload if already installed)
nltk.download('punkt')

def entropy(words):
    if len(words) == 0:
        return 0
    
    freq = Counter(words)
    total = len(words)
    
    return -sum(
        (count / total) * math.log2(count / total)
        for count in freq.values()
    )

def extract_features(text):
    text = text.strip()

    if len(text) == 0:
        return [0] * 9

    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)

    # -------------------------
    # Basic Linguistic Features
    # -------------------------
    avg_sentence_length = (
        np.mean([len(s.split()) for s in sentences])
        if sentences else 0
    )

    word_entropy = entropy(words)

    unique_ratio = (
        len(set(words)) / len(words)
        if words else 0
    )

    # -------------------------
    # Capitalization Behavior
    # -------------------------
    capital_ratio = sum(
        1 for c in text if c.isupper()
    ) / len(text)

    # -------------------------
    # Punctuation Behavior
    # -------------------------
    exclamation_count = text.count("!")
    question_count = text.count("?")

    punctuation_ratio = sum(
        1 for c in text if c in string.punctuation
    ) / len(text)

    # -------------------------
    # Urgency Indicators
    # -------------------------
    urgent_words = [
        "urgent",
        "immediately",
        "confidential",
        "transfer",
        "asap",
        "now"
    ]

    urgent_count = sum(
        text.lower().count(word)
        for word in urgent_words
    )

    # -------------------------
    # Suspicious Phrase Patterns
    # -------------------------
    suspicious_phrases = [
        "transfer funds",
        "bank account",
        "wire money",
        "act immediately",
        "must be done now"
    ]

    suspicious_phrase_count = sum(
        text.lower().count(phrase)
        for phrase in suspicious_phrases
    )

    return [
        avg_sentence_length,
        word_entropy,
        unique_ratio,
        capital_ratio,
        exclamation_count,
        question_count,
        punctuation_ratio,
        urgent_count,
        suspicious_phrase_count
    ]
