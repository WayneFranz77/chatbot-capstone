"""
Configuration settings for the chatbot project.
"""

DATA_PATH = "data/intents.json"

RANDOM_STATE = 42

TFIDF_MAX_FEATURES = 1000

WORD2VEC_VECTOR_SIZE = 100
WORD2VEC_WINDOW = 5
WORD2VEC_MIN_COUNT = 1
WORD2VEC_WORKERS = 4

DEFAULT_RESPONSE = "I'm sorry, I don't understand that question yet."
