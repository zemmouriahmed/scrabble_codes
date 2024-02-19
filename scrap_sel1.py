from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time
from tqdm import tqdm

def setup_driver():
    driver_options = Options()
    driver_options.add_argument("--headless")  # Pour le débogage, vous pouvez temporairement enlever cette ligne
    driver_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
    driver = webdriver.Edge(options=driver_options)
    return driver

def create_directory(directory_name):
    if not os.path.isdir(directory_name):
        os.mkdir(directory_name)

def scrape_words(driver, letter):
    try:
        url = f'https://www.motscroises.fr/dictionnaire-scrabble.fr/mot-commencant-par-{letter}/'
        driver.get(url)
        wait = WebDriverWait(driver, 20)
        word_css_selector = '.letter-bloc.open td'
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, word_css_selector)))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        tds = soup.select(word_css_selector)
        return [td.text.strip() for td in tds]
    except Exception as e:
        print(f"Erreur lors du scraping pour la lettre {letter}: {e}")
        return []

def write_words_to_file(vocabulaire, letter, directory='scrabble_vocabularies1'):
    with open(f'{directory}/{letter}.txt', 'w', encoding='utf-8') as f:
        for mot in vocabulaire:
            f.write(f"{mot}\n")

def main():
    driver = setup_driver()
    create_directory('scrabble_vocabularies1')

    for letter in tqdm('abcdefghijklmnopqrstuvwxyz', desc='Progression'):
        vocabulaire = scrape_words(driver, letter)
        if vocabulaire:
            write_words_to_file(vocabulaire, letter)
            print(f"Mots pour la lettre {letter} sauvegardés.")
        time.sleep(1)  # Délai pour éviter le blocage et la surcharge du serveur

    driver.quit()

if __name__ == "__main__":
    main()
