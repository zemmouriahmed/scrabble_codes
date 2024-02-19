from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import os
from tqdm import tqdm  # Pour afficher une barre de progression
import pandas as pd

def setup_driver():
    driver_options = Options()
    driver_options.add_argument("--headless")  # Pour exécuter en mode sans tête
    driver = webdriver.Edge(options=driver_options, service=Service(EdgeChromiumDriverManager().install()))
    return driver

def create_directory(directory_name):
    os.makedirs(directory_name, exist_ok=True)

def scrape_words(driver, letter):
    url = f'https://www.motscroises.fr/dictionnaire-scrabble/{letter}'  # URL mise à jour pour la correction
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    try:
        word_css_selector = '.mot'  # Sélecteur CSS mis à jour pour correspondre à la structure de la page
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, word_css_selector)))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        tds = soup.select(word_css_selector)
        return tds
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []

def parse_words(tds, letter):
    vocabulaire = [td.text.strip() for td in tds if td.text.strip()]
    return vocabulaire

def write_words_to_file(vocabulaire, letter, directory='scrabble_vocabularies1'):
    filepath = os.path.join(directory, f'{letter}.txt')
    with open(filepath, 'w', encoding='utf-8') as f:
        for mot in vocabulaire:
            f.write(f"{mot}\n")

def main():
    driver = setup_driver()
    create_directory('scrabble_vocabularies1')

    for letter in tqdm(range(97, 123), desc='Overall Progress'):
        char_letter = chr(letter)
        tds = scrape_words(driver, char_letter)
        vocabulaire = parse_words(tds, char_letter)
        write_words_to_file(vocabulaire, char_letter)

    driver.quit()
    print("Scraping process completed successfully.")

if __name__ == "__main__":
    main()
