import pandas as pd

# Exemple de données
data = {
    "text": [
        "Un atome est constitué d'un noyau autour duquel gravitent des électrons.",
        "La Révolution française a débuté en 1789 avec la prise de la Bastille.",
        "En biologie, la photosynthèse est le processus par lequel les plantes transforment la lumière du solei en glucose."
    ],
    "summary": [
        "TITRE: Atome. Un atome possède un noyau avec protons et neutrons, et des électrons autour.",
        "TITRE: Révolution française. La Révolution française a aboli la monarchie en 1789.",
        "TITRE: Photosynthèse. La photosynthèse permet aux plantes de convertir la lumière (soleil) en énergie (glucose)."
    ]
}

# Créer le DataFrame
df = pd.DataFrame(data)

# Sauvegarder en fichier CSV
df.to_csv('train.csv', index=False)
