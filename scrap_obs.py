from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import os
from tqdm import tqdm
from selenium.common.exceptions import TimeoutException

def setup_driver():
    driver_options = Options()
    # driver_options.add_argument("--headless")  # Exécute Edge en mode sans tête
    driver = webdriver.Edge(options=driver_options)
    return driver

def create_directory(directory_name):
    os.makedirs(directory_name, exist_ok=True)

def scrape_words(driver, letter):
    # Supposons que l'URL doit être ajustée pour chaque lettre
    url = f'https://www.aide-scrabble.fr/mot-commencant-par-{letter}/'
    driver.get(url)
    
    
    # Ajustez ce sélecteur CSS pour correspondre à la structure de la page
    # Ce sélecteur est un exemple et doit être modifié pour correspondre aux éléments réels
    word_css_selector = '.word-list li'  # Sélecteur hypothétique pour les mots
    
    try:
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, word_css_selector)))
    except Exception as e:
        print(f"Timed out waiting for page elements to load for letter '{letter}': {e}")
        return []

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    words_elements = soup.select(word_css_selector)
    return [element.text.strip() for element in words_elements]

def write_words_to_file(words, letter, directory='scrabble_vocabularies_final5'):
    file_path = os.path.join(directory, f'{letter}.txt')
    with open(file_path, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(f"{word}\n")

def main():
    driver = setup_driver()
    directory_name = 'scrabble_vocabularies_final5'
    create_directory(directory_name)

    for letter in tqdm(range(97, 123), desc='Overall Progress'):  # de 'a' à 'z'
        char_letter = chr(letter)
        try:
            words = scrape_words(driver, char_letter)
            write_words_to_file(words, char_letter, directory_name)
        except Exception as e:
            print(f"An error occurred for letter {char_letter}: {e}")

    driver.quit()

if __name__ == "__main__":
    main()
