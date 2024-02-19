import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QFrame
from PyQt5.QtCore import Qt, QMimeData, QPoint
from PyQt5.QtGui import QDrag, QPixmap

class ScrabbleTile(QLabel):
    def __init__(self, letter, value, parent=None):
        super().__init__(parent)
        self.letter = letter
        self.value = value
        self.setText(f"{letter}\n{value}")
        self.setFixedSize(50, 50)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background-color: lightblue; border: 1px solid black; border-radius: 10px;")
        self.setAttribute(Qt.WA_DeleteOnClose)

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
        
        if drag.exec_(Qt.MoveAction) == Qt.MoveAction:
            self.close()

class WordFormationArea(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("background-color: lightgray; border: 2px dashed black;")

        self.cell_width = 50
        self.cell_height = 50
        self.num_cells = 15

        # Ajustez la taille ici
        self.setFixedHeight(self.cell_height)
        self.setMinimumWidth(self.cell_width * self.num_cells)


    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        x_drop = event.pos().x()
        cell_index = min(self.num_cells - 1, max(0, x_drop // self.cell_width))
        if self.cells[cell_index] is None:  # Vérifie si la cellule est vide
            letter = event.mimeData().text()
            tile_label = ScrabbleTile(letter, '?', self)
            self.layout.addWidget(tile_label)
            tile_label.move(cell_index * self.cell_width, 0)
            self.cells[cell_index] = tile_label  # Marque la cellule comme occupée
            tile_label.show()
            event.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrabble Game")
        self.setGeometry(100, 100, 800, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        self.tiles_layout = QHBoxLayout()
        self.main_layout.addLayout(self.tiles_layout)

        self.word_formation_area = WordFormationArea()
        self.main_layout.addWidget(self.word_formation_area)

        self.draw_button = QPushButton("Draw Tiles")
        self.draw_button.clicked.connect(self.draw_tiles)
        self.main_layout.addWidget(self.draw_button)

    def draw_tiles(self):
        # Simplified tile drawing for demonstration
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        for _ in range(7):
            letter = random.choice(letters)
            tile = ScrabbleTile(letter, random.randint(1, 10))
            self.tiles_layout.addWidget(tile)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
