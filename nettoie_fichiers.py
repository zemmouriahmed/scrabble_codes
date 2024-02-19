import os

def remove_duplicates_from_file(file_path):
    if os.path.exists(file_path):
        # Lire les mots du fichier tout en préservant l'ordre et en éliminant les doublons
        with open(file_path, 'r', encoding='utf-8') as file:
            unique_words = set()
            words_in_order = []
            for line in file:
                word = line.strip()
                if word not in unique_words:
                    unique_words.add(word)
                    words_in_order.append(word)
        
        # Réécrire le fichier avec les mots uniques
        with open(file_path, 'w', encoding='utf-8') as file:
            for word in words_in_order:
                file.write(f"{word}\n")

def main():
    directory =directory = "C:\\Users\\eptec\\Desktop\\SCRABBLE\\scrabble_vocabularies"
 # Modifier ce chemin selon l'emplacement de vos fichiers
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        file_path = os.path.join(directory, f'{letter}.txt')
        remove_duplicates_from_file(file_path)
        print(f"Doublons supprimés pour {file_path}")

if __name__ == "__main__":
    main()
