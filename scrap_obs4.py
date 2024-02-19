from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import tqdm.notebook as tqdm
from bs4 import BeautifulSoup
import glob
import os
from collections import Counter
import pandas as pd

driver_options = webdriver.EdgeOptions()
driver = webdriver.ChromiumEdge(driver_options)

if not os.path.isdir('scrabble_vocabularies3'):
    os.mkdir('scrabble_vocabularies3')
with tqdm.trange(97, 123) as pbar:
    for i in pbar:
        letter = chr(i)
        url = f'https://aide-scrabble.fr/mot-commencant-par-{letter}/'
        pbar.set_description('Sending request')
        driver.get(url)
        wait = WebDriverWait(driver, 25)
        word_css_selector = '.letter-bloc.open td'
        wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, word_css_selector)
        ))
        
        soup = BeautifulSoup(driver.page_source, 'html')
        tds = soup.select(word_css_selector)
        
        vocabulaire = []
        pbar.set_description('Parsing words')
        for td in tqdm.tqdm(tds, position=1, leave=False, desc=f'Words starting with {letter.upper()}'):
            nbr_points = td.select_one('i').text
            td_text = td.text
            mot = td_text.replace(nbr_points.strip(), '')
            vocabulaire.append(mot)
        pbar.set_description('Writing words to disc')
        with open(f'scrabble_vocabularies3/{letter}.txt', 'w') as f:
            f.writelines(vocabulaire)


driver.close()