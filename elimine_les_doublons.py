import os

# Chemin vers le dossier contenant les fichiers
dossier = r'C:\Users\eptec\Desktop\dictionnaire_compilé'

# Ensemble pour garder une trace de tous les mots uniques à travers les fichiers
mots_uniques_globaux = set()

# Parcourir tous les fichiers du dossier
for nom_fichier in os.listdir(dossier):
    chemin_fichier = os.path.join(dossier, nom_fichier)
    # Vérifier si c'est bien un fichier pour éviter les dossiers
    if os.path.isfile(chemin_fichier):
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            # Lire le contenu du fichier et le convertir en un ensemble de mots uniques
            contenu = fichier.read()
            mots_uniques_fichier = set(contenu.split())
            print(f"{nom_fichier} contient {len(mots_uniques_fichier)} mots uniques.")
            # Fusionner avec l'ensemble global de mots uniques
            mots_uniques_globaux.update(mots_uniques_fichier)

# Afficher le total de mots uniques à travers tous les fichiers
print(f"Total de mots uniques dans tous les fichiers: {len(mots_uniques_globaux)}")
