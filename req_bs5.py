import requests
from bs4 import BeautifulSoup

# Fonction pour scraper les mots commençant par une lettre spécifique
def scrape_words(letter):
    # Format de l'URL avec la lettre actuelle
    url = f'https://www.motscroises.fr/dictionnaire-scrabble.fr/mot-commencant-par-{letter}/'
    
    # Utilisation de requests pour télécharger le contenu de la page
    response = requests.get(url)
    
    # Vérification que la requête a réussi
    if response.status_code == 200:
        # Utilisation de BeautifulSoup pour analyser le contenu HTML récupéré
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remplacez 'balise' par la balise réelle que vous recherchez
        # Par exemple, si vous cherchez des mots dans des éléments <td>, remplacez 'balise' par 'td'
        for element in soup.find_all('balise'):
            print(element.text)  # Imprime le texte de chaque élément trouvé
    else:
        print(f"Erreur lors de la récupération de la page pour la lettre {letter} : {response.status_code}")

# Boucle sur chaque lettre de l'alphabet
for letter in 'abcdefghijklmnopqrstuvwxyz':
    scrape_words(letter)
