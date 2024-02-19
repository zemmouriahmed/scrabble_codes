from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import os
from tqdm import tqdm  # Utilisation de tqdm pour une compatibilité générale
import pandas as pd

def setup_driver():
    driver_options = Options()
    driver_options.add_argument("--headless")  # Option pour exécuter Edge en mode sans tête
    driver = webdriver.Edge(options=driver_options)
    return driver

def create_directory(directory_name):
    if not os.path.isdir(directory_name):
        os.mkdir(directory_name)

def scrape_words(driver, letter):
    url = f'https://www.motscroises.fr/dictionnaire-scrabble.fr/mot-commencant-par-{letter}/'
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    word_css_selector = '.letter-bloc.open td'
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, word_css_selector)))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    tds = soup.select(word_css_selector)
    return tds

def parse_words(tds, letter):
    vocabulaire = []
    for td in tds:
        nbr_points = td.select_one('i').text
        mot = td.text.replace(nbr_points.strip(), '').strip()
        vocabulaire.append(mot)
    return vocabulaire

def write_words_to_file(vocabulaire, letter):
    with open(f'scrabble_vocabularies1/{letter}.txt', 'w') as f:
        for mot in vocabulaire:
            f.write(f"{mot}\n")

def main():
    driver = setup_driver()
    create_directory('scrabble_vocabularies1')

    for letter in tqdm(range(97, 123), desc='Overall Progress'):
        char_letter = chr(letter)
        try:
            tds = scrape_words(driver, char_letter)
            vocabulaire = parse_words(tds, char_letter)
            write_words_to_file(vocabulaire, char_letter)
            print(f"Letter {char_letter}: {len(vocabulaire)} words found.")  # Affiche le nombre de mots récupérés
        except Exception as e:
            print(f"An error occurred for letter {char_letter}: {e}")

    driver.quit()

if __name__ == "__main__":
    main(