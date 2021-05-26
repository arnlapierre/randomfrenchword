import pandas as pd
from random import choice


class Mot_aléatoire:
    def __init__(self):
        self.dt = pd.read_csv("Lexique 3.83\Lexique_modifié.csv", sep=";")

    def mot(self):
        # Retourne un mot aléatoire sans critères de sélection.
        mots = []
        for i in self.dt.orthographe:
            mots += [i]
        return choice(mots)

    def set_categorie(self, gram):
        catégorie = []
        for i, j in enumerate(self.dt.classe):
            j = str(j)
            if j[0:3] == gram:
                catégorie += [self.dt.orthographe[i]]
        return catégorie

    def set_premlettre(self, lettre, liste):
        #Méthode qui permet de définir comment restraindre les méthodes de
        #Groupe grammaticales à une première lettre.
        #Lettre doit être entre a et z en incluant les caractères accents.
        liste_premlettre = []
        for i in liste:
            i = str(i)
            if i[:1] == lettre:
                liste_premlettre += [i]
        return liste_premlettre

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
        for i, j in enumerate(self.dt.orthographe):
            if j in liste and self.dt.nbsyll[i] == syll:
                    liste_syllabes += [self.dt.orthographe[i]]
        return liste_syllabes

    def set_all(self, catégorie, liste_premlettres, liste_nblettres, liste_syllabes=None):
        pass
        #TODO

    def nom(self, *, premlettre=None, nblettres=None, nbsyllabes=None):
        noms = self.set_categorie("NOM")
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

print(Mot_aléatoire().nom(premlettre="b", nblettres=8, nbsyllabes=4))