import random
import time
import settings
import Shark

class Environment:
    def __init__(self,largeur,longueur):
        self.largeur = largeur
        self.longueur = longueur

    def init_grille(self):
        self.grille = [[0 for i in range(self.longueur)] for j in range(self.largeur)] # On initialise une grille vide
        population = round(settings.taux_occupation *(self.longueur*self.largeur))


        pop_sharks = round(settings.nb_tunas*population)
        pop_tunas = round(settings.nb_tunas*population)
        if pop_sharks > self.largeur*self.longueur:
            raise ValueError("Sharks population exceeds environment space")

        sharks_coord = []
        while pop_sharks > 0:
            x = random.randint(0,self.longueur-1)
            y = random.randint(0,self.largeur-1)
            if (x,y) not in sharks_coord:
                self.grille[x][y] = 'S'         #Shark.Shark(10)
                sharks_coord.append((x,y))
                pop_sharks -= 1
            else:
                pass
                #print(f"il y a déja un requin ici ({(x,y)})")

        tunas_coord = []
        while pop_tunas > 0:
            x = random.randint(0,self.longueur-1)
            y = random.randint(0,self.largeur-1)
            if (x,y) not in tunas_coord and (x,y) not in sharks_coord:
                self.grille[x][y] = 'T'
                tunas_coord.append((x,y))
                pop_tunas -= 1
            else:
                pass
                #print(f"il y a déja un requin ou un thon ici ({(x,y)})")
        return self.grille, sharks_coord,tunas_coord

    def afficher_grille(self):
        new_grille = [[0 for i in range(self.longueur)] for j in range(self.largeur)]
        for ligne in self.grille:        #affichage des élements de la grille
            print(ligne)
        print(self.longueur*3*'_')
        for ligne in new_grille:
            print(ligne)       
        print(self.longueur*3*'_')
        time.sleep(0.25)

    def toroidal_permission(self, x, y):
        return x % self.largeur, y % self.longueur

ma_planete = Environment(5,5)
print(ma_planete.init_grille())
ma_planete.afficher_grille()

if __name__ == "__main__":

    ma_planete = Environment(5,5)
    b = ma_planete.init_grille()[1]
    print(b)
