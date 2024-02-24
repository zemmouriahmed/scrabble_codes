import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QMessageBox, QLineEdit
from PyQt5.QtCore import QMimeData, Qt, pyqtSignal
from PyQt5.QtGui import QDrag, QDragLeaveEvent
import random
import string
import os

class PlayTile(QLabel):
    tileMoved = pyqtSignal(str)
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

        if dropAction == self.drag.exec_(Qt.MoveAction):
            self.tileMoved.emit(self.letter)
    


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
        self.letters_bag = self.initialize_letter_bag()
        self.letters_drawn = []  # To store drawn letters
        self.create_scrabble_board()
        self.create_draw_zone()
        self.isTurnInProgress = False  # Ajoutez cet attribut
        # Chargez le dictionnaire
        dictionary_path = r"C:\Users\eptec\Desktop\dictionnaire_compilé"
        self.load_dictionary_from_folder(r"C:\Users\eptec\Desktop\dictionnaire_compilé")
    def load_dictionary_from_folder(self, folder_path):
        self.dictionary = set()
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                filepath = os.path.join(folder_path, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    for line in file:
                        self.dictionary.add(line.strip().upper())



    def initialize_letter_bag(self):
        # Initialisation du sac de lettres à partir de la définition des lettres
        letters = [
           
        {'letter':'A', 'quantity': 9, 'value': 1},
        {'letter':'B', 'quantity': 2, 'value': 3},
        {'letter':'C', 'quantity': 2, 'value': 3},
        {'letter':'D', 'quantity': 4, 'value': 2},
        {'letter':'E', 'quantity': 12, 'value': 1},
        {'letter':'F', 'quantity': 2, 'value': 4},
        {'letter':'G', 'quantity': 3, 'value': 2},
        {'letter':'H', 'quantity': 2,'value': 4},
        {'letter':'I', 'quantity': 9, 'value': 1},
        {'letter':'J','quantity': 1, 'value': 8},
        {'letter':'K', 'quantity': 1, 'value': 5},
        {'letter':'L', 'quantity': 4,'value': 1},
        {'letter':'M','quantity': 2, 'value': 3},
        {'letter':'N', 'quantity':6, 'value': 1},
        {'letter':'O','quantity': 8, 'value': 1},
        {'letter':'P','quantity':2, 'value': 3},
        {'letter':'Q','quantity': 1, 'value': 10},
        {'letter':'R','quantity': 6, 'value': 1},
        {'letter':'S','quantity': 4, 'value': 1},
        {'letter':'T', 'quantity': 6, 'value': 1},
        {'letter':'U','quantity': 4, 'value': 1},
        {'letter':'V','quantity': 2, 'value': 4},
        {'letter':'W','quantity': 2, 'value': 4},
        {'letter':'X','quantity': 1, 'value': 8},
        {'letter':'Y','quantity': 2, 'value': 4},
        {'letter':'Z','quantity': 1, 'value': 10},
        {'letter':'?', 'quantity':2, 'value': 0}  # Joker avec une valeur de 0
        
        ]
        bag = []
        for letter_info in letters:
            for _ in range(letter_info['quantity']):
                bag.append({'letter': letter_info['letter'], 'value': letter_info['value']})
        random.shuffle(bag)  # Mélanger le sac de lettres
        return bag


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
        self.draw_zone.setFixedSize(700, 150)
        self.draw_layout = QGridLayout(self.draw_zone)

        self.draw_button = QPushButton("Draw Letters", self.draw_zone)
        self.draw_button.setFixedSize(100, 40)
        self.validate_button = QPushButton("Validate Word",self.draw_zone)
        self.validate_button.setFixedSize(100, 40)
        self.draw_button.clicked.connect(self.draw_letters)

    #   self.word_input = QLineEdit(self.draw_zone)  # Créez le QLineEdit pour la saisie des mots
    #   self.word_input.setPlaceholderText("Entrez un mot ici")  # Texte indicatif
    #   self.draw_layout.addWidget(self.word_input, 1, 0, 1, 8)  # Ajoutez le QLineEdit au layout

        self.draw_layout.addWidget(self.draw_button, 0, 0)
        self.draw_button.setFixedSize(100, 40)
        self.letter_labels = [PlayTile(" ", self.draw_zone) for _ in range(7)]  # Placeholder for letters
        for i, label in enumerate(self.letter_labels):
            label.tileMoved.connect(self.handleTileMoved)
            self.draw_layout.addWidget(label, 0, i+1)
            
        self.draw_layout.addWidget(self.validate_button, 0, i+2)





    def draw_letters(self):
        if not self.isTurnInProgress and len(self.letters_bag) >= 7:  # Assurer qu'il y a assez de lettres
            drawn_letters = []
            for _ in range(7):  # Tirer 7 lettres
                if len(self.letters_bag) == 0:  # Vérifier si le sac est vide
                    break  # Sortir de la boucle si plus de lettres disponibles
                letter_info = self.letters_bag.pop(0)  # Tirer la première lettre disponible
                drawn_letters.append(letter_info)
                self.letters_drawn.append(letter_info['letter'])  # Stocker les lettres tirées
        
        # Mettre à jour l'affichage des lettres tirées
            for i, letter_info in enumerate(drawn_letters):
                self.letter_labels[i].setText(letter_info['letter'])
            # Vous pouvez également stocker la valeur de la lettre pour un usage ultérieur
        
            self.draw_button.setEnabled(False)  # Désactiver le bouton de tirage
            self.isTurnInProgress = True  # Marquer le début d'un tour
        else:
            QMessageBox.warning(self, "Attention", "Le tour est en cours ou il n'y a pas assez de lettres.")

    def validate_word(self):
        word = self.word_input.text().upper()
        if word in self.dictionary:  # Replace with actual dictionary check
            QMessageBox.information(self, "Word Validation", f"'{word}' is a valid word!")
            self.word_input.clear()
        else:
            QMessageBox.warning(self, "Word Validation", f"'{word}' is not a valid word.")
    
            self.isTurnInProgress = False  # Réinitialiser l'état du tour
            self.draw_button.setEnabled(True)  # Réactiver le bouton pour le prochain tour


    def handleTileMoved(self, letter):
         if letter in self.letters_drawn:
            self.letters_drawn.remove(letter)  # Retirer la lettre déplacée
            self.update_draw_zone()  # Mettre à jour l'affichage des tuiles

    def update_draw_zone(self):
    # Mettez à jour l'affichage pour montrer uniquement les tuiles restantes.
     for i, tile in enumerate(self.letter_labels):
        if i < len(self.letters_drawn):
            tile.setText(self.letters_drawn[i])
            tile.setVisible(True)  # Rendre la tuile visible
        else:
            tile.setVisible(False)  # Cacher les tuiles non utilisées


    def handleTileMoved(self, letter):
        # Supprimez la lettre de la liste des lettres tirées
        if letter in self.letters_drawn:
            self.letters_drawn.remove(letter)
            self.update_draw_zone()  # Mettez à jour la draw_zone

    def returnTileToDrawZone(self, letter):
        # Ajoutez une lettre retournée du plateau à la draw_zone
        self.letters_drawn.append(letter)
        self.update_draw_zone()

def main():
    app = QApplication(sys.argv)
    scrabble_board = ScrabbleBoard()
    scrabble_board.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()