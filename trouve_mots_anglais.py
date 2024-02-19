from itertools import permutations

# Supposons que vous avez une liste de mots anglais appelée `liste_mots_anglais`
# liste_mots_anglais = [...]

def trouver_mots_possibles(lettres, liste_mots_anglais):
    mots_possibles = set()
    # Générer toutes les permutations des lettres pour toutes les longueurs possibles
    for i in range(1, len(lettres) + 1):
        for combo in permutations(lettres, i):
            mot_potentiel = ''.join(combo)
            if mot_potentiel in liste_mots_anglais:
                mots_possibles.add(mot_potentiel)
    return mots_possibles

# Exemple d'utilisation
lettres = input("Entrez sept lettres sans espace entre elles : ")
# Vous devrez remplacer ceci par votre liste de mots anglais
liste_mots_anglais = ["word", "rod", "row", "dow", "dog", "god", "grow", "woe", "owe", "wear", "awe", "war", "raw"]

mots_trouves = trouver_mots_possibles(lettres, liste_mots_anglais)

print(f"Mots possibles avec les lettres '{lettres}':")
for mot in sorted(mots_trouves):
    print(mot)
