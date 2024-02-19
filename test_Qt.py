import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # Configuration initiale de la fenêtre
        self.setWindowTitle('Interaction entre Widgets')  # Définit le titre de la fenêtre
        self.setGeometry(100, 100, 280, 80)  # Définit la position et la taille de la fenêtre (x, y, largeur, hauteur)

        # Création et configuration du QVBoxLayout (layout vertical)
        layout = QVBoxLayout()
        
        # Création du QLineEdit (champ de saisie)
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Écrivez quelque chose ici et appuyez sur Entrée')  # Texte indicatif
        self.line_edit.returnPressed.connect(self.onReturnPressed)  # Connecte le signal returnPressed à la méthode onReturnPressed
        layout.addWidget(self.line_edit)  # Ajoute le QLineEdit au layout

        # Création du QLabel (étiquette pour afficher le texte)
        self.label = QLabel('Le texte saisi s\'affichera ici')
        layout.addWidget(self.label)  # Ajoute le QLabel au layout

        # Configuration du layout de la fenêtre principale
        self.setLayout(layout)

    def onReturnPressed(self):
        # Méthode appelée lorsque la touche Entrée est pressée dans le QLineEdit
        input_text = self.line_edit.text()  # Récupère le texte saisi dans le QLineEdit
        self.label.setText(input_text)  # Met à jour le QLabel avec le texte saisi

def main():
    # Crée une instance de l'application
    app = QApplication(sys.argv)
    window = MyWindow()  # Crée une instance de la fenêtre principale
    window.show()  # Affiche la fenêtre
    sys.exit(app.exec_())  # Démarre la boucle d'événements de l'application

if __name__ == '__main__':
    main()
