import random
import time

class Shark:
    def __init__(self, energy, position):
        self.position = position
        self.energy = energy


    def check_and_move(self):
        east_position = (self.position[0] + 1, self.position[1])
        west_position = (self.position[0] - 1, self.position[1])
        north_position = (self.position[0], self.position[1] + 1)
        south_position = (self.position[0], self.position[1] - 1)

        position_voisine = [east_position, west_position, north_position, south_position]
        # random.choice(position_voisine)  

        for i in position_voisine:
            if 0 <= i[0] < len(grid) and 0 <= i[1] < len(grid[0]):  # limites de la grille
                controle_case = grid[i[0]][i[1]]

                if controle_case == ".":
                    self.energy -= 1
                    self.position = i
                    break

                elif controle_case == "T":
                    self.energy += 1
                    self.position = i
                    grid[i[0]][i[1]] = "."  # le thon est remplacé par une case vide
                    break

    def check_energy(self):
        if self.energy == 0:
            grid[self.position[0]][self.position[1]] = "." #si requin n'a plus d'energie il est remplacé par une case vide (cad mort)


grid = [
    ["T", ".", ".", ".", "T"],
    [".", "T", ".", ".", "."],
    [".", ".", ".", "T", "."],
    [".", ".", ".", ".", "."],
    ["T", ".", ".", ".", "T"]
]

# initialisation requin avec energy et position

shark = Shark(energy=10, position=(0, 2))
ancienne_position = (shark.position[0], shark.position[1])


# Boucle while tant que requin est vivant
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
print("Nombre de thons mangés:", shark.compteur_thon_mangés)
