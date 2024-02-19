# N'oubliez pas d'importer les modules nécessaires de PyQt5
from PyQt5.QtCore import Qt, QMimeData, pyqtSignal
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QLabel

class Tile(QLabel):
    def __init__(self, letter, parent=None):
        super().__init__(letter, parent)
        self.letter = letter
        self.setFixedSize(40, 40)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            drag = QDrag(self)
            mimeData = QMimeData()
            mimeData.setText(self.letter)
            drag.setMimeData(mimeData)
            drag.exec_(Qt.MoveAction)

class BoardTile(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setFixedSize(40, 40)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        self.setText(event.mimeData().text())
