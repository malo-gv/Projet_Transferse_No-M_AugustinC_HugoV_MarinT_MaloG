https://github.com/malo-gv/Projet_Transferse_NoeM_AugustinC_HugoV_MarinT_MaloG

# Jeu Bow Battle

## Description

Ce projet est un jeu de tir à l'arc développé en Python en utilisant la bibliothèque Pygame. Le but du jeu est de tirer des flèches sur une cible qui change de position après chaque tir réussi.

## Fonctionnalités

- **Affichage d'un environnement mystérieux dans lequel se déroule le jeu**
- **Calcul de la trajectoire de la flèche en fonction de l'angle de tir et de la force**
- **Affichage de la trajectoire prévue avant le tir**
- **Détection de la collision entre la flèche et la cible**
- **Détection de la collision entre la flèche et le sol ainsi que les bords de l'écran**
- **Mouvement aléatoire de la cible après chaque tir réussi**
- **Indicateur de puissance pour montrer la force du tir en cours de chargement**
- **Affichage de divers compteurs en lien avec le niveau du joueur**

## Structure du projet

- `main.py` : Le fichier principal qui initialise le jeu et gère la boucle principale du jeu.
- `arrow.py` : Contient les fonctions pour gérer l'affichage et le mouvement de la flèche, ainsi que pour vérifier les collisions avec la cible.
- `constants.py` : Définit les constantes utilisées dans le jeu, comme les positions initiales, les dimensions de la fenêtre ou encore la gravité.
- `target.py` : Contient la fonction pour déplacer la cible à une nouvelle position aléatoire après chaque tir réussi.

## Prérequis

- Python 3.x
- Pygame

## Utilisation

1. Assurez-vous que les fichiers suivants sont dans le même répertoire :
    - `main.py`
    - `arrow.py`
    - `constants.py`
    - `target.py`
      


2. Lancez le fichier main et profitez de cette expérience de tir en 2D !

## Contrôles

- **Utilisation de la souris pour viser :** Le jeu calcule automatiquement l'angle de tir basé sur la position de la souris.
- **Maintenez la touche `Espace` pour charger la puissance du tir :** Relâchez la touche `Espace` pour tirer la flèche.
