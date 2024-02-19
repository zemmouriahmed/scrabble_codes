import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QMimeData


class DraggableTile(QLabel):
    def __init__(self, letter, value):
        super().__init__()
        self.letter = letter
        self.value = value
        self.setFixedSize(50, 50)
        self.setText(f"{letter}\n{value}")
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background-color: lightblue; border-radius: 10px;")
        self.setAcceptDrops(True)
        self.drag_start_position = None

    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return

        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(self.letter)
        drag.setMimeData(mime_data)

        drop_action = drag.exec_(Qt.MoveAction)

class MagneticArea(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 200)
        self.setStyleSheet("background-color: lightgrey; border: 2px dashed black;")
        self.tiles = []

    def add_tile(self, tile):
        if len(self.tiles) < 7:
            self.tiles.append(tile)
            self.update_layout()

    def update_layout(self):
        x, y = 10, 10
        for tile in self.tiles:
            tile.move(x, y)
            x += 60
            if x >= 250:
                x = 10
                y += 60

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        letter = event.mimeData().text()
        tile = DraggableTile(letter, 1)
        self.add_tile(tile)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Magnetic Tiles")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.magnetic_area = MagneticArea()
        self.layout.addWidget(self.magnetic_area)

        self.draw_button = QLabel("Draw Tiles")
        self.draw_button.setAlignment(Qt.AlignCenter)
        self.draw_button.setStyleSheet("background-color: lightgreen; border-radius: 10px;")
        self.draw_button.mousePressEvent = self.draw_tiles
        self.layout.addWidget(self.draw_button)

    def draw_tiles(self, event):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # Example letters
        random.shuffle(letters)
        for letter in letters:
            tile = DraggableTile(letter, 1)
            self.magnetic_area.add_tile(tile)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
