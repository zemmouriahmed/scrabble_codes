import random

# Définition des lettres avec leurs valeurs et quantités
letters = [
    {'letter': 'A', 'value': 1, 'quantity': 9},
    {'letter': 'B', 'value': 3, 'quantity': 2},
    {'letter': 'C', 'value': 3, 'quantity': 2},
    {'letter': 'D', 'value': 2, 'quantity': 4},
    {'letter': 'E', 'value': 1, 'quantity': 12},
    {'letter': 'F', 'value': 4, 'quantity': 2},
    {'letter': 'G', 'value': 2, 'quantity': 3},
    {'letter': 'H', 'value': 4, 'quantity': 2},
    {'letter': 'I', 'value': 1, 'quantity': 9},
    {'letter': 'J', 'value': 8, 'quantity': 1},
    {'letter': 'K', 'value': 10, 'quantity': 1},
    {'letter': 'L', 'value': 1, 'quantity': 4},
    {'letter': 'M', 'value': 2, 'quantity': 2},
    {'letter': 'N', 'value': 1, 'quantity': 6},
    {'letter': 'O', 'value': 1, 'quantity': 8},
    {'letter': 'P', 'value': 3, 'quantity': 2},
    {'letter': 'Q', 'value': 10, 'quantity': 1},
    {'letter': 'R', 'value': 1, 'quantity': 6},
    {'letter': 'S', 'value': 1, 'quantity': 4},
    {'letter': 'T', 'value': 1, 'quantity': 6},
    {'letter': 'U', 'value': 1, 'quantity': 4},
    {'letter': 'V', 'value': 4, 'quantity': 2},
    {'letter': 'W', 'value': 4, 'quantity': 2},
    {'letter': 'X', 'value': 8, 'quantity': 1},
    {'letter': 'Y', 'value': 4, 'quantity': 2},
    {'letter': 'Z', 'value': 10, 'quantity': 1},
    {'letter': '*', 'value': 0, 'quantity': 2},  # Joker
]

# Initialisation du sac de lettres
letter_bag = []

# Attribution de numéros uniques à chaque lettre
letter_numbering = {index: letter_info['letter'] for index, letter_info in enumerate(letters)}

# Remplir le sac avec les numéros en fonction de la quantité souhaitée pour chaque lettre
for letter_index in letter_numbering:
    quantity = letters[letter_index]['quantity']
    letter = letter_numbering[letter_index]
    
    letter_bag.extend([letter_index] * quantity)

# Mélanger le sac (facultatif mais recommandé)
random.shuffle(letter_bag)

# Exemple : Tirer trois lettres aléatoires du sac
drawn_letter_indices = random.sample(letter_bag, 7)

# Convertir les indices en lettres
drawn_letters = [letter_numbering[index] for index in drawn_letter_indices]

print("Lettres tirées :", drawn_letters)