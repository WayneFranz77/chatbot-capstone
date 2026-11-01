from gensim.models import Word2Vec
from src.preprocessing import preprocess_text


class Word2VecManager:

    def __init__(self):

        self.training_sentences = [
            "Python is used for machine learning",
            "Machine learning is part of artificial intelligence",
            "Data science uses Python",
            "Azure AI supports machine learning",
            "AI engineers build intelligent systems",
            "Deep learning is a branch of machine learning",
            "Statistics is useful for data science",
            "Python is popular in artificial intelligence",
            "Azure offers AI services",
            "AI certifications improve careers",
        ]

        processed_sentences = [
            preprocess_text(sentence) for sentence in self.training_sentences
        ]

        self.model = Word2Vec(
            sentences=processed_sentences,
            vector_size=100,
            window=5,
            min_count=1,
            workers=4,
            epochs=100,
        )

    def similarity(self, word1, word2):

        if word1 in self.model.wv and word2 in self.model.wv:
            return self.model.wv.similarity(word1, word2)

        return None

    def most_similar(self, word, topn=5):

        if word in self.model.wv:
            return self.model.wv.most_similar(word, topn=topn)

        return []


if __name__ == "__main__":

    manager = Word2VecManager()

    print()

    print("Similarity:", manager.similarity("python", "data"))

    print()

    print(manager.most_similar("python"))
