import random
import time
from settings import *
print(Settings.nb_fishes)

class Environment:
    def __init__(self,largeur,longueur):
        self.largeur = largeur
        self.longueur = longueur

    def init_grille(self):
        self.grille = [["." for _ in range(self.longueur)] for _ in range(self.largeur)] # On initialise une grille vide
        population = round(Settings.nb_fishes *(self.longueur*self.largeur))

        pop_sharks = round(Settings.nb_sharks)
        pop_tunas = round(Settings.nb_tunas)


         
        sharks_coord = []
        while pop_sharks > 0:
            x = random.randint(0,self.longueur-1)
            y = random.randint(0,self.largeur-1)
            if (x,y) not in sharks_coord: # si les coor ne sont pas deja dans liste de shark_coor 
                self.grille[x][y] = 'S'         #Shark.Shark(10)
                sharks_coord.append((x,y))
                pop_sharks -= 1

        tunas_coord = []
        while pop_tunas > 0:
            x = random.randint(0,self.longueur-1)
            y = random.randint(0,self.largeur-1)

            if (x,y) not in tunas_coord and (x,y) not in sharks_coord:
                self.grille[x][y] = 'T'
                tunas_coord.append((x,y))
                pop_tunas -= 1

        return self.grille

    def afficher_grille(self):
        new_grille = [[0 for _ in range(self.longueur)] for _ in range(self.largeur)]
        for ligne in self.grille:        #affichage des élements de la grille
            print(ligne)
        print(self.longueur*3*'_')
        for ligne in new_grille:
            print(ligne)       
        print(self.longueur*3*'_')
        time.sleep(0.25)

# if __name__ == "__main__":

ma_planete = Environment(5,5)
b = ma_planete
print(b)
