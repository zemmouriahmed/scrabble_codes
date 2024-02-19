import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []

    def draw_initial_letters(self, letter_bag, num_letters):
        # Piocher un ensemble initial de lettres du sac
        drawn_letters = random.sample(letter_bag, num_letters)
        self.hand.extend(drawn_letters)

    def display_hand(self):
        print(f"{self.name}'s Hand: {', '.join([letter for letter in self.hand])}")

    def choose_letters(self):
        # Le joueur choisit des lettres pour composer son mot
        chosen_letters = input(f"{self.name}, choisissez les lettres pour votre mot (séparées par des espaces): ").upper().split()
        # Vérifier que les lettres choisies sont dans la main du joueur
        valid_choices = [letter for letter in chosen_letters if letter in self.hand]
        return valid_choices

    def validate_word(self, word, dictionary):
        # Valider si le mot est dans le dictionnaire
        return word.upper() in dictionary

    def draw_letters(self, letter_bag, num_letters):
        # Piocher des lettres pour compléter la main du joueur
        drawn_letters = random.sample(letter_bag, num_letters)
        self.hand.extend(drawn_letters)

def load_dictionary(file_path):
    # Charger le dictionnaire à partir d'un fichier texte
    with open(file_path, 'r', encoding='utf-8') as file:
        dictionary = set(word.strip().upper() for word in file.readlines())
    return dictionary

def initialize_game(num_players):
    # Définir les lettres, y compris les jokers
    letters = [
        {'letter': 'A', 'value': 1, 'quantity': 9},
        # ... Ajouter les autres lettres avec valeurs et quantités
        {'letter': '*', 'value': 0, 'quantity': 2},  # Joker
    ]

    # Initialiser le sac de lettres
    letter_bag = []
    letter_numbering = {index: letter_info['letter'] for index, letter_info in enumerate(letters)}
    for letter_index in letter_numbering:
        quantity = letters[letter_index]['quantity']
        letter_bag.extend([letter_index] * quantity)

    # Mélanger le sac (facultatif mais recommandé)
    random.shuffle(letter_bag)

    # Initialiser les joueurs
    players = [Player(f"Joueur {i+1}") for i in range(num_players)]

    # Distribuer les lettres initiales à chaque joueur
    num_initial_letters = 7  # Nombre standard de lettres pour chaque joueur au début
    for player in players:
        player.draw_initial_letters(letter_bag, num_initial_letters)

    return players, letter_bag

def display_board(board):
    # Fonction pour afficher le plateau (à définir)
    pass

def display_player_info(player):
    print(f"{player.name} - Score: {player.score} - Main: {', '.join([letter for letter in player.hand])}")

# Emplacement du fichier contenant le dictionnaire ODS
ods_file_path = 'votre_chemin_vers_le_fichier_ODS.txt'  # Remplacez par le chemin réel de votre fichier ODS

# Charger le dictionnaire ODS
ods_dictionary = load_dictionary(ods_file_path)

# Exemple d'utilisation
num_players = 4
players, letter_bag = initialize_game(num_players)

# Afficher les informations des joueurs
for player in players:
    display_player_info(player)

# Tour de chaque joueur pour composer son premier mot
for player in players:
    print(f"\nTour de {player.name} :")
    player.display_hand()

    # Boucle pour permettre au joueur de former un mot valide
    while True:
        chosen_letters = player.choose_letters()
        chosen_word = ''.join(chosen_letters)

        if player.validate_word(chosen_word, ods_dictionary):
            print(f"{player.name} a choisi le mot : {chosen_word}")
            # Ici, vous pouvez ajouter la logique pour placer le mot sur le plateau et calculer les points

            # Piocher des lettres pour compléter la main du joueur
            num_drawn_letters = num_initial_letters - len(chosen_letters)
            player.draw_letters(letter_bag, num_drawn_letters)
            display_player_info(player)
            break
        else:
            print(f"Le mot {chosen_word} n'est pas valide. Veuillez reformer votre mot.")