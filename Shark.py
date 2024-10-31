import random
import time
from animals import Animals

class Shark:

    def __init__(self, energy, position, compteur_tour=1):
        self.position = position
        self.energy = energy
        self.compteur_tour = compteur_tour
        self.name = 'S'
        Animals.instances_sharks.append(self)

    def __str__(self):
        return self.name

    def check_and_move(self):

        east_position = ((self.position[0]) % len(grid), (self.position[1]+1) % len(grid))
        west_position = ((self.position[0] )% len(grid), (self.position[1]-1 )% len(grid))
        north_position = ((self.position[0]-1 )% len(grid), (self.position[1])% len(grid))
        south_position = ((self.position[0]+1) % len(grid), (self.position[1]) % len(grid))

        position_voisine = [east_position, west_position, north_position, south_position]

        thon_possible = []
        mouv_possible = []
        self.compteur_tour += 1

        ancienne_position = (shark.position[0], shark.position[1])
        self.ancienne_position = ancienne_position

        for i in position_voisine:

            if 0 <= i[0] < len(grid) and 0 <= i[1] < len(grid[0]):  # limites de la grille
                controle_case = grid[i[0]][i[1]]

                if controle_case == "T": 
                    thon_possible.append(i) 
                elif controle_case == ".":
                    mouv_possible.append(i)

        if thon_possible: 
            eat = random.choice(thon_possible) 
            self.position = eat
            self.energy += 1
            grid[eat[0]][eat[1]] = "S"
            grid[self.ancienne_position[0]][self.ancienne_position[1]] = "."

        elif mouv_possible:
            mouv = random.choice(mouv_possible) 
            self.position = mouv
            self.energy -= 1
            grid[mouv[0]][mouv[1]] = "S"
            grid[self.ancienne_position[0]][self.ancienne_position[1]] = "."

    # def reproduce(self):
    #     if self.compteur_tour == 5:
    #         grid[self.ancienne_position[0]][self.ancienne_position[1]] = "S" 
    #         grid[shark.position[0]][shark.position[1]] = "S"
    #         self.compteur_tour = 0

    def reproduce(self):
        if self.compteur_tour == 5:
            new_shark = Shark(energy=10, position=(self.ancienne_position[0],self.ancienne_position[1]))
            grid[self.ancienne_position[0]][self.ancienne_position[1]] = new_shark
            grid[shark.position[0]][shark.position[1]] = "S" 
            self.compteur_tour = 0
            l_shark.append(new_shark)


    def check_energy(self):
        if self.energy == 0:
            grid[self.position[0]][self.position[1]] = "." #si requin n'a plus d'energie il est remplacé par une case vide (cad mort)
            Animals.instances_sharks.remove(self)

# grid = [
#     [".", ".", ".", ".", "T"],
#     [".", "T", ".", ".", "."],
#     [".", ".", ".", "T", "."],
#     [".", ".", ".", ".", "."],
#     ["T", ".", ".", ".", "T"]
# ]

# # initialisation requin avec energy et position
# shark = Shark(energy=10, position=(0, 0)) #(ligne3,colonne 0)
# l_shark = [shark]

# while shark.energy > 0:
    
#     # print("\033[H\033[J") #permet d'effacer chaque terminal
#     print("\nPosition actuelle:", shark.position)
#     print("Énergie actuelle:", shark.energy)
#     print("Number of moves:", shark.compteur_tour)
#     print("Grille:")

#     for ligne in grid:
#         # print("  ".join(ligne))
#         print(ligne)

#     time.sleep(1)

#     for shark in l_shark:
#         shark.check_and_move()
#         # print(self.ancienne_position)
#         print(shark.position)
#         # grid[ancienne_position[0]][ancienne_position[1]] = "." 
#         # grid[shark.position[0]][shark.position[1]] = "S"
#         shark.reproduce()
#         shark.check_energy()  

# print("\nLe requin n'a plus d'énergie et ne peut plus se déplacer.")
# print("Position finale:", shark.position)