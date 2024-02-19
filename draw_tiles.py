import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QPoint, QRect

class ScrabbleTile:
    def __init__(self, letter, value):
        self.letter = letter  # Lettre de la tuile
        self.value = value    # Valeur de la tuile en points

class ScrabbleBag:
    def __init__(self):
        self.tiles = []  # Liste pour stocker les tuiles de Scrabble dans le sac
        self.create_tiles()  # Appel de la méthode pour créer les tuiles

    def create_tiles(self):
        # Définition des tuiles pour chaque lettre avec leur valeur associée
        letter_distribution = {
            'A': {'count': 9, 'value': 1},
            'B': {'count': 2, 'value': 3},
            'C': {'count': 2, 'value': 3},
            'D': {'count': 4, 'value': 2},
            'E': {'count': 12, 'value': 1},
            'F': {'count': 2, 'value': 4},
            'G': {'count': 3, 'value': 2},
            'H': {'count': 2, 'value': 4},
            'I': {'count': 9, 'value': 1},
            'J': {'count': 1, 'value': 8},
            'K': {'count': 1, 'value': 5},
            'L': {'count': 4, 'value': 1},
            'M': {'count': 2, 'value': 3},
            'N': {'count': 6, 'value': 1},
            'O': {'count': 8, 'value': 1},
            'P': {'count': 2, 'value': 3},
            'Q': {'count': 1, 'value': 10},
            'R': {'count': 6, 'value': 1},
            'S': {'count': 4, 'value': 1},
            'T': {'count': 6, 'value': 1},
            'U': {'count': 4, 'value': 1},
            'V': {'count': 2, 'value': 4},
            'W': {'count': 2, 'value': 4},
            'X': {'count': 1, 'value': 8},
            'Y': {'count': 2, 'value': 4},
            'Z': {'count': 1, 'value': 10},
            '_': {'count': 2, 'value': 0}  # Joker avec une valeur de 0
        }

        # Création des tuiles en fonction de la distribution de lettres
        for letter, info in letter_distribution.items():
            for _ in range(info['count']):
                self.tiles.append(ScrabbleTile(letter, info['value']))

    def draw_tiles(self, num_tiles):
        # Sélection aléatoire d'un certain nombre de tuiles depuis le sac
        drawn_tiles = random.sample(self.tiles, num_tiles)
        
        # Retrait des tuiles sélectionnées du sac
        for tile in drawn_tiles:
            self.tiles.remove(tile)
        
        return drawn_tiles

class ScrabbleTileLabel(QLabel):
    def __init__(self, parent, letter, value):
        super().__init__(parent)
        self.letter = letter
        self.value = value
        self.setFixedSize(50, 50)
        self.setText(f"{letter}\n{value}")
        self.setAlignment(Qt.AlignCenter)  # Centrer le texte
        self.setStyleSheet("background-color: lightblue; border-radius: 10px;")

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            new_pos = self.pos() + event.pos() - self.offset
            self.move(new_pos)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrabble Tile Draw")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.draw_button = QPushButton("Draw Tiles", self)
        self.draw_button.clicked.connect(self.draw_tiles)
        self.layout.addWidget(self.draw_button)

        self.tiles_widget = QWidget()
        self.tiles_layout = QVBoxLayout()
        self.tiles_widget.setLayout(self.tiles_layout)
        self.layout.addWidget(self.tiles_widget)

    def draw_tiles(self):
        scrabble_bag = ScrabbleBag()
        drawn_tiles = scrabble_bag.draw_tiles(7)

        # Afficher les tuiles sous forme de boutons carrés dans le layout des tuiles
        for tile in drawn_tiles:
            tile_label = ScrabbleTileLabel(self.tiles_widget, tile.letter, tile.value)
            self.tiles_layout.addWidget(tile_label)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
