import os

def count_words_in_file(file_path):
    word_count = 0
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                word_count += 1
    return word_count

def main():
    directory = r"C:\Users\eptec\Desktop\SCRABBLE\scrabble_vocabularies"  # Assurez-vous que le chemin est correct
    total_word_count = 0
    
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        file_path = os.path.join(directory, f'{letter}.txt')
        word_count = count_words_in_file(file_path)
        total_word_count += word_count
        print(f"{file_path} contient {word_count} mots.")
    
    print(f"Nombre total de mots dans tous les fichiers : {total_word_count}")

if __name__ == "__main__":
    main()