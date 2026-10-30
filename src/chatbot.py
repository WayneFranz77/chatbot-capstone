from intent_classifier import IntentClassifier
from entity_recognition import extract_entities
from response_selector import ResponseSelector


class ChatBot:

    def __init__(self):

        self.intent_classifier = IntentClassifier()

        self.intent_classifier.load_training_data(
            "data/intents.json"
        )

        self.intent_classifier.train()

        self.response_selector = ResponseSelector(
            "data/intents.json"
        )

    def get_response(self, user_input):

        intent = self.intent_classifier.predict(
            user_input
        )

        entities = extract_entities(
            user_input
        )

        response = self.response_selector.get_response(
            intent
        )

        return {
            "intent": intent,
            "entities": entities,
            "response": response
        }


if __name__ == "__main__":

    chatbot = ChatBot()

    result = chatbot.get_response(
        "Tell me about Python and AI-900"
    )

    print(result)