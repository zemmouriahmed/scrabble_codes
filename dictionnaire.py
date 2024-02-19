from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def telecharger_dictionnaire_selenium(url):
    chrome_options = Options()
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get(url)
        time.sleep(5)  # Laissez le temps à la page de charger complètement

        # Ajustez selon la structure réelle de la page
        elements = driver.find_elements(By.TAG_NAME, 'li')
        mots = [element.text for element in elements if element.text != '']

        return mots
    finally:
        driver.quit()

# Exemple d'utilisation
url_dictionnaire = "https://aide-scrabble.fr/dictionnaire/"  # Assurez-vous que l'URL est correcte
liste_mots = telecharger_dictionnaire_selenium(url_dictionnaire)

if liste_mots:
    print(f"Nombre de mots dans le dictionnaire: {len(liste_mots)}")
else:
    print("Impossible de télécharger le dictionnaire.")
