from tkinter import *
from class_mot_aléatoire import MotAléatoire

# Paramètres de la fenêtre
window = Tk()
window.title("Générateur aléatoire de mots")
window.geometry("500x320")
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

    # Fréquence aux bornes
    if radio_rarete.get() == 3 and (check_freq_ut.get() == 1 or check_freq_lt.get() == 1):
        if check_freq_ut.get() == 1:
            freq_ut_var = freq_upper_than_spin.get()
        else:
            freq_ut_var = None
        if check_freq_lt.get() == 1:
            freq_lt_var = freq_lower_than_spin.get()
        else:
            freq_lt_var = None

    # Cas ou le radio est sélectionné, mais pas les checkbox
    if radio_rarete.get() == 3 and (check_freq_ut.get(), check_freq_lt.get()) == (0, 0):
        freq_ut_var = None
        freq_lt_var = None

    # Rareté
    # Mot fréquent
    if radio_rarete.get() == 1:
        freq_ut_var = 10
        freq_lt_var = None

    # Mot rare
    if radio_rarete.get() == 2:
        freq_lt_var = 0.02
        freq_ut_var = None

    affichage.config(text=MotAléatoire().set_all(cat=cat_var, nblettres=nb_lettres_var,
                                                 premlettre=prem_lettre_var,
                                                 nbsyllabes=nb_syllabes_var,
                                                 freq_ut=freq_ut_var,
                                                 freq_lt=freq_lt_var))


# Button
generer = Button(text="Générer", command=generer_mot, bg="white")
generer.grid(row=7, column=1, padx=3, pady=3)

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

# Fréquence

# Fréquence Label
freq_label = Label(text="Options de fréquence")
freq_label.grid(row=3, column=0, columnspan=2, sticky="sw", pady=8)


# Scale "upper than"
freq_upper_than_spin = Spinbox(from_=0.00, to=1000, width=10, bg="white", relief="ridge")
freq_upper_than_spin.grid(row=6, column=0, padx=3, pady=9)

check_freq_ut = IntVar()
checkbutton_freq_ut = Checkbutton(text="Plus que : ", variable=check_freq_ut, bg="white", relief="ridge")
checkbutton_freq_ut.grid(row=5, column=0, padx=3, pady=3)

# Scale "lower than"
freq_lower_than_spin = Spinbox(from_=0.00, to=1000, width=10, bg="white", relief="ridge")
freq_lower_than_spin.grid(row=6, column=1, padx=3, pady=9)

check_freq_lt = IntVar()
checkbutton_freq_lt = Checkbutton(text="Moins que : ", variable=check_freq_lt, bg="white", relief="ridge")
checkbutton_freq_lt.grid(row=5, column=1, padx=3, pady=3)


# Rareté avec radiobutton

radio_rarete = IntVar()
rarete_radio_frequent = Radiobutton(text="Mot fréquent", value=1, variable=radio_rarete)
rarete_radio_frequent.grid(row=4, column=2, padx=6, pady=6)
rarete_radio_rare = Radiobutton(text="Mot rare", value=2, variable=radio_rarete)
rarete_radio_rare.grid(row=4, column=3, sticky="w", padx=6)
rarete_radio_intervalle = Radiobutton(text="Ajuster manuellement l'intervalle", value=3, variable=radio_rarete)
rarete_radio_intervalle.grid(row=4, column=0, columnspan=2, sticky="w", padx=6)

window.mainloop()
