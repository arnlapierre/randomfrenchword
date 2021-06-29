from tkinter import *


window = Tk()
window.title("Générateur de mot aléatoire")
window.minsize(width=500, height=400)
window.config(padx=40, pady=40)

# Label pour afficher le mot
affichage = Label(text="")
affichage.grid(row=0, column=1)

# Button
generer = Button(text="Générer")
generer.grid(row=3, column=1)

# Spinbox nombre de lettres
spinbox_nblettres = Spinbox(from_=0, to=10, width=5)
spinbox_nblettres.grid(row=2, column=0)

# Label pour nombre de lettres
nb_lettres = Label(text="# lettres")
nb_lettres.grid(row=1, column=0)


window.mainloop()