import pandas as pd


dt = pd.read_csv("Lexique 3.83/Lexique_modifié.csv", sep=";")
data = dt.head(1000)

def set_categorie(gram):
    catégorie = []
    for i, j in enumerate(data.classe):
        j = str(j)
        if j[0:3] == gram:
            catégorie += [data.orthographe[i]]
    return catégorie

noms = set_categorie("NOM")

def set_nbsyllabes(syll, liste):
    liste_syllabes = []
    for i, j in enumerate(data.orthographe):
        for k in liste:
            if j == k and data.nbsyll[i] == syll:
                liste_syllabes += [data.orthographe[i]]
    return liste_syllabes

print(set_nbsyllabes(3, noms))