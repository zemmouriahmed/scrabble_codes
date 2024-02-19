import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import QMimeData, Qt, pyqtSignal
from PyQt5.QtGui import QDrag, QDragLeaveEvent
import random
import string

class PlayTile(QLabel):
    def __init__(self, letter, parent=None):
        super(PlayTile, self).__init__(parent)
        self.letter = letter
        self.setFixedSize(40, 40)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet('background-color: lightgrey; border: 1px solid black;')

    def setText(self, a0: str | None) -> None:
        self.letter = a0
        return super().setText(a0)
    
    def mouseMoveEvent(self, e):

        if e.buttons() != Qt.LeftButton:
            return

        mimeData = QMimeData()
        mimeData.setText(self.text())

        self.drag = QDrag(self)
        self.drag.setMimeData(mimeData)
        self.drag.setPixmap(self.grab())
        self.drag.setHotSpot(self.rect().center())

        dropAction = self.drag.exec_(Qt.MoveAction)
    # def 


class ClickableLabel(QLabel):
    clicked = pyqtSignal(int, int)
    COLORS = {'DL': 'lightblue', 'TL': 'orange', 'DW': 'lightgreen', 'TW': 'pink', "INPLAY": "yellow"}

    def __init__(self, row, col, celltype=None, parent=None):
        super(ClickableLabel, self).__init__(parent)
        self.row = row
        self.col = col
        self.type = celltype

        self.value = None
        self.mode = "EMPTY"

        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(40, 40)
        self.setFrameShape(QLabel.Panel)
        self.refreshTile()


    def refreshTile(self):
        if self.value is not None:
            self.setText(str(self.value))
            self.setAcceptDrops(False) 
            self.setStyleSheet('background-color: ' + ClickableLabel.COLORS.get(self.mode, "whitesmoke"))

        else:
            if self.type is not None:
                self.setText(str(self.type).upper())
            else:
                self.setText("")

            self.setStyleSheet('background-color: ' + ClickableLabel.COLORS.get(self.type, "whitesmoke"))
            self.setAcceptDrops(True) 

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.row, self.col)
        elif event.button() == Qt.RightButton:
            if self.value is not None:
                self.value = None
                self.mode = "EMPTY"
                self.refreshTile()

    def dragEnterEvent(self, e):
        # self.setStyleSheet("background: gray")
        e.accept()

    def dragLeaveEvent(self, e):
        pass
        # self.setStyleSheet("background: red")

    def dropEvent(self, e):
        # self.setStyleSheet("background: white")
        self.value = e.source().letter
        self.mode = "INPLAY"
        self.refreshTile()

class ScrabbleBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Scrabble Board with Letter Draw')
        self.setGeometry(100, 100, 800, 1000)  # Adjusted for additional components
        self.letters_drawn = []  # To store drawn letters
        self.create_scrabble_board()
        self.create_draw_zone()



    def create_scrabble_board(self):
         # Widget central pour le plateau de jeu
        game_board_widget = QWidget()
        game_board_widget.setFixedSize(800, 800)  # Fixe la taille du plateau de jeu
        layout = QGridLayout(game_board_widget)
        self.setCentralWidget(game_board_widget)

        double_lettre = [(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14),
                         (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2),
                         (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6),
                         (12, 8), (14, 3), (14, 11)]
        triple_lettre = [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1),
                         (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)]
        double_mot = [(1, 1), (1, 13), (2, 2), (2, 12), (3, 3), (3, 11), (4, 4),
                      (4, 10), (7, 7), (10, 4), (10, 10), (11, 3), (11, 11),
                      (12, 2), (12, 12), (13, 1), (13, 13)]
        triple_mot = [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7),
                      (14, 14)]

        for row in range(15):
            for col in range(15):
                
                if (row, col) in double_lettre:
                    label = ClickableLabel(row, col, 'DL')
                elif (row, col) in triple_lettre:
                    label = ClickableLabel(row, col, 'TL')
                elif (row, col) in double_mot:
                    label = ClickableLabel(row, col, 'DW')
                elif (row, col) in triple_mot:
                    label = ClickableLabel(row, col, 'TW')
                else:
                    label = ClickableLabel(row, col)
                
                label.clicked.connect(lambda rw=row, cl=col: self.on_label_click(rw, cl))
                layout.addWidget(label, row, col)

        game_board_widget.setLayout(layout)  # Applique le layout au game_board_widget

    def on_label_click(self, row, col):
        print(f"Case cliquée : {row}, {col}")


    def create_draw_zone(self):
        self.draw_zone = QWidget(self)
        self.draw_zone.setGeometry(50, 850, 700, 150)  # Positioning below the board
        draw_layout = QGridLayout(self.draw_zone)

        self.draw_button = QPushButton("Draw Letters", self.draw_zone)
        self.draw_button.clicked.connect(self.draw_letters)

        # self.word_input = QLineEdit(self.draw_zone)
        self.validate_button = QPushButton("Validate Word", self.draw_zone)
        self.validate_button.clicked.connect(self.validate_word) #fonc a revoir

        draw_layout.addWidget(self.draw_button, 0, 0)
        self.letter_labels = [PlayTile(" ", self.draw_zone) for _ in range(7)]  # Placeholder for letters
        for i, label in enumerate(self.letter_labels):
            draw_layout.addWidget(label, 0, i+1)
            
        draw_layout.addWidget(self.validate_button, 0, i+2)

    def draw_letters(self):
        self.letters_drawn = random.choices(string.ascii_uppercase, k=7)
        for i, letter in enumerate(self.letters_drawn):
            self.letter_labels[i].setText(letter)

    def validate_word(self):
        word = self.word_input.text().upper()
        if word in ["DUMMY_DICTIONARY"]:  # Replace with actual dictionary check
            QMessageBox.information(self, "Word Validation", f"'{word}' is a valid word!")
        else:
            QMessageBox.warning(self, "Word Validation", f"'{word}' is not a valid word.")

def main():
    app = QApplication(sys.argv)
    scrabble_board = ScrabbleBoard()
    scrabble_board.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
