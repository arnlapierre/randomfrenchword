import pandas as pd
from random import choice


class MotAléatoire:

    def __init__(self):
        self.dt = pd.read_csv("Lexique_modifié.csv", sep=";")
        for i in self.dt.freqfilms:
            i == int(i)

    def mot(self):
        # Retourne un mot aléatoire sans critères de sélection.
        return choice(self.dt.orthographe)

    def set_categorie(self, gram):
        catégorie_df = self.dt[self.dt["classe"] == gram]
        return catégorie_df

    def set_premlettre(self, lettre, dataframe):
        première_lettre_df = dataframe[dataframe.orthographe.str[:1] == lettre]
        return première_lettre_df

    def set_nblettres(self, nb, dataframe):
        # Détermine un mot en fonction du nb de lettres (entre 1 et 25 lettres).
        nblettres_df = dataframe[dataframe.nblettres == nb]
        return nblettres_df

    def set_nbsyllabes(self, syl, dataframe):
        # Détermine un mot en fonction du nb de syllabes (entre 1 et 9 syllabes).
        nbsyllabes_df = dataframe[dataframe.nbsyll == syl]
        return nbsyllabes_df

    def set_genre(self, genre, dataframe):
        # TODO
        pass

    def set_nombre(self, nombre, dataframe):
        # TODO
        pass

    def set_rare_films(self, rareté, dataframe):
        # TODO ajuster la rareté avec un quelconque barême.
        # BOOL. Retourne un mot rare à partir de la fréquence dans les scénarios de films.
        if rareté is False:
            rareté_films_df = dataframe[dataframe.freqfilms > 1]
        if rareté is True:
            rareté_films_df = dataframe[dataframe.freqfilms < 0.05]
        return rareté_films_df

    def set_rare_livres(self, rareté, dataframe):
        # TODO ajuster la rareté avec un quelconque barême.
        # BOOL. Retourne un mot rare à partir de la fréquence dans les scénarios de films.
        if rareté is False:
            rareté_livres_df = dataframe[dataframe.freqlivres > 1]
        if rareté is True:
            rareté_livres_df = dataframe[dataframe.freqlivres < 0.05]
        return rareté_livres_df

    def set_all(self, classe, *, premlettre=None, nblettres=None, nbsyllabes=None, rareté=None):
        # TODO trouver le problème quand je l'appelle pour une catégorie
        df = self.set_categorie(classe)
        if premlettre:
            df = self.set_premlettre(premlettre, df)
        if nblettres:
            df = self.set_nblettres(nblettres, df)
        if nbsyllabes:
            df = self.set_nbsyllabes(nbsyllabes, df)
        if rareté is not None:
            df = self.set_rare_films(rareté, df)
        return choice(list(df.orthographe))

    def nom(self, *, premlettre=None, nblettres=None, nbsyllabes=None,
            rareté_films=None, rareté_livres=None):
        noms = self.set_categorie("NOM")
        if premlettre:
            noms = self.set_premlettre(premlettre, noms)
        if nblettres:
            noms = self.set_nblettres(nblettres, noms)
        if nbsyllabes:
            noms = self.set_nbsyllabes(nbsyllabes, noms)
        if rareté_films is not None:
            noms = self.set_rare_films(rareté_films, noms)
        if rareté_livres is not None:
            noms = self.set_rare_livres(rareté_livres, noms)
        return choice(list(noms.orthographe))

    def adjectif(self, *, premlettre=None, nblettres=None, nbsyllabes=None,
            rareté_films=None, rareté_livres=None):
        adjectifs = self.set_categorie("ADJ")
        if premlettre:
            adjectifs = self.set_premlettre(premlettre, adjectifs)
        if nblettres:
            adjectifs = self.set_nblettres(nblettres, adjectifs)
        if nbsyllabes:
            adjectifs = self.set_nbsyllabes(nbsyllabes, adjectifs)
        if rareté_films is not None:
            adjectifs = self.set_rare_films(rareté_films, adjectifs)
        if rareté_livres is not None:
            adjectifs = self.set_rare_livres(rareté_livres, adjectifs)
        return choice(list(adjectifs.orthographe))

    def verbe(self, *, premlettre=None, nblettres=None, nbsyllabes=None,
        rareté_films=None, rareté_livres=None):
        verbes = self.set_categorie("VER")
        if premlettre:
            verbes = self.set_premlettre(premlettre, verbes)
        if nblettres:
            verbes = self.set_nblettres(nblettres, verbes)
        if nbsyllabes:
            verbes = self.set_nbsyllabes(nbsyllabes, verbes)
        if rareté_films is not None:
            verbes = self.set_rare_films(rareté_films, verbes)
        if rareté_livres is not None:
            verbes = self.set_rare_livres(rareté_livres, verbes)
        return choice(list(verbes.orthographe))

    def auxiliaire(self, *, premlettre=None, rareté_films=None, rareté_livres=None):
        auxiliaires = self.set_categorie("AUX")
        if premlettre:
            auxiliaires = self.set_premlettre(premlettre, auxiliaires)
        if rareté_films is not None:
            auxiliaires = self.set_rare_films(rareté_films, auxiliaires)
        if rareté_livres is not None:
            auxiliaires = self.set_rare_livres(rareté_livres, auxiliaires)
        return choice(list(auxiliaires.orthographe))

    def préposition(self, *, premlettre=None, rareté_films=None, rareté_livres=None):
        prépositions = self.set_categorie("PRE")
        if premlettre:
            prépositions = self.set_premlettre(premlettre, prépositions)
        if rareté_films is not None:
            prépositions = self.set_rare_films(rareté_films, prépositions)
        if rareté_livres is not None:
            prépositions = self.set_rare_livres(rareté_livres, prépositions)
        return choice(list(prépositions.orthographe))

    def adverbe(self, *, premlettre=None, nblettres=None, nbsyllabes=None,
            rareté_films=None, rareté_livres=None):
        adverbes = self.set_categorie("ADV")
        if premlettre:
            adverbes = self.set_premlettre(premlettre, adverbes)
        if nblettres:
            adverbes = self.set_nblettres(nblettres, adverbes)
        if nbsyllabes:
            adverbes = self.set_nbsyllabes(nbsyllabes, adverbes)
        if rareté_films is not None:
            adverbes = self.set_rare_films(rareté_films, adverbes)
        if rareté_livres is not None:
            adverbes = self.set_rare_livres(rareté_livres, adverbes)
        return choice(list(adverbes.orthographe))

    def conjonction(self, *, premlettre=None, rareté_films=None, rareté_livres=None):
        conjonctions = self.set_categorie("CON")
        if premlettre:
            conjonctions = self.set_premlettre(premlettre, conjonctions)
        if rareté_films is not None:
            conjonctions = self.set_rare_films(rareté_films, conjonctions)
        if rareté_livres is not None:
            conjonctions = self.set_rare_livres(rareté_livres, conjonctions)
        return choice(list(conjonctions.orthographe))

    def onomatopée(self, *, premlettre=None, nblettres=None, nbsyllabes=None,
            rareté_films=None, rareté_livres=None):
        onomatopées = self.set_categorie("ONO")
        if premlettre:
            onomatopées = self.set_premlettre(premlettre, onomatopées)
        if nblettres:
            onomatopées = self.set_nblettres(nblettres, onomatopées)
        if nbsyllabes:
            onomatopées = self.set_nbsyllabes(nbsyllabes, onomatopées)
        if rareté_films is not None:
            onomatopées = self.set_rare_films(rareté_films, onomatopées)
        if rareté_livres is not None:
            onomatopées = self.set_rare_livres(rareté_livres, onomatopées)
        return choice(list(onomatopées.orthographe))

    def pronom(self, *, premlettre=None, nblettres=None, nbsyllabes=None,
            rareté_films=None, rareté_livres=None):
        pronoms = self.set_categorie("PRO")
        if premlettre:
            pronoms = self.set_premlettre(premlettre, pronoms)
        if nblettres:
            pronoms = self.set_nblettres(nblettres, pronoms)
        if nbsyllabes:
            pronoms = self.set_nbsyllabes(nbsyllabes, pronoms)
        if rareté_films is not None:
            pronoms = self.set_rare_films(rareté_films, pronoms)
        if rareté_livres is not None:
            pronoms = self.set_rare_livres(rareté_livres, pronoms)
        return choice(list(pronoms.orthographe))

    def déterminant(self, *, premlettre=None, rareté_films=None, rareté_livres=None):
        déterminants = self.set_categorie("ART")
        if premlettre:
            déterminants = self.set_premlettre(premlettre, déterminants)
        if rareté_films is not None:
            déterminants = self.set_rare_films(rareté_films, déterminants)
        if rareté_livres is not None:
            déterminants = self.set_rare_livres(rareté_livres, déterminants)
        return choice(list(déterminants.orthographe))


print(MotAléatoire().onomatopée(rareté_livres=False))
