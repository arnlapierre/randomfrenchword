""" Ce module importe le contenu d'un fichier csv 'Lexique383_colonnes de moins.csv'."""
"""À partir de la colonne 'orthographe de ce fichier, on choisit un mot au hasard parmi les 146000+"""
"""entrées."""

import pandas as pd
import random

#TODO ajouter préposition, conjonction, pronom, article (ART:def)
def mot_aléatoire(*, adjectif=False, verbe=False, adverbe=False, nom=False):

    fichier = ("Lexique_modifié.csv")
    data = pd.read_csv(fichier, sep=";") # data est un dataframe
    #conditions de recherche
    adjectifs, verbes, noms, adverbes = [], [], [], []
    for i in data.itertuples():
        if i[2] == "ADJ":
            adjectifs += [i[1]]
        elif i[2] == "VER":
            verbes += [i[1]]
        elif i[2] == "ADV":
            adverbes += [i[1]]
        elif i[2] == "NOM":
            noms += [i[1]]

    liste_totale = []
    args = [(adjectif, adjectifs), (verbe, verbes), (adverbe, adverbes), (nom, noms)]
    for i in args:
        if i[0] is True:
            liste_totale += i[1]

    #si l'arg positionnel adjectif est True
    if adjectif is True:
        print(f"Il y a {len(adjectifs)} adjectifs dans les choix.")
    #si l'arg posititionnel verbe est True
    if verbe is True:
        print(f"Il y a {len(verbes)} verbes dans les choix.")
    #si l'arg posititionnel adverbe est True
    if adverbe is True:
        print(f"Il y a {len(adverbes)} adverbes dans les choix.")
    #si l'arg posititionnel nom est True
    if nom is True:
        print(f"Il y a {len(noms)} noms dans les choix.")

    #si la fonction est appelée sans arguments, elle retourne un mot au hasard,
    #toute catégorie confondue
    if liste_totale != []:
        print(f"mot aléatoire : {random.choice(liste_totale)}.")
        print(f"Il y a {len(liste_totale)} mots dans la liste.")
    else:
        print(f"mot aléatoire : {random.choice(data['orthographe'])}.")
        print(f"Il y a {len(data['orthographe'])} mots dans la liste.")

