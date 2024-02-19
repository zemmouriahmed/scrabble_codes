import requests
from bs4 import BeautifulSoup

# Fonction pour extraire les mots d'une page spécifique du dictionnaire
def extraire_mots(url):
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'html.parser')
    
    # Mise à jour du sélecteur pour cibler les balises <td> dans la structure spécifiée
    # L'exemple ci-dessous suppose que vous avez la structure HTML exacte mentionnée précédemment
    # et que vous cherchez à extraire le texte directement depuis les éléments <td>
    selecteur = 'div.letter-bloc.open'  # Ajustez 'identifiant_ul' au vrai ID
    elements_cibles = soup.select(selecteur)
    liste_mots = [element.text.strip() for element in elements_cibles]  # .strip() pour enlever les espaces superflus
    
    return liste_mots

# Itérer sur chaque lettre de l'alphabet pour récupérer les mots
dictionnaire_complet = []
for lettre in 'abcdefghijklmnopqrstuvwxyz':
    url = f'https://www.aide-scrabble.fr/dictionnaire/{lettre}/'
    mots = extraire_mots(url)
    dictionnaire_complet.extend(mots)
    print(f"Mots extraits pour la lettre {lettre}: {len(mots)}")

# Ici, `dictionnaire_complet` contient tous les mots extraits
# Vous pouvez ensuite les sauvegarder dans un fichier ou les utiliser directement dans votre jeu
