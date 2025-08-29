# recommender.py

import pandas as pd
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict, Any

# Load the scraped data from your CSV file
try:
    df = pd.read_csv('imdb_2024_movies.csv')
    df.dropna(inplace=True)  # Clean up any rows with missing data
except FileNotFoundError:
    print("Error: The 'imdb_2024_movies.csv' file was not found. Please run scraper.py first.")
    exit()

# Preprocessing function for the storylines
def preprocess_text(text: str) -> str:
    """
    Cleans and preprocesses the text for NLP analysis.
    This includes removing non-alphabetic characters, converting to lowercase,
    and removing common stopwords.
    """
    if not isinstance(text, str):
        return ""
    
    # Remove all non-alphabetic characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Convert text to lowercase
    text = text.lower()
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    
    return " ".join(filtered_words)

# Apply preprocessing to the 'Storyline' column
df['processed_storyline'] = df['Storyline'].apply(preprocess_text)

# Initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['processed_storyline'])

# Calculate the Cosine Similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get movie recommendations
def get_recommendations_by_storyline(user_input_storyline: str, num_recommendations: int = 5) -> List[Dict[str, str]]:
    """
    Recommends movies based on a user-provided storyline using Cosine Similarity.
    """
    # Preprocess the user's input
    processed_input = preprocess_text(user_input_storyline)
    
    if not processed_input:
        return []
    
    # Transform the user's input into a TF-IDF vector
    user_input_vector = tfidf_vectorizer.transform([processed_input])
    
    # Calculate the similarity scores between the user's input and all movies
    cosine_scores = cosine_similarity(user_input_vector, tfidf_matrix).flatten()
    
    # Get the indices of the top N most similar movies
    top_indices = cosine_scores.argsort()[-num_recommendations:][::-1]
    
    # Get the movie details for the recommendations
    recommendations = []
    for index in top_indices:
        movie_info = {
            "name": df['Movie Name'].iloc[index],
            "storyline": df['Storyline'].iloc[index]
        }
        recommendations.append(movie_info)
        
    return recommendations