from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import os
from tqdm import tqdm
import pandas as pd

def setup_driver(headless=True):
    driver_options = Options()
    if headless:
        driver_options.add_argument("--headless")  # Commentez ou modifiez cette ligne pour voir le navigateur
    driver = webdriver.Edge(options=driver_options)
    print("Driver set up successfully.")
    return driver

def create_directory(directory_name):
    if not os.path.isdir(directory_name):
        os.mkdir(directory_name)
    print(f"Directory '{directory_name}' is ready for use.")

def scrape_words(driver, letter):
    url = f'https://aide-scrabble.fr/mot-commencant-par-{letter}/'
    driver.get(url)
    wait = WebDriverWait(driver, 100)
    word_css_selector = '.letter-bloc.open td'
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, word_css_selector)))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    tds = soup.select(word_css_selector)
    print(f"Scraped words for letter '{letter}'.")
    return tds

def parse_words(tds, letter):
    vocabulaire = []
    for td in tds:
        nbr_points = td.select_one('i').text
        mot = td.text.replace(nbr_points.strip(), '').strip()
        vocabulaire.append(mot)
    print(f"Parsed words for letter '{letter}'.")
    return vocabulaire

def write_words_to_file(vocabulaire, letter, directory='scrabble_vocabularies'):
    with open(f'{directory}/{letter}.txt', 'w') as f:
        for mot in vocabulaire:
            f.write(f"{mot}\n")
    print(f"Words for letter '{letter}' written to file.")

def main():
    driver = setup_driver(headless=False)  # Changez headless=False pour voir l'exécution dans le navigateur
    create_directory('scrabble_vocabularies2')

    for letter in tqdm(range(97, 123), desc='Overall Progress'):
        char_letter = chr(letter)
        try:
            tds = scrape_words(driver, char_letter)
            vocabulaire = parse_words(tds, char_letter)
            write_words_to_file(vocabulaire, char_letter)
        except Exception as e:
            print(f"An error occurred for letter {char_letter}: {e}")

    driver.quit()
    print("Scraping process completed successfully.")

if __name__ == "__main__":
    main()
