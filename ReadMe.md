# Projet Wator : Simulation de l'Écosystème Marin

Ce projet simule l'écosystème marin en modélisant les comportements des requins et des poissons dans une grille représentant l'océan. Le but est de comprendre les interactions entre prédateurs et proies et d'observer l'évolution d'une population dans un environnement dynamique.

![Texte alternatif](.assets/photo.webp)



## Table des Matières

1. [Contexte et Objectifs](#contexte-et-objectifs)
2. [Structure du Projet](#structure-du-projet)
3. [Fonctionnalités des Classes](#fonctionnalités-des-classes)
    - [Classe Fish](#classe-fish)
    - [Classe Shark](#classe-shark)
    - [Classe Ocean](#classe-océan)

4. [Lancement de la Simulation](#lancement-de-la-simulation)
5. [Notes supplémentaires](#notes-supplémentaires)
6. [Contributeurs](#contributeurs)
7. [Remerciements](#remerciements)

---

### Contexte et Objectifs

Le projet Wa-Tor est une simulation inspirée de la théorie des automates cellulaires, où une grille représente l'océan, et chaque cellule peut contenir un poisson, un requin ou rester vide. Les objectifs principaux de ce projet sont d'analyser :
- La dynamique des populations de proies (poissons) et de prédateurs (requins).
- L'impact de la reproduction et de la consommation d'énergie sur la survie des individus.

### Structure du Projet

Le projet est organisé en plusieurs fichiers :

- **fish.py** : Définition de la classe `Fish`, qui gère les comportements de base des poissons (déplacement, reproduction).
- **shark.py** : Définition de la classe `Shark`, qui hérite de la classe `Fish` et ajoute des fonctionnalités spécifiques aux requins (manger, gérer l'énergie).
- **environnement.py** : Gère la création et l'affichage de la grille océanique.
- **main.py** : Point d'entrée du programme pour initialiser la grille et lancer la simulation.
- **settings.py** : Contient les paramètres de la simulation, comme la proportion de la grille occupée par les poissons et les requins, et la taille de la grille en largeur et hauteur. 
- **requirements.txt** : Gère les dépendances (bibliothèques ou packages) nécessaires au bon fonctionnement d'un projet.


### Fonctionnalités des Classes

#### Classe `Fish`

- **Constructeur** : Initialise la position, le compteur de tours pour la reproduction, et le nom de représentation du poisson.
- **Méthodes principales** :
  - `check_and_move()` : Évalue les déplacements possibles autour du poisson et le fait bouger dans une cellule vide.
  - `reproduce()` : Si le poisson atteint un certain nombre de tours, crée un nouveau poisson à une position adjacente. 

[![Voir le code de fish.py](https://img.shields.io/badge/Class%20Fish-darkgreen)](fish.py) 

#### Classe `Shark`

- **Constructeur** : Initialise l'énergie en plus des attributs de la classe `Fish`.
- **Méthodes principales** :
  - `check_and_move()` : Le requin se déplace vers une cellule vide ou mange un poisson pour regagner de l'énergie.
  - `reproduce()` : Reproduit un nouveau requin lorsque le compteur de tours atteint une certaine valeur.
  - `check_energy()` : Vérifie si le requin doit être retiré de la grille en raison d'un manque d'énergie.

[![Voir le code de Shark.py](https://img.shields.io/badge/Class%20Shark-brown)](shark.py)  

#### Classe `Ocean`

La classe `Ocean` représente l'environnement dans lequel les poissons et les requins interagissent. Elle est responsable de la gestion de la grille représentant l'océan, de l'initialisation des poissons et des requins, ainsi que de l'exécution des actions dans chaque tour du simulateur.

- **Constructeur** : 

    - `width (int)`: Le nombre de lignes de la grille qui représente l'océan.

    - `height (int)`: Le nombre de colonnes de la grille qui représente l'océan.



- **Attributs de classe** : 
    - `grid (list)`: La grille qui représente l'océan, où chaque cellule peut être vide (représentée par un `.`), ou remplit par un poisson ou un requin.
    - `instances_fishes (list)`: Liste qui contient les instances des poissons présents dans l'océan.
    - `instances_sharks (list)`: Liste qui contient les instances des requins présents dans l'océan.



- **Méthodes principales** :

    - `init_grid()`: Initialise la grille en plaçant les poissons et les requins à des positions aléatoires, selon les listes d'instances données.
    - `move()`: Met à jour la grille en fonction des mouvements effectués par les poissons et les requins.
    - `start_simulation()`: Effectue les actions de tous les poissons et requins dans un tour (déplacements, reproduction, etc.).


[![Voir le code de Environnement.py](https://img.shields.io/badge/Class%20Ocean-darkblue)](environnement.py)  





### Lancement de la Simulation

Pour lancer la simulation, paramétrez le fichier `settings.py` en saisissant le taux d'occupation de la grille et la proportion de poissons et de requins.

Exécutez le fichier `main.py` qui initialise la grille, place les poissons et les requins, et exécute les itérations de simulation. La grille se met à jour à chaque tour selon les règles définies dans les classes `Fish` et `Shark`.


### Contributeurs

Ce projet a été imaginé et réalisé par :
- Sami Kabdani - Apprenant Tech IA
- Michael Adebayo - Apprenant Tech IA
- Antoine Delvoye - Apprenant Tech IA

### Remerciements

- A notre formateur, Benjamin Quinet, pour ses précieux conseils et son accompagnement tout au long de ce projet.

- A nos camarades, pour les échanges enrichissants qui nous ont permis de surmonter les obstacles rencontrés.

- A Safia, pour la confiance accordée, et à Simplon Hauts-de-France, pour le cadre d'apprentissage et les moyens mis à disposition permettant de concrétiser ce projet.