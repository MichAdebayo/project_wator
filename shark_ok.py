import random
import time

class Shark:
    def __init__(self, energy, position, compteur_tour=0):
        self.position = position
        self.energy = energy
        self.compteur_tour = compteur_tour

    def check_and_move(self):
    
        east_position = ((self.position[0]) % len(grid), (self.position[1]+1) % len(grid))
        west_position = ((self.position[0] )% len(grid), (self.position[1]-1 )% len(grid))
        north_position = ((self.position[0]-1 )% len(grid), (self.position[1])% len(grid))
        south_position = ((self.position[0]+1) % len(grid), (self.position[1]) % len(grid))

        position_voisine = [east_position, west_position, north_position, south_position]

    
        thon_possible = []
        mouv_possible = []

        for i in position_voisine :

            self.compteur_tour += 1 
            
            if 0 <= i[0] < len(grid) and 0 <= i[1] < len(grid[0]):  # limites de la grille
                controle_case = grid[i[0]][i[1]]

                if controle_case == "T" :
                    thon_possible.append(i)
                    
                elif controle_case == "." : 
                    mouv_possible.append(i)
            
            if thon_possible : 
                eat = random.choice(thon_possible)
                self.energy += 1
                self.position = eat
                event_1 = eat 
                grid[eat[0]][eat[1]] = "." 

            elif not thon_possible and mouv_possible :
                mouv = random.choice(mouv_possible) 
                event_1 = mouv
                self.energy -= 1
                self.position = mouv
                if event_1 and self.compteur_tour == 3 :
                    grid[eat[0]][eat[1]] = "S"
                    self.position = "S"
                    self.compteur_tour == 0



    def check_energy(self):
        if self.energy == 0:
            grid[self.position[0]][self.position[1]] = "." #si requin n'a plus d'energie il est remplacé par une case vide (cad mort)


grid = [
    [".", ".", ".", ".", "T"],
    [".", "T", ".", ".", "."],
    [".", ".", ".", "T", "."],
    [".", ".", ".", ".", "."],
    ["T", ".", ".", ".", "T"]
]

# initialisation requin avec energy et position
shark = Shark(energy=100, position=(0, 0)) #(ligne3,colonne 0)

while shark.energy > 0:
    
    # print("\033[H\033[J") #permet d'effacer chaque terminal
    print("\nPosition actuelle:", shark.position)
    print("Énergie actuelle:", shark.energy)
    print("Grille:")


    for ligne in grid:
        print("  ".join(ligne))


    time.sleep(1)

    
    ancienne_position = (shark.position[0], shark.position[1])
    shark.check_and_move()
    print(ancienne_position)
    print(shark.position)
    grid[ancienne_position[0]][ancienne_position[1]] = "." 
    grid[shark.position[0]][shark.position[1]] = "S"
    shark.check_energy()  

print("\nLe requin n'a plus d'énergie et ne peut plus se déplacer.")
print("Position finale:", shark.position)
