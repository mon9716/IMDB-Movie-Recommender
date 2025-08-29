# app.py
import streamlit as st
from recommender import get_recommendations_by_storyline
from typing import List, Dict, Any

# --- Page Configuration ---
st.set_page_config(
    page_title="Personalized Movie Recommender",
    page_icon="🍿",
    layout="centered" # "wide" or "centered"
)

# --- Custom Background (Optional but recommended!) ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title and Introduction ---
st.title("🎬 IMDB Movie Recommender!")
st.markdown("### Find movies that feel just right for you! ✨")
st.markdown("""
Welcome to your personal guide to the **best movies of 2024**! 🍿
Just describe the kind of movie you're in the mood for, and our system will find films with the most similar storylines.
Get ready for some amazing recommendations! 👇
""")

# --- User Input Section ---
user_storyline = st.text_area(
    "📝 **Tell me a storyline you'd love to see:**",
    placeholder="e.g., A young wizard learns magic at a special school.",
    height=150
)

# --- Recommendation Button ---
if st.button("🌟 Find My Perfect Movie! 🌟"):
    if user_storyline:
        with st.spinner("Searching through the cinematic universe for you... 🌌"):
            try:
                # Get recommendations using your function
                recommendations: List[Dict[str, str]] = get_recommendations_by_storyline(user_storyline)
                
                if recommendations:
                    st.success("🎉 **Success! Here are your top 5 personalized recommendations:**")
                    for i, rec in enumerate(recommendations):
                        st.markdown(f"**{i+1}. {rec['name']}**")
                        st.write(f"**Storyline:** {rec['storyline']}")
                        st.markdown("---")
                else:
                    st.warning("🧐 **Hmm, couldn't find a perfect match. Try a different storyline!**")
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.info("💡 **Tip:** Make sure you've successfully created the `imdb_2024_movies.csv` file by running `scraper.py` first.")
    else:
        st.warning("⚠️ **Heads up! Please describe a storyline to get started.**")

st.markdown("---")
st.markdown("© 2024 Movie Recommender Project")