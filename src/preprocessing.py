import nltk
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))


def preprocess_text(text):
    """
    Clean and preprocess text.

    Steps:
    1. Lowercase
    2. Tokenize
    3. Remove punctuation
    4. Remove stopwords
    5. Lemmatize
    """

    text = text.lower()

    tokens = word_tokenize(text)

    cleaned_tokens = []

    for token in tokens:

        if token in string.punctuation:
            continue

        if token in stop_words:
            continue

        lemma = lemmatizer.lemmatize(token)

        cleaned_tokens.append(lemma)

    return cleaned_tokens


if __name__ == "__main__":

    sample_text = ("Machine Learning allows computers to learn from data.")

    print(preprocess_text(sample_text))