import random
import time
from Shark import *
from Fish import *
from animals import Animals
from settings import *

class Ocean:
    def __init__(self,largeur,longueur):
        self.largeur = largeur
        self.longueur = longueur

        self.grille = [["." for _ in range(self.longueur)] for _ in range(self.largeur)] # On initialise une grille vide
        self.instances_sharks = []                  # On initialise une liste qui répertorie les sharks de la grille
        self.instances_fishes = []

        self.init_grille()

    def init_grille(self):
        pop_sharks = 1 # round(Settings.nb_sharks)
        pop_tunas = 3 # round(Settings.nb_tunas)

        sharks_coord = []
        while pop_sharks > 0:
            x = random.randint(0,self.longueur-1)
            y = random.randint(0,self.largeur-1)
            if (x,y) not in sharks_coord:
                new_shark = Shark(energy=10, position=(x,y), grille = self.grille)
                self.grille[x][y] = new_shark
                self.instances_sharks.append(new_shark)

                sharks_coord.append((x,y))
                pop_sharks -= 1

        tunas_coord = []
        while pop_tunas > 0:
            x = random.randint(0,self.longueur-1)
            y = random.randint(0,self.largeur-1)

            if (x,y) not in tunas_coord and (x,y) not in sharks_coord:

                new_fish = Fish(position = (x,y))
                self.grille[x][y] = new_fish
                self.instances_fishes.append(new_fish)


                pop_tunas -= 1

        return self.grille, sharks_coord, tunas_coord

    def mouv_ok(self):

        for shark in self.instances_sharks :
            shark.check_and_move()
            shark.reproduce()
            shark.energy()
            print(shark.position)
            
        
        for fish in self.instances_fishes:
            fish.check_and_move()
            fish.reproduce()
            print(fish.position)


if __name__ == "__main__":
    my_ocean = Ocean(5,5)







