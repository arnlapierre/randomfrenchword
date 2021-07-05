from tkinter import *
from class_mot_aléatoire import MotAléatoire

# Paramètres de la fenêtre
window = Tk()
window.title("Générateur aléatoire de mots")
window.minsize(width=300, height=200)
window.config(padx=40, pady=40, bg="deep sky blue")

# Label pour afficher le mot
affichage = Label(text="")
affichage.grid(row=0, column=0, columnspan=2)


# Button
def generer_mot():
    # Catégorie
    if check_classe.get() == 1:
        cat_var = categorie_entry.get()
    else:
        cat_var = None

    # Nb lettres
    if check_nblettres.get() == 1:
        nb_lettres_var = int(spinbox_nblettres.get())
    else:
        nb_lettres_var = None

    # Nb syllabes
    if check_nb_syllabes.get() == 1:
        nb_syllabes_var = int(spinbox_nbsyllabes.get())
    else:
        nb_syllabes_var = None

    # Première lettre
    if check_1st_lettre.get() == 1:
        prem_lettre_var = prem_lettre_entry.get()
    else:
        prem_lettre_var = None

    affichage.config(text=MotAléatoire().set_all(cat=cat_var, nblettres=nb_lettres_var,
                                                 premlettre=prem_lettre_var,
                                                 nbsyllabes=nb_syllabes_var))


generer = Button(text="Générer", command=generer_mot)
generer.grid(row=3, column=2, padx=3, pady=3)

# Catégorie
categorie_entry = Entry(width=7)
categorie_entry.grid(row=2, column=0, padx=3, pady=3)

check_classe = IntVar()
checkbutton_categorie = Checkbutton(text="Catégorie", variable=check_classe)
checkbutton_categorie.grid(row=1, column=0, padx=3, pady=3)

# Nombre de lettres
spinbox_nblettres = Spinbox(from_=0, to=25, width=7)
spinbox_nblettres.grid(row=2, column=1, padx=3, pady=3)

check_nblettres = IntVar()
checkbutton_nblettres = Checkbutton(text="# Lettres", variable=check_nblettres)
checkbutton_nblettres.grid(row=1, column=1, padx=3, pady=2)

# Nombre de syllabes
spinbox_nbsyllabes = Spinbox(from_=0, to=7, width=7)
spinbox_nbsyllabes.grid(row=2, column=2, padx=3, pady=3)

check_nb_syllabes = IntVar()
checkbutton_syllabes = Checkbutton(text="# Syllabes", variable=check_nb_syllabes)
checkbutton_syllabes.grid(row=1, column=2, padx=3, pady=3)

# Première lettre
prem_lettre_entry = Entry(width=7)
prem_lettre_entry.grid(row=2, column=3, padx=3, pady=3)

check_1st_lettre = IntVar()
checkbutton_1st_lettre = Checkbutton(text="Première lettre", variable=check_1st_lettre)
checkbutton_1st_lettre.grid(row=1, column=3, padx=3, pady=3)

# Rareté
rarete = Label(text="Rareté", width=7)
rarete.grid(row=1, column=4, padx=3, pady=3)

window.mainloop()
