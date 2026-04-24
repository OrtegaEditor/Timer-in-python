
import tkinter as tk

    # Initialisation de la solution

fenetre = tk.Tk()
fenetre.title("Timer")
fenetre.geometry("800x500")

    # Cadre de gauche
cadre_gauche = tk.Frame(fenetre, bg="lightblue",width=400, height=500)
cadre_gauche.pack(side="left", fill="both", expand=True)

    # Titre
titre = tk.Label(cadre_gauche,text="Nouvelle",bg="lightblue", font=("Arial", 14,"bold"))

    # Cadre de droite
cadre_droit = tk.Frame(fenetre,bg="lightyellow", width=400, height=500)
cadre_droit.pack(side="right", fill="both", expand=True)

fenetre.mainloop()