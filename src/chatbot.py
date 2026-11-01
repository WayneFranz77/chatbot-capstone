from src.intent_classifier import IntentClassifier
from src.entity_recognition import extract_entities
from src.response_selector import ResponseSelector


class ChatBot:

    def __init__(self):

        self.intent_classifier = IntentClassifier()

        self.intent_classifier.load_training_data("data/intents.json")

        self.intent_classifier.train()

        self.response_selector = ResponseSelector("data/intents.json")

    def get_response(self, user_input):

        intent, confidence = self.intent_classifier.predict(user_input)

        entities = extract_entities(user_input)

        response = self.response_selector.get_response(intent)

        if confidence < 0.20:

            return {
                "intent": "unknown",
                "confidence": confidence,
                "entities": entities,
                "response": (
                    "I'm not confident I understand "
                    "that question. Could you rephrase it?"
                ),
            }

        return {
            "intent": intent,
            "confidence": confidence,
            "entities": entities,
            "response": response,
        }


if __name__ == "__main__":

    chatbot = ChatBot()

    result = chatbot.get_response("Tell me about Python and AI-900")

    print(result)
