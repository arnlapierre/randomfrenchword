import pandas as pd
from random import choice


class MotAléatoire:

    def __init__(self):
        self.dt = pd.read_csv("Lexique_modifié.csv", sep=";")

    def afficher_catégories(self):
        # Retourne :
        # ['NOM', 'AUX', 'VER', 'ADV', 'PRE', 'ADJ', 'ONO', 'CON', 'ART', 'PRO']
        catégories = []
        for i in self.dt.classe:
            if str(i)[:3] not in catégories:
                catégories.append(str(i)[:3])
        return catégories[:10]

    def mot(self):
        # TODO méthode caduque si j'utilise set_all. set_all avec aucun argument devient cette méthode
        # Retourne un mot aléatoire sans critères de sélection.
        return choice(self.dt.orthographe)

    def set_categorie(self, gram):
        catégorie_df = self.dt[self.dt["classe"].str[0:3] == gram]
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

    def set_all(self, *, cat=None, premlettre=None, nblettres=None, nbsyllabes=None, rareté=None):
        # catégories :
        # ['NOM', 'AUX', 'VER', 'ADV', 'PRE', 'ADJ', 'ONO', 'CON', 'ART', 'PRO']
        if cat:
            df = self.set_categorie(cat)
        else:
            df = self.dt
        if premlettre:
            df = self.set_premlettre(premlettre, df)
        if nblettres:
            df = self.set_nblettres(nblettres, df)
        if nbsyllabes:
            df = self.set_nbsyllabes(nbsyllabes, df)
        if rareté is not None:
            df = self.set_rare_films(rareté, df)
        if len(df) == 0:
            return "Aucun mot ne correspond à ces critères de recherche."
        return choice(list(df.orthographe))
