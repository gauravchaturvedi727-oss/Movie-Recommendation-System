import pandas as pd
import ast


def convert(text):
    data = ast.literal_eval(text)
    result = []

    for item in data:
        result.append(item["name"])
    return result


def convert_cast(text):
    data = ast.literal_eval(text)
    result = []

    for i, item in enumerate(data):
        if i != 3:
            result.append(item["name"])
        else:
            break

    return result


def fetch_director(text):
    data = ast.literal_eval(text)

    for item in data:
        if item["job"] == "Director":
            return [item["name"]]

    return []


def remove_space(words):
    return [word.replace(" ", "") for word in words]

def preprocess():

    movies = pd.read_csv("dataset/tmdb_5000_movies.csv")
    credits = pd.read_csv("dataset/tmdb_5000_credits.csv")

    movies = movies.merge(credits, on="title")

    movies = movies[
        [
            "movie_id",
            "title",
            "overview",
            "genres",
            "keywords",
            "cast",
            "crew",
        ]
    ]

    movies.dropna(inplace=True)

    movies["genres"] = movies["genres"].apply(convert)
    movies["keywords"] = movies["keywords"].apply(convert)
    movies["cast"] = movies["cast"].apply(convert_cast)
    movies["crew"] = movies["crew"].apply(fetch_director)

    movies["overview"] = movies["overview"].apply(lambda x: x.split())

    movies["genres"] = movies["genres"].apply(remove_space)
    movies["keywords"] = movies["keywords"].apply(remove_space)
    movies["cast"] = movies["cast"].apply(remove_space)
    movies["crew"] = movies["crew"].apply(remove_space)

    movies["tags"] = (
        movies["overview"]
        + movies["genres"]
        + movies["keywords"]
        + movies["cast"]
        + movies["crew"]
    )

    new_df = movies[["movie_id", "title", "tags"]].copy()
    new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x))
    new_df["tags"] = new_df["tags"].apply(lambda x: x.lower())
    return new_df

if __name__ == "__main__":
    df = preprocess()
    print(df.head())
    print("\nShape:", df.shape)