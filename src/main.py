from src.chatbot import ChatBot


def main():

    chatbot = ChatBot()

    print("=" * 50)
    print("AI Career Advisor Chatbot")
    print("Type 'quit' to exit")
    print("=" * 50)

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        result = chatbot.get_response(user_input)

        print(f"\nIntent: {result['intent']}")

        print(f"Confidence: " f"{result['confidence']:.2%}")

        print(f"Entities: {result['entities']}")

        print(f"Bot: {result['response']}")


if __name__ == "__main__":
    main()
