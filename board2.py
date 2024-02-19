import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout
from PyQt5.QtCore import Qt, pyqtSignal

class ClickableLabel(QLabel):
    clicked = pyqtSignal(int, int)

    def __init__(self, row, col, parent=None):
        super(ClickableLabel, self).__init__(parent)
        self.row = row
        self.col = col
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(40, 40)
        self.setFrameShape(QLabel.Panel)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.row, self.col)

class ScrabbleBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Scrabble Board')
        self.setGeometry(100, 100, 600, 600)
        self.create_scrabble_board()

    def create_scrabble_board(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout()

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
        colors = {'DL': 'lightblue', 'TL': 'orange', 'DW': 'lightgreen', 'TW': 'pink'}

        for row in range(15):
            for col in range(15):
                label = ClickableLabel(row, col)
                if (row, col) in double_lettre:
                    label.setText('DL')
                    label.setStyleSheet('background-color: ' + colors['DL'])
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
                    label.setStyleSheet('background-color: lightgrey')
                
                label.clicked.connect(lambda rw=row, cl=col: self.on_label_click(rw, cl))
                layout.addWidget(label, row, col)

        central_widget.setLayout(layout)

    def on_label_click(self, row, col):
        print(f"Case cliquée : {row}, {col}")

def main():
    app = QApplication(sys.argv)
    scrabble_board = ScrabbleBoard()
    scrabble_board.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
