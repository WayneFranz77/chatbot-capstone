from gensim.models import Word2Vec

from preprocessing import preprocess_text


training_sentences = [
    "Python is used for machine learning",
    "Machine learning is part of artificial intelligence",
    "Data science uses Python and statistics",
    "Azure provides artificial intelligence services",
    "AI engineers build machine learning systems",
    "Deep learning is a subset of machine learning",
    "Python is widely used in data science",
    "Azure AI supports intelligent applications",
    "Statistics is important for data science",
    "AI certification helps advance careers"]


processed_sentences = [preprocess_text(sentence)
    for sentence in training_sentences]


model = Word2Vec(sentences=processed_sentences, vector_size=100,
    window=5, min_count=1, workers=4, epochs=100)


if __name__ == "__main__":

    print("\nVocabulary\n")
    print(model.wv.index_to_key)

    print("\nSimilarity\n")

    print("python vs data:", model.wv.similarity("python", "data"))
    print("machine vs learning:", model.wv.similarity("machine", "learning"))

    print("\nMost Similar To Python\n")

    print(model.wv.most_similar("python", topn=5))