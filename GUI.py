from tkinter import *
from class_mot_aléatoire import MotAléatoire

# Paramètres de la fenêtre
window = Tk()
window.title("Générateur aléatoire de mots")
window.geometry("630x220")
window.config(padx=40, pady=40, bg="deep sky blue")

# Label pour afficher le mot
affichage = Label(text="", anchor="w", bg="white", width=22, relief="ridge", font=("Bookman Old Style", 12, "bold"))
affichage.grid(row=0, column=0, columnspan=3, pady=3, sticky="w")


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

    # Rareté
    if check_rarete_2.get() == 1:
        if radio_rarete.get() == 1:
            rarete_radio_var = False
        if radio_rarete.get() == 2:
            rarete_radio_var = True
    else:
        rarete_radio_var = None

    affichage.config(text=MotAléatoire().set_all(cat=cat_var, nblettres=nb_lettres_var,
                                                 premlettre=prem_lettre_var,
                                                 nbsyllabes=nb_syllabes_var,
                                                 rareté=rarete_radio_var))


# Button
generer = Button(text="Générer", command=generer_mot, bg="white")
generer.grid(row=4, column=2, padx=3, pady=3)

# Catégorie
# TODO Combobox
categorie_entry = Entry(width=12, relief="ridge")
categorie_entry.grid(row=2, column=0, padx=3, pady=3)

check_classe = IntVar()
checkbutton_categorie = Checkbutton(text="Catégorie", variable=check_classe, bg="white", relief="ridge")
checkbutton_categorie.grid(row=1, column=0, pady=3)

# Nombre de lettres
spinbox_nblettres = Spinbox(from_=0, to=25, width=9, relief="ridge")
spinbox_nblettres.grid(row=2, column=1, padx=3, pady=3)

check_nblettres = IntVar()
checkbutton_nblettres = Checkbutton(text="# Lettres", variable=check_nblettres, bg="white", relief="ridge")
checkbutton_nblettres.grid(row=1, column=1, padx=6, pady=2)

# Nombre de syllabes
spinbox_nbsyllabes = Spinbox(from_=0, to=7, width=10, relief="ridge")
spinbox_nbsyllabes.grid(row=2, column=2, padx=3, pady=3)

check_nb_syllabes = IntVar()
checkbutton_syllabes = Checkbutton(text="# Syllabes", variable=check_nb_syllabes, bg="white", relief="ridge")
checkbutton_syllabes.grid(row=1, column=2, pady=3)

# Première lettre
prem_lettre_entry = Entry(width=16, relief="ridge")
prem_lettre_entry.grid(row=2, column=3, padx=3, pady=3)

check_1st_lettre = IntVar()
checkbutton_1st_lettre = Checkbutton(text="Première lettre", variable=check_1st_lettre, bg="white", relief="ridge")
checkbutton_1st_lettre.grid(row=1, column=3, padx=6, pady=3)

# Rareté avec scale

rarete_scale = Scale(from_=0, to=10, resolution=0.01, bg="white", troughcolor="white", relief="ridge",
                     orient=HORIZONTAL, length=100, sliderlength=8)
rarete_scale.grid(row=2, rowspan=2, column=4, padx=3, pady=9, sticky="n")

check_rarete_1 = IntVar()
checkbutton_rarete_1 = Checkbutton(text="Rareté précis", variable=check_rarete_1, bg="white", relief="ridge")
checkbutton_rarete_1.grid(row=1, column=4, padx=3, pady=3)

# Rareté avec radiobutton

check_rarete_2 = IntVar()
checkbutton_rarete_2 = Checkbutton(text="Rareté", variable=check_rarete_2, bg="white", relief="ridge")
checkbutton_rarete_2.grid(row=1, column=5, padx=3, pady=3)

radio_rarete = IntVar()
rarete_radio_frequent = Radiobutton(text="Mot fréquent", value=1, variable=radio_rarete)
rarete_radio_frequent.grid(row=2, column=5, padx=6, pady=6)
rarete_radio_rare = Radiobutton(text="Mot rare", value=2, variable=radio_rarete)
rarete_radio_rare.grid(row=3, column=5, sticky="w", padx=6)

window.mainloop()
