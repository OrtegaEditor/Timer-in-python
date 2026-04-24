
import tkinter as tk

    # Initialisation de la solution

fenetre = tk.Tk()
fenetre.title("Timer")
fenetre.geometry("800x500")

# Cadre de gauche
cadre_gauche = tk.Frame(fenetre, bg="lightblue",width=400, height=500)
cadre_gauche.pack(side="left", fill="both", expand=True)

    # Titre
titre = tk.Label(cadre_gauche,text="Nouvelle tache",bg="lightblue", font=("Arial", 14,"bold"))
titre.pack(fill="x", padx=10, pady=10)
    # Champ de saisie
        #Nom de la tache
label_nom = tk.Label(cadre_gauche, text="Nom Tâche", bg="white", font=("Arial", 11))
label_nom.pack(anchor="w", padx=20, pady=(20, 5))
        #
# Cadre de droite
cadre_droit = tk.Frame(fenetre,bg="lightyellow", width=400, height=500)
cadre_droit.pack(side="right", fill="both", expand=True)

fenetre.mainloop()