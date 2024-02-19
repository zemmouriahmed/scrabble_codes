import sys
import random

from PyQt5 import QtCore, QtWidgets,QtGui

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

class ScrabbleTileLabel(QtWidgets.QLabel):
    def __init__(self, parent, letter, value):
        super().__init__(parent)
        self.letter = letter
        self.value = value
        self.setFixedSize(50, 50)
        self.setText(f"{letter}\n{value}")
        self.setAlignment(QtCore.Qt.AlignCenter)  # Centrer le texte
        self.setStyleSheet("background-color: lightblue; border-radius: 10px;")
        # Activer le glisser-déposer
        self.setAcceptDrops(True)

    def mousePressEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            self.drag_start_position = event.pos()

def mouseMoveEvent(self, event):
    if not (event.buttons() & QtCore.Qt.LeftButton):
        return
    if (event.pos() - self.drag_start_position).manhattanLength() < QtWidgets.QApplication.startDragDistance():
        return

    drag = QtGui.QDrag(self)  # Utilisez QtGui au lieu de QtWidgets pour QDrag
    mime_data = QtCore.QMimeData()
    mime_data.setText(self.letter)
    drag.setMimeData(mime_data)

    drop_action = drag.exec_(QtCore.Qt.MoveAction)


    def mouseReleaseEvent(self, event):
        pass  # Vous pouvez ajouter un traitement ici si nécessaire

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrabble Tile Draw")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QtWidgets.QVBoxLayout(self.central_widget)
        

        self.draw_button = QtWidgets.QPushButton("Draw Tiles", self)
        self.draw_button.clicked.connect(self.draw_tiles)
        self.layout.addWidget(self.draw_button)

        self.tiles_widget = QtWidgets.QWidget()
        self.tiles_layout = QtWidgets.QVBoxLayout(self.tiles_widget)
        self.tiles_widget.setLayout(self.tiles_layout)
        self.layout.addWidget(self.tiles_widget)

        self.dragged_tile = None  # Pour stocker la tuile en cours de déplacement


    def draw_tiles(self):
        scrabble_bag = ScrabbleBag()
        drawn_tiles = scrabble_bag.draw_tiles(7)

        # Afficher les tuiles sous forme de boutons carrés dans le layout des tuiles
        for tile in drawn_tiles:
            tile_label = ScrabbleTileLabel(self.tiles_widget, tile.letter, tile.value)
            self.tiles_layout.addWidget(tile_label)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        if event.mimeData().hasText():
            letter = event.mimeData().text()
            tile_label = ScrabbleTileLabel(self.tiles_widget, letter, 1)
            self.tiles_layout.addWidget(tile_label)

    def check_word(self):
        # Vérifiez si l'ordre des tuiles forme un mot valide dans votre dictionnaire
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
