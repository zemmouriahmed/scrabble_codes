from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def scrape_site():
    # Options pour exécuter Chrome en mode headless
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    # Remplacer 'path/to/your/chromedriver' par le chemin vers votre ChromeDriver
    driver_service = Service(executable_path='C:\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service, options=options)

    try:
        driver.get('https://www.motscroises.fr/dictionnaire-scrabble.fr/')
        # Remplacer 'VotreSelecteurCSS' par le sélecteur CSS correct pour les éléments que vous voulez extraire
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'container')))
        
        elements = driver.find_elements(By.CSS_SELECTOR, 'container')
        for element in elements:
            print(element.text)  # Affiche le texte de chaque élément trouvé
    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_site()
