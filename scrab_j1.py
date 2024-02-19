import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

# Represents individual Scrabble tiles that can be dragged.
class DraggableTile(QLabel):
    def __init__(self, letter="", value=0, parent=None):
        super().__init__(parent)
        self.setText(letter)
        self.value = value
        self.setFixedSize(40, 40)
        self.setStyleSheet("border: 1px solid black;")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            drag = QDrag(self)
            mimeData = QMimeData()
            mimeData.setText(self.text())
            drag.setMimeData(mimeData)
            drag.exec_(Qt.MoveAction)

# Represents the spaces on the Scrabble board.
class BoardTile(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setFixedSize(40, 40)
        self.setStyleSheet("border: 1px solid black; background-color: lightgrey;")

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        self.setText(event.mimeData().text())
        event.accept()

# Main window for the Scrabble game.
class ScrabbleGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrabble Game")
        self.setGeometry(100, 100, 800, 600)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QGridLayout(self.centralWidget)

        self.initBoard()
        self.initTiles()

    def initBoard(self):
        for row in range(15):
            for col in range(15):
                tile = BoardTile(self)
                self.layout.addWidget(tile, row, col)

    def initTiles(self):
        for i in range(7):  # Example with 7 tiles
            letter = chr(65 + i)  # Example letters A-G
            tile = DraggableTile(letter, 1)  # Example value 1 for each tile
            self.layout.addWidget(tile, 16, i)  # Adding tiles below the board

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScrabbleGame()
    window.show()
    sys.exit(app.exec_())
