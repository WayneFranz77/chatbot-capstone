TECH_ENTITIES = [
    "python",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "ai",
    "data science",
    "statistics",
    "azure",
    "ai-900",
    "ai-102",
    "tensorflow",
    "pytorch",
    "numpy",
    "pandas",
    "neural networks",
    "chatbot",
]


def extract_entities(text):

    text = text.lower()

    entities_found = []

    for entity in TECH_ENTITIES:

        if entity in text:
            entities_found.append(entity)

    return entities_found


if __name__ == "__main__":

    sample = "Tell me about TensorFlow, PyTorch and AI-102 certification"

    print(extract_entities(sample))
