import random
import settings
import time
from Shark import *
from Fish import *
from animals import Animals

class Environment:
    instances_sharks = []                   # On initialise une liste qui répertorie les sharks de la grille
    def __init__(self,largeur,longueur):
        self.largeur = largeur
        self.longueur = longueur
        # self.instances_sharks = []                   # On initialise une liste qui répertorie les sharks de la grille

    def init_grille(self):
        self.grille = [["." for _ in range(self.longueur)] for _ in range(self.largeur)] # On initialise une grille vide
        population = round(settings.taux_occupation *(self.longueur*self.largeur))

        pop_sharks = 1 #round(settings.nb_sharks*population)
        pop_tunas = round(settings.nb_tunas*population)

        if pop_sharks > self.largeur*self.longueur:
            raise ValueError("Sharks population exceeds environment space")
         
        sharks_coord = []
        while pop_sharks > 0:
            x = random.randint(0,self.longueur-1)
            y = random.randint(0,self.largeur-1)
            if (x,y) not in sharks_coord:
                new =  Shark(energy=10, position=(x,y))  #' #Shark.Shark(energy=10, position=(x,y))
                self.grille[x][y] =  new
                Animals.instances_sharks.append(new)

                sharks_coord.append((x,y))
                pop_sharks -= 1

        tunas_coord = []
        while pop_tunas > 0:
            x = random.randint(0,self.longueur-1)
            y = random.randint(0,self.largeur-1)

            if (x,y) not in tunas_coord and (x,y) not in sharks_coord:
                self.grille[x][y] = 'T' #Fish.Fish(position=(x,y)) #'T'
                tunas_coord.append((x,y))
                pop_tunas -= 1

        return self.grille, sharks_coord, tunas_coord