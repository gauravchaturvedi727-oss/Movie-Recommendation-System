# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using **Python**, **Scikit-Learn**, and **Streamlit**. The application recommends similar movies based on genres, keywords, cast, crew, and overview using **Natural Language Processing (NLP)** and **Cosine Similarity**.

---

## 🚀 Features

- 🎥 Content-Based Movie Recommendation
- 🧠 NLP-based Feature Engineering
- ✂️ Text Stemming using NLTK
- 📊 CountVectorizer for Text Vectorization
- 📐 Cosine Similarity for Recommendations
- 🌐 Interactive Streamlit Web Application
- 🎞️ Movie Posters and Details using OMDb API
- 🏗️ Modular Project Structure

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- NLTK
- Streamlit
- Requests (OMDb API)

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│
├── dataset/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── train.py
│   ├── recommend.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/gauravchaturvedi727-oss/Movie-Recommendation-System.git
```

Move to the project folder:

```bash
cd Movie-Recommendation-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

Generate the required model files:

```bash
python src/train.py
```

This will create:

- `movie_list.pkl`
- `similarity.pkl`

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. Load movie and credits datasets.
2. Merge both datasets.
3. Extract genres, keywords, cast, director, and overview.
4. Create a combined `tags` column.
5. Apply stemming using NLTK.
6. Convert text into vectors using CountVectorizer.
7. Compute Cosine Similarity.
8. Recommend the Top 5 most similar movies.
9. Fetch movie posters and details using the OMDb API.

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```
Home Screen

Recommendation Results

Movie Posters
```

---

## 🔮 Future Improvements

- Search Autocomplete
- Genre Filtering
- IMDb Rating Filter
- User Login
- Favorites List
- Hybrid Recommendation System
- Deployment on Streamlit Cloud

---

## 👨‍💻 Author

**Gaurav Chaturvedi**

GitHub:
https://github.com/gauravchaturvedi727-oss

---

## ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.
