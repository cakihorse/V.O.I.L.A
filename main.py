import tkinter
import customtkinter
import threading
from sum import summarize


# Fonction pour résumer le texte
def summarize_text(max_char: int):
    # Récupérer le texte dans le champ de saisie
    res = field.get("1.0", "end").strip()
    sum_result = summarize(res, max_char)

    # Afficher le résumé dans la console et une boîte de dialogue
    print("Résumé généré:")
    print(sum_result)
    tkinter.messagebox.showinfo(title="Résumé", message=sum_result)


# Fonction pour gérer le thread sans bloquer l'interface
def button_callback():
    # Récupérer la valeur du slider
    max_char = int(slider.get())  # Obtenir la valeur actuelle du slider

    # Démarrer le résumé dans un thread pour éviter de bloquer l'interface
    thread = threading.Thread(target=summarize_text, args=(max_char,))
    thread.start()


# Fonction appelée lors du déplacement du slider
def slider_event(value):
    label.configure(text=f"Nombre maximum de caractères du résumé : {int(value)}")  # Met à jour le texte du label


# Création de l'application
app = customtkinter.CTk()
app.geometry("400x400")
app.title("Résumé de texte")

# Champ de texte pour entrer le texte à résumer
field = customtkinter.CTkTextbox(app, height=100)
field.pack(padx=20, pady=20)

# Label pour afficher la valeur du slider
label = customtkinter.CTkLabel(app, text="Nombre maximum de caractères du résumé : 0", fg_color="transparent")
label.pack(padx=20, pady=10)

# Slider pour ajuster une valeur
slider = customtkinter.CTkSlider(app, from_=10, to=500, command=slider_event)
slider.pack(padx=20, pady=10)
slider.set(100)  # Valeur par défaut du slider

# Bouton pour lancer le résumé
button = customtkinter.CTkButton(app, text="Résumer", command=button_callback)
button.pack(padx=20, pady=20)

# Lancer l'application
app.mainloop()
