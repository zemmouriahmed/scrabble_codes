import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt

class ScrabbleBoard(QMainWindow):
    def __init__(self):
        super().__init__()  # Appel du constructeur de la classe parente QMainWindow

        # Configuration de la fenêtre principale
        self.setWindowTitle('Scrabble Board')  # Titre de la fenêtre
        self.setGeometry(100, 100, 600, 600)   # Position et taille de la fenêtre

        # Création de l'échiquier de Scrabble
        self.create_scrabble_board()           # Appel de la méthode pour créer l'échiquier

        self.show()                            # Afficher la fenêtre principale

    def create_scrabble_board(self):
        central_widget = QWidget()             # Création d'un widget central
        self.setCentralWidget(central_widget)  # Définir ce widget comme widget central de la fenêtre

        layout = QGridLayout()                 # Création d'une grille pour organiser les éléments

        # Placer les cases à double et triple lettres
        double_lettre = [(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14),
                         (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2),
                         (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6),
                         (12, 8), (14, 3), (14, 11)]
        triple_lettre = [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1),
                         (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)]

        # Placer les cases à double et triple mots
        double_mot = [(1, 1), (1, 13), (2, 2), (2, 12), (3, 3), (3, 11), (4, 4),
                      (4, 10), (7, 7), (10, 4), (10, 10), (11, 3), (11, 11),
                      (12, 2), (12, 12), (13, 1), (13, 13)]
        triple_mot = [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7),
                      (14, 14)]

        colors = {'DL': 'lightblue', 'TL': 'orange', 'DW': 'lightgreen', 'TW': 'pink'}  # Dictionnaire de couleurs pour les cases spéciales

        for row in range(15):
            for col in range(15):
                label = QLabel()               # Création d'un QLabel pour chaque case
                label.setFixedSize(40, 40)    # Taille de chaque case
                label.setAlignment(Qt.AlignCenter)  # Alignement du texte au centre
                label.setFrameShape(QLabel.Panel)   # Ajouter une bordure autour de chaque case

                # Marquer les cases spéciales avec les lettres DW, DL, TW, TL
                if (row, col) in double_lettre:
                    label.setText('DL')
                    label.setStyleSheet('background-color: ' + colors['DL'])  # Appliquer la couleur de fond correspondante
                elif (row, col) in triple_lettre:
                    label.setText('TL')
                    label.setStyleSheet('background-color: ' + colors['TL'])
                elif (row, col) in double_mot:
                    label.setText('DW')
                    label.setStyleSheet('background-color: ' + colors['DW'])
                elif (row, col) in triple_mot:
                    label.setText('TW')
                    label.setStyleSheet('background-color: ' + colors['TW'])
                else:
                    label.setStyleSheet('background-color: lightgrey')  # Couleur de fond pour les cases non spéciales
                
                layout.addWidget(label, row, col)  # Ajouter le QLabel à la grille à la position (row, col)

        central_widget.setLayout(layout)  # Appliquer la grille au widget central

def main():
    app = QApplication(sys.argv)         # Création d'une application Qt
    scrabble_board = ScrabbleBoard()      # Création de l'instance ScrabbleBoard
    sys.exit(app.exec_())                 # Lancement de l'application Qt

if __name__ == '__main__':
    main()
