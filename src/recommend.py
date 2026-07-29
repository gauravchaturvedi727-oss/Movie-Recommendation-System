import pickle
import requests
from urllib.parse import quote

API_KEY = "8d9afb57"
movies = pickle.load(open("model/movie_list.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))

def fetch_movie_details(movie_name):

    url = f"https://www.omdbapi.com/?apikey={API_KEY}&t={quote(movie_name)}"

    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":

        return {
            "poster": data.get("Poster"),
            "rating": data.get("imdbRating"),
            "year": data.get("Year"),
            "plot": data.get("Plot"),
            "genre": data.get("Genre")
        }

    return {
        "poster": "https://via.placeholder.com/300x450?text=No+Poster",
        "rating": "N/A",
        "year": "N/A",
        "plot": "Not Available",
        "genre": "N/A"
    }


def recommend(movie):

    index = movies[movies["title"] == movie].index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []

    for i in movie_list[1:6]:

        movie_name = movies.iloc[i[0]].title

        details = fetch_movie_details(movie_name)

        recommendations.append({

            "title": movie_name,
            "poster": details["poster"],
            "rating": details["rating"],
            "year": details["year"],
            "plot": details["plot"],
            "genre": details["genre"]

        })

    return recommendations


if __name__ == "__main__":

    result = recommend("Avatar")

    for movie in result:

        print("=" * 50)

        print("Title :", movie["title"])
        print("Year :", movie["year"])
        print("Rating :", movie["rating"])
        print("Genre :", movie["genre"])
        print("Poster :", movie["poster"])
        print("Plot :", movie["plot"])