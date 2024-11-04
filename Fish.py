import random
import time

class Fish:
    def __init__(self, position, compteur_tour=1):
        self.position = position
        self.compteur_tour = compteur_tour

    def check_and_move(self):

        east_position = ((self.position[0]) % len(grid), (self.position[1]+1) % len(grid))
        west_position = ((self.position[0] )% len(grid), (self.position[1]-1 )% len(grid))
        north_position = ((self.position[0]-1 )% len(grid), (self.position[1])% len(grid))
        south_position = ((self.position[0]+1) % len(grid), (self.position[1]) % len(grid))

        position_voisine = [east_position, west_position, north_position, south_position]

        mouv_possible = []
        mouv_impossible = []
        self.compteur_tour += 1

        ancienne_position = (fish.position[0], fish.position[1])
        self.ancienne_position = ancienne_position
        
        for i in position_voisine:

            if 0 <= i[0] < len(grid) and 0 <= i[1] < len(grid[0]):  # limites de la grille
                controle_case = grid[i[0]][i[1]]

                if controle_case == ".": 
                    mouv_possible.append(i) 
                elif controle_case == "T":
                    mouv_impossible.append(i)

        if mouv_possible: 
            move = random.choice(mouv_possible) 
            self.position = move
            grid[move[0]][move[1]] = "T"
            grid[self.ancienne_position[0]][self.ancienne_position[1]] = "."

        elif mouv_impossible and len(mouv_impossible)!=4:
            new_mouv = random.choice(mouv_possible) 
            self.position = new_mouv
            grid[new_mouv[0]][new_mouv[1]] = "T"
            grid[self.ancienne_position[0]][self.ancienne_position[1]] = "."

    def reproduce(self):
        if self.compteur_tour == 2:
            grid[ancienne_position[0]][ancienne_position[1]] = "T" 
            grid[fish.position[0]][fish.position[1]] = "T"
            self.compteur_tour = 0

grid = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]
]

# initialisation requin avec energy et position
fish = Fish(position=(0, 3)) #(ligne3,colonne 0)


while True:
    
    # print("\033[H\033[J") #permet d'effacer chaque terminal
    print("\nPosition actuelle:", fish.position)
    print("Number of moves:", fish.compteur_tour)
    print("Grille:")

    for ligne in grid:
        print("  ".join(ligne))

    time.sleep(1)

    
    ancienne_position = (fish.position[0], fish.position[1])
    fish.check_and_move()
    # print(ancienne_position)
    print(fish.position)
    # grid[ancienne_position[0]][ancienne_position[1]] = "." 
    # grid[fish.position[0]][fish.position[1]] = "T"
    fish.reproduce() 

print("Position finale:", fish.position)