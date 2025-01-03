# V.O.I.L.A 😁
Visualisation Organisée Interactive de Listes d' Approfondissement

## Description 📜🖋
Ce projet Python permet de générer des fiches de révision sous forme de fichiers PDF à partir de cours (entrés manuellement par l'utilisateur). 
L'utilisateur peut choisir parmi trois styles prédéfinis de fiches, et le programme s'occupe de résumer et d'organiser le contenu sous forme de fiches structurées.

Le projet utilise un modèle de langage finement ajusté (BART) pour résumer les cours et les adapter aux besoins d'une révision efficace.

## Fonctionnalités 🚀
- **Génération de fiches de révision** : Choisissez parmi plusieurs styles de mise en page et générez des fiches en PDF.
- **Résumé automatique** : Le programme utilise un modèle de résumé basé sur le modèle BART pour condenser les informations du cours.
- **Personnalisation** : Trois styles prédéfinis de fiches, avec possibilité d'extension.
- **Format CSV** : Importez des cours sous format CSV pour le fine-tuning du modèle BART.

## Installation ⬇
1. Clonez ce dépôt sur votre machine :
   ```bash
   git clone https://github.com/cakihorse/V.O.I.L.A.git

## Technologies utilisées 👨‍💻
- Python 3.x
- Transformers (Hugging Face) : Pour l’utilisation du modèle BART et le fine-tuning.
- Pandas : Pour la gestion des données CSV.
- ReportLab : Pour la génération de fichiers PDF.
- Tkinter : Pour l'interface utilisateur (si implémentée).
- Contribuer
- Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, suivez ces étapes :

## Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, suivez ces étapes :

- Fork ce dépôt.
- Créez une nouvelle branche (git checkout -b feature/ma-fonctionnalite).
- Faites vos modifications et committez (git commit -am 'Ajoute une fonctionnalité').
- Poussez la branche (git push origin feature/ma-fonctionnalite).
- Ouvrez une Pull Request.

