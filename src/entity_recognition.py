import re


TECH_ENTITIES = [
    "python",
    "machine learning",
    "ai",
    "artificial intelligence",
    "data science",
    "azure",
    "ai-900",
    "tensorflow",
    "pytorch",
    "streamlit"
]


def extract_entities(text):

    text = text.lower()

    entities_found = []

    for entity in TECH_ENTITIES:

        if entity in text:
            entities_found.append(entity)

    return entities_found


if __name__ == "__main__":

    sample = (
        "Tell me about Python and AI-900 certification"
    )

    print(extract_entities(sample))