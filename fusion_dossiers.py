import os

# Chemins vers vos trois dossiers source et le dossier cible
dossier1 = r'C:\Users\eptec\Desktop\SCRABBLE\scrabble_vocabularies'
dossier2 = r'C:\Users\eptec\Desktop\SCRABBLE\scrabble_vocabularies1'
dossier3 = r'C:\Users\eptec\Desktop\SCRABBLE\scrabble_vocabularies2'
dossier4 = r'C:\Users\eptec\Desktop\SCRABBLE\scrabble_vocabularies3'
dossier_cible = r'C:\Users\eptec\Desktop\dictionnaire_compilé'

# Assurez-vous que le dossier cible existe
os.makedirs(dossier_cible, exist_ok=True)

# Liste des noms de fichiers (supposons qu'ils sont identiques dans tous les dossiers)
noms_fichiers = [f for f in os.listdir(dossier1) if os.path.isfile(os.path.join(dossier1, f))]

for nom_fichier in noms_fichiers:
    # Ensemble pour garder une trace des lignes uniques
    lignes_uniques = set()

    # Lire et ajouter le contenu de chaque fichier à l'ensemble pour éliminer les doublons
    for dossier in [dossier1, dossier2, dossier3, dossier4]:
        chemin_fichier = os.path.join(dossier, nom_fichier)
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            lignes_uniques.update(fichier.readlines())

    # Écrire le contenu unique dans un nouveau fichier dans le dossier cible
    chemin_fichier_cible = os.path.join(dossier_cible, nom_fichier)
    with open(chemin_fichier_cible, 'w', encoding='utf-8') as fichier_cible:
        fichier_cible.writelines(sorted(lignes_uniques))  # Écriture des lignes triées pour une meilleure organisation

print("Fusion terminée.")
