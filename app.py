import streamlit as st
import pickle
from src.recommend import recommend

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

movies = pickle.load(open("model/movie_list.pkl", "rb"))

st.title("🎬 Movie Recommendation System")
st.write("Get Top 5 Similar Movie Recommendations")

selected_movie = st.selectbox(
    "Select a Movie",
    movies["title"].values
)


if st.button("Recommend"):
    results = recommend(selected_movie)
    cols = st.columns(5)
    for col, movie in zip(cols, results):
        with col:
            st.image(movie["poster"])
            st.markdown(f"### {movie['title']}")
            st.write(f"⭐ IMDb : {movie['rating']}")
            st.write(f"📅 {movie['year']}")
            st.write(f"🎭 {movie['genre']}")
            st.caption(movie["plot"])