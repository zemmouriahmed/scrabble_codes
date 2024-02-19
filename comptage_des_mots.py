import os

# Chemin vers le dossier contenant les fichiers
dossier = r'C:\Users\eptec\Desktop\SCRABBLE\scrabble_vocabularies8'

# Initialisation du compteur total de mots
total_mots = 0

# Parcourir tous les fichiers du dossier
for nom_fichier in os.listdir(dossier):
    chemin_fichier = os.path.join(dossier, nom_fichier)
    # Vérifier si c'est bien un fichier pour éviter les dossiers
    if os.path.isfile(chemin_fichier):
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            # Lire le contenu du fichier
            contenu = fichier.read()
            # Compter les mots dans le fichier actuel
            mots = contenu.split()
            nombre_mots = len(mots)
            print(f"{nom_fichier} contient {nombre_mots} mots.")
            # Ajouter au total global
            total_mots += nombre_mots

# Afficher le total global de mots
print(f"Total de mots dans tous les fichiers: {total_mots}")
