import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import Qt

# Distribution des lettres du jeu de Scrabble
letters_distribution = [
    # Ajoutez ici la distribution des lettres comme fournie précédemment
]

# Fonction pour créer le sac de lettres
def create_letter_bag(distribution):
    bag = []
    for item in distribution:
        for _ in range(item['quantity']):
            bag.append((item['letter'], item['value']))
    random.shuffle(bag)
    return bag

# Fonction pour distribuer ou compléter les lettres des joueurs
def distribute_letters(bag, player_hands, num_letters=7):
    for player_hand in player_hands.values():
        while len(player_hand) < num_letters and bag:
            player_hand.append(bag.pop())
    return player_hands, bag

class ScrabbleBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.letter_bag = create_letter_bag(letters_distribution)
        self.player_hands = {1: [], 2: [], 3: [], 4: []}  # Exemple pour 4 joueurs
        self.initUI()

    def initUI(self):
        # Initialiser l'interface utilisateur ici
        # Cette fonction doit inclure la logique pour la création du plateau de jeu et l'affichage des lettres des joueurs
        
        # Exemple de distribution initiale des lettres
        self.distribute_initial_letters()

    def distribute_initial_letters(self):
        # Distribuer initialement 7 lettres à chaque joueur
        global distribute_letters
        self.player_hands, self.letter_bag = distribute_letters(self.letter_bag, self.player_hands)

        # Mettre à jour l'affichage des lettres pour chaque joueur (à implémenter)

if __name__ == '__main__':
    app = QApplication([])
    scrabble = ScrabbleBoard()
    scrabble.show()
    app.exec_()
