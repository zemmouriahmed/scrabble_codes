import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QPixmap

class ScrabbleTile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

class ScrabbleBag:
    def __init__(self):
        self.tiles = []
        self.create_tiles()

    def create_tiles(self):
        letter_distribution = {
            'A': {'count': 9, 'value': 1}, 'B': {'count': 2, 'value': 3},
            # Ajoutez ici le reste des lettres selon leur distribution et valeur
            'Z': {'count': 1, 'value': 10},
        }
        for letter, info in letter_distribution.items():
            for _ in range(info['count']):
                self.tiles.append(ScrabbleTile(letter, info['value']))

    def draw_tiles(self, num_tiles):
        drawn_tiles = random.sample(self.tiles, min(num_tiles, len(self.tiles)))
        for tile in drawn_tiles:
            self.tiles.remove(tile)
        return drawn_tiles

class ScrabbleTileLabel(QLabel):
    def __init__(self, letter, value):
        super().__init__()
        self.letter = letter
        self.value = value
        self.setText(f"{letter}\n{value}")
        self.setFixedSize(50, 50)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background-color: lightblue; border: 1px solid black; border-radius: 10px;")
        self.setAcceptDrops(False)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.letter)
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        self.render(pixmap)
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos() - self.rect().topLeft())
        drag.exec_(Qt.MoveAction)

class WordFormationArea(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        letter = event.mimeData().text()
        tile_label = ScrabbleTileLabel(letter, '?')
        self.layout.addWidget(tile_label)
        event.accept()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrabble Game")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        self.draw_button = QPushButton("Draw Tiles")
        self.draw_button.clicked.connect(self.draw_tiles)
        self.main_layout.addWidget(self.draw_button)

        self.tiles_layout = QHBoxLayout()
        self.main_layout.addLayout(self.tiles_layout)

        self.word_formation_area = WordFormationArea()
        self.main_layout.addWidget(self.word_formation_area)

    def draw_tiles(self):
        for i in reversed(range(self.tiles_layout.count())): 
            self.tiles_layout.itemAt(i).widget().setParent(None)
            
        scrabble_bag = ScrabbleBag()
        drawn_tiles = scrabble_bag.draw_tiles(7)
        for tile in drawn_tiles:
            tile_label = ScrabbleTileLabel(tile.letter, tile.value)
            self.tiles_layout.addWidget(tile_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
