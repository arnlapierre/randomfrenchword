import pandas as pd
from random import choice
import time

class MotAléatoire:

    def __init__(self):
        self.dt = pd.read_csv("Lexique_modifié.csv", sep=";")

    def mot(self):
        # Retourne un mot aléatoire sans critères de sélection.
        return choice(self.dt.orthographe)

    def set_categorie(self, gram):
        catégorie = [i for i in self.dt[self.dt["classe"] == gram].orthographe]
        return catégorie

    def set_categorie_2(self, gram):
        # catégorie = [i for i in self.dt[self.dt["classe"] == gram].orthographe]
        catégorie = self.dt[self.dt["classe"] == gram]
        return catégorie

    def set_premlettre(self, lettre, liste):
        #Méthode qui permet de définir comment restreindre les méthodes de
        #Groupe grammaticales à une première lettre.
        #Lettre doit être entre a et z en incluant les caractères accents.
        liste_premlettre = []
        for i in liste:
            i = str(i)
            if i[:1] == lettre:
                liste_premlettre += [i]
        return liste_premlettre

    def set_dtpremlettre(self, lettre, dataframe):
        première_lettre = dataframe[dataframe.orthographe.str[:1] == lettre]
        return première_lettre

    def set_nblettres(self, nb, liste):
        #retourne un mot aléatoire en fonction du nombre de lettres. nb est
        # un int entre 1 et 25.
        liste_nblettres = []
        for i in liste:
            i = str(i)
            if len(i) == nb:
                liste_nblettres += [i]
        return liste_nblettres

    def set_nbsyllabes(self, syll, liste):
        #retourne un mot aléatoire en fonction du nombre de syllabes. syll doit être
        # un int. syll est entre 1 et 9.
        liste_syllabes = []
        liste = set(liste)  #en faisant cela, on double la vitesse de cette méthode, puisque
                            #on n'a seulement besoin que de faire «in» (ligne 52).
        for i, j in enumerate(self.dt.orthographe):
            if j in liste and self.dt.nbsyll[i] == syll:
                    liste_syllabes += [self.dt.orthographe[i]]
        return liste_syllabes

    def set_rareté(self):
        # retourne un mot en fonction de sa rareté (à la fois dans les films et dans les livres).
        pass
        #TODO

    def set_all(self, catégorie, liste_premlettres, liste_nblettres, liste_syllabes=None):
        pass
        #TODO

    def nom(self, *, premlettre=None, nblettres=None, nbsyllabes=None):
        noms = self.set_categorie("NOM")
        #TODO travailler avec des dataframe plutôt que des listes?
        # préférable pour syllabe et fréquence...
        if premlettre:
            noms = self.set_premlettre(premlettre, noms)
        if nblettres:
            noms = self.set_nblettres(nblettres, noms)
        if nbsyllabes:
            noms = self.set_nbsyllabes(nbsyllabes, noms)
        return choice(noms)

    def adjectif(self):
        adjectifs = self.set_categorie("ADJ")
        return choice(adjectifs)

    def verbe(self):
        verbes = self.set_categorie("VER")
        return choice(verbes)

    def auxiliaire(self):
        auxiliaires = self.set_categorie("AUX")
        return choice(auxiliaires)

    def préposition(self):
        prépositions = self.set_categorie("PRE")
        return choice(prépositions)

    def adverbe(self):
        adverbes = self.set_categorie("ADV")
        return choice(adverbes)

    def conjonction(self):
        conjonctions = self.set_categorie("CON")
        return choice(conjonctions)

    def onomatopée(self):
        onomatopées = self.set_categorie("ONO")
        return choice(onomatopées)

    def pronom(self):
        pronoms = self.set_categorie("PRO")
        return choice(pronoms)

    def déterminant(self):
        déterminants = self.set_categorie("ART")
        return choice(déterminants)

print(MotAléatoire().nom(premlettre = "a"))
