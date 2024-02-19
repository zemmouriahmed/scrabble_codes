import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QComboBox, QGridLayout
from PyQt5.QtCore import Qt

from draw_tiles import ScrabbleBag

class ScrabbleTileButton(QPushButton):
    def __init__(self, letter, value):
        super().__init__()
        self.letter = letter
        self.value = value
        self.setFixedSize(50, 50)
        self.setText(f"{letter}\n{value}")
        self.setStyleSheet("background-color: lightblue; border-radius: 10px;")

class ScrabbleBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Scrabble Board')
        self.setGeometry(100, 100, 600, 600)

        self.tiles_widget = QWidget()
        self.tiles_layout = QGridLayout(self.tiles_widget)  # Utilisez QGridLayout pour organiser les widgets
        self.setCentralWidget(self.tiles_widget)

        self.scrabble_board = [[None for _ in range(15)] for _ in range(15)]
        self.scrabble_bag = ScrabbleBag()

        self.available_tiles_combo = QComboBox()
        self.available_tiles_combo.currentIndexChanged.connect(self.on_tile_selected)
        self.tiles_layout.addWidget(self.available_tiles_combo, 0, 0)  # Ajoutez la combo box à la grille

        self.draw_tiles()
        self.create_scrabble_board()

    def create_scrabble_board(self):
        for row in range(15):
            for col in range(15):
                label = QLabel()
                label.setFixedSize(40, 40)
                label.setAlignment(Qt.AlignCenter)
                label.setFrameShape(QLabel.Panel)
                label.setStyleSheet('background-color: lightgrey')
                label.mousePressEvent = lambda event, r=row, c=col: self.on_tile_clicked(r, c)
                self.tiles_layout.addWidget(label, row + 1, col + 1)  # Ajoutez le label à la grille

    def on_tile_clicked(self, row, col):
        if self.scrabble_board[row][col] is None:
            selected_tile_index = self.available_tiles_combo.currentIndex()
            selected_tile_data = self.available_tiles_combo.itemData(selected_tile_index)
            if selected_tile_data is not None:
                selected_tile = selected_tile_data['tile']
                tile_button = ScrabbleTileButton(selected_tile.letter, selected_tile.value)
                self.scrabble_board[row][col] = tile_button
                self.tiles_layout.itemAtPosition(row + 1, col + 1).widget().deleteLater()
                self.tiles_layout.addWidget(tile_button, row + 1, col + 1)
                self.update()

    def on_tile_selected(self, index):
        pass

    def add_available_tile(self, tile):
        self.available_tiles_combo.addItem(f"{tile.letter} - {tile.value}", userData={'tile': tile})

    def draw_tiles(self):
        drawn_tiles = self.scrabble_bag.draw_tiles(7)
        for tile in drawn_tiles:
            self.add_available_tile(tile)

def main():
    app = QApplication(sys.argv)
    scrabble_board = ScrabbleBoard()
    scrabble_board.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
