## 🎬 MoviePlot Recommender: An IMDB-Powered Recommendation System

This project is an end-to-end movie recommendation application that finds and suggests films based on the similarity of their storylines. It's built as a full-stack data science project, starting with data collection from IMDB and culminating in an interactive web application.

-----

### 🌟 Project Highlights

  - **Data-Driven Discovery:** Utilizes **web scraping** with **Selenium** to gather movie titles and plot summaries from IMDB's 2024 film releases.
  - **Intelligent Recommendations:** Implements a text-based recommendation engine powered by **Natural Language Processing (NLP)**, specifically **TF-IDF** for text vectorization and **Cosine Similarity** to calculate film-to-film likeness.
  - **Seamless User Experience:** Delivers a clean, intuitive, and interactive user interface using the **Streamlit** framework, allowing anyone to get personalized recommendations instantly.
  - **Robust Architecture:** The project is modular, with dedicated scripts for scraping, data processing, and the final application, ensuring clarity and maintainability.

-----

### ⚙️ Getting Started

Follow these simple steps to get the application running on your local machine.

#### 1\. Clone the Repository

Begin by cloning the project files from GitHub to your local system.

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

*(Remember to replace `your-username/your-repository-name` with your actual repository link.)*

#### 2\. Set Up the Environment

It's best practice to work within a dedicated virtual environment.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS / Linux:
source venv/bin/activate
```

#### 3\. Install Dependencies

Install all the necessary Python libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

-----

### ▶️ How to Run the App

The process involves two quick steps: collecting the data and then launching the application.

#### Step 1: Gather Movie Data

Run the `scraper.py` script to collect movie titles and storylines from IMDB. This action will create the `imdb_2024_movies.csv` file, which serves as the dataset for your recommendation engine.

```bash
python scraper.py
```

#### Step 2: Launch the Web App

Once the data file is successfully generated, start the Streamlit application.

```bash
streamlit run app.py
```

Your web browser will automatically open a new tab with the **MoviePlot Recommender** ready for use.

-----

### 📚 Core Technologies

  * **Languages:** Python
  * **Libraries:** Selenium, Pandas, Scikit-learn, NLTK, Streamlit
  * **Concepts:** Web Scraping, Natural Language Processing (NLP), TF-IDF, Cosine Similarity
  * **Tools:** Git, GitHub

📹 Project Demo
Check out a short video demonstration of the app in action on LinkedIn:
(https://www.linkedin.com/posts/monica-umamageswaran_python-datascience-machinelearning-activity-7367219819949027329-iLug?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE_7PqYBCyvYmCOnir7XtTdIJhnL6JtNqSA)
