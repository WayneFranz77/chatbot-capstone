import json
import random


class ResponseSelector:

    def __init__(self, filepath):

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            self.data = json.load(file)

    def get_response(self, tag):

        for intent in self.data["intents"]:

            if intent["tag"] == tag:

                return random.choice(
                    intent["responses"]
                )

        return (
            "I'm sorry, I don't understand."
        )


if __name__ == "__main__":

    selector = ResponseSelector(
        "data/intents.json"
    )

    print(
        selector.get_response(
            "machine_learning"
        )
    )