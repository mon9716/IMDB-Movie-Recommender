import nltk
nltk.download('stopwords')

# scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from typing import List, Dict, Any

# --- Constants ---
IMDB_URL = "https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31"
CSV_FILE_PATH = "imdb_2024_movies.csv"

# --- Setup Selenium WebDriver ---
def setup_driver() -> webdriver.Chrome:
    """
    Sets up and returns a Chrome WebDriver instance.
    Handles the installation and management of the correct ChromeDriver.
    """
    print("Setting up Selenium WebDriver...")
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        print("WebDriver setup successful!")
        return driver
    except Exception as e:
        print(f"Error setting up WebDriver: {e}")
        print("Please ensure you have a compatible Chrome browser installed.")
        return None

# --- Main Scraping Function ---
def scrape_imdb(driver: webdriver.Chrome) -> List[Dict[str, str]]:
    """
    Navigates to the IMDB URL, scrapes movie data, and returns it as a list of dictionaries.
    """
    if driver is None:
        return []

    print(f"Navigating to {IMDB_URL}...")
    driver.get(IMDB_URL)
    time.sleep(5) # Give the page some time to load all dynamic content.
    
    movie_data = []
    
    # Find all the movie list items on the page.
    movie_list_items = driver.find_elements(By.CSS_SELECTOR, '.ipc-metadata-list-summary-item')
    
    if not movie_list_items:
        print("No movie items found. Please check the CSS selector or the URL.")
    
    for item in movie_list_items:
        try:
            # Scrape the movie name and storyline.
            movie_name_element = item.find_element(By.CSS_SELECTOR, '.ipc-title__text')
            storyline_element = item.find_element(By.CSS_SELECTOR, '.ipc-html-content-inner-div')
            
            # Clean the data.
            movie_name = movie_name_element.text.split(' ', 1)[1].strip() if movie_name_element.text else "N/A"
            storyline = storyline_element.text.strip() if storyline_element.text else "N/A"
            
            # Store the data as a dictionary.
            movie_data.append({"Movie Name": movie_name, "Storyline": storyline})
            print(f"Scraped: {movie_name}")
            
        except Exception as e:
            print(f"Skipping a movie due to an error: {e}")
            continue
            
    print(f"Scraping complete. Found {len(movie_data)} movies.")
    return movie_data

def save_to_csv(data: List[Dict[str, str]], file_path: str):
    """
    Saves a list of dictionaries to a CSV file using pandas.
    """
    if not data:
        print("No data to save.")
        return
        
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"\nData successfully saved to {file_path}")
    print("\nFirst 5 rows of the DataFrame:")
    print(df.head()) # This is useful for verification.

# --- Execution ---
if __name__ == "__main__":
    driver = setup_driver()
    if driver:
        scraped_movies = scrape_imdb(driver)
        driver.quit()  # Close the browser instance.
        save_to_csv(scraped_movies, CSV_FILE_PATH)