import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


class IntentClassifier:

    def __init__(self):

        self.vectorizer = TfidfVectorizer()

        self.classifier = LogisticRegression(max_iter=1000, random_state=42)

        self.patterns = []
        self.labels = []

    def load_training_data(self, filepath):

        with open(filepath, "r", encoding="utf-8") as file:

            data = json.load(file)

        for intent in data["intents"]:

            for pattern in intent["patterns"]:

                self.patterns.append(pattern)
                self.labels.append(intent["tag"])

    def train(self):

        X = self.vectorizer.fit_transform(self.patterns)

        self.classifier.fit(X, self.labels)

    def predict(self, text):

        X = self.vectorizer.transform([text])

        prediction = self.classifier.predict(X)[0]

        confidence = max(self.classifier.predict_proba(X)[0])

        return prediction, confidence


if __name__ == "__main__":

    classifier = IntentClassifier()

    classifier.load_training_data("data/intents.json")

    classifier.train()

    test_questions = [
        "Tell me about TensorFlow",
        "What is NumPy?",
        "How do I become an AI engineer?",
        "What is deep learning?",
        "Tell me about pandas",
    ]

    for question in test_questions:

        intent, confidence = classifier.predict(question)

        print(f"Question: {question}")

        print(f"Intent: {intent}")

        print(f"Confidence: {confidence:.2%}\n")
