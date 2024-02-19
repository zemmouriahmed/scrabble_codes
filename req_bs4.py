import requests
from bs4 import BeautifulSoup

# URL de la page à scraper
url = 'https://www.motscroises.fr/dictionnaire-scrabble/mot-commencant-par-{letter}/'

# Utilisation de requests pour télécharger le contenu de la page
response = requests.get(url)

# Vérification que la requête a réussi
if response.status_code == 200:
    # Utilisation de BeautifulSoup pour analyser le contenu HTML récupéré
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Exemple d'extraction de toutes les instances d'une balise spécifique
    # Remplacer 'balise' par la balise réelle que vous recherchez, comme 'a' pour les liens
    for element in soup.find_all('balise'):
        print(element.text)  # Imprime le texte de chaque élément trouvé
else:
    print(f"Erreur lors de la récupération de la page : {response.status_code}")
