# README - Bow Battle

Ce jeu d'archer, intitulé "Bow Battle", met en scène un archer visant à mettre des flèches dans une cible. Le joueur contrôle un archer et doit ajuster l'angle et la puissance pour atteindre la cible avec précision.

## Installation

Pour exécuter ce jeu, assurez-vous d'avoir installé Python ainsi que les bibliothèques nécessaires. Vous pouvez installer les dépendances en exécutant :

"""pip install pygame"""

Assurez-vous également d'avoir les images nécessaires (fournies dans le dossier "sprites character" et "Images background") placées dans le répertoire approprié.
- Un fichier "arrow.png" dans le répertoire "sprites character" pour représenter la flèche.
- Les bibliothèques pygame et random doivent être installées.

Assurez-vous d'importer ce module dans votre fichier principal et d'appeler les fonctions nécessaires pour afficher et déplacer la flèche dans votre jeu.

## Utilisation

Pour lancer le jeu, exécutez le fichier `arrow.py`. Utilisez les touches suivantes pour jouer :

- Utilisez la touche DELETE pour afficher la flèche et la positionner.
- Appuyez sur ESPACE pour lancer la flèche vers la cible.

### Variables globales:
- `arrow_speed`: La vitesse de déplacement de la flèche.
- `distance_travelled`: La distance parcourue par la flèche depuis le début.
- `arrow_x`: La position horizontale de la flèche.
- `arrow_y`: La position verticale de la flèche.

## Fonctionnalités principales

- **Affichage de la flèche :** La fonction `show_arrow` permet d'afficher la flèche à l'écran avec une position et un angle donnés.
- **Déplacement de la flèche :** La fonction `move_arrow_straight` permet de déplacer la flèche dans une direction donnée à une vitesse spécifique.
- **Contrôle du personnage :** Le joueur peut contrôler l'angle et la puissance de la flèche pour viser la cible.
- **Gestion des événements :** Le jeu prend en charge les événements clavier pour permettre au joueur de déclencher le tir de la flèche.

### Bugs notables

- Certaines fonctions peuvent ne pas fonctionner correctement, veuillez consulter la section des fonctions principales pour plus de détails.

