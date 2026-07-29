import os
import pickle

from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess

ps = PorterStemmer()

def stem(text):
    words = text.split()
    stemmed_words = []
    for word in words:
        stemmed_words.append(ps.stem(word))
    return " ".join(stemmed_words)


def train():
    print("Loading cleaned data...")
    movies = preprocess()
    print("Applying stemming...")
    movies["tags"] = movies["tags"].apply(stem)
    print("Creating vectors...")
    cv = CountVectorizer(
        max_features=5000,
        stop_words="english"
    )
    vectors = cv.fit_transform(movies["tags"]).toarray()
    print("Calculating cosine similarity...")
    similarity = cosine_similarity(vectors)
    os.makedirs("model", exist_ok=True)
    pickle.dump(
        movies,
        open("model/movie_list.pkl", "wb")
    )
    pickle.dump(
        similarity,
        open("model/similarity.pkl", "wb")
    )
    print("\nTraining Completed Successfully!")
    print("movie_list.pkl saved")
    print("similarity.pkl saved")


if __name__ == "__main__":
    train()