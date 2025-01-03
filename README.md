# V.O.I.L.A 😁
Visualisation Organisée Interactive de Listes d' Approfondissement <br>
[Rejoindre le discord](https://discord.gg/ZCyTjvSfQK)

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
- Python 3.x (en l'occurence 3.12)
- Transformers (Hugging Face) : Pour l’utilisation du modèle BART et le fine-tuning. (spécialisation de l'IA)
- Pandas : Pour la gestion des données CSV.
- ReportLab : Pour la génération de fichiers PDF.
- CustomTkinter : Pour l'interface utilisateur.

## Contribuer 🆕
Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, suivez ces étapes :

- Fork ce dépôt.
- Créez une nouvelle branche (git checkout -b feature/ma-fonctionnalite).
- **Lancez un fine-tunning** pour avoir le bon modèle. Dans le cas contraire, veillez à mettre ce modèle de résumé : ```facebook/bart-large-cnn```
- Faites vos modifications et committez (git commit -am 'FEATURE: Personalisation de la police d'écriture.').
- Poussez la branche (git push origin feature/ma-fonctionnalite).
- Ouvrez une Pull Request.

### Formatage des commits 🧐
Pour un projet plus clair, il est demander aux développeurs souhaitant contribuer au projet de respecter les différents formatages de commits ci-dessous. Il est égamement demandé à ce que les badges de PR soient respectés. Merci par avance.  

- **Ajout d'une fonctionnalité :** ```git commit -am 'FEATURE: courte description'```
- **Correction d'un bug :** ```git commit -am 'FIX: courte description'```
- **Correction typographique :** ```git commit -am 'TYPO: courte description'```
- **Autre :** ```git commit -am 'OTHER: courte description'```

 
