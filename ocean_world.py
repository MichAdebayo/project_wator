import random
import time

class Environment:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def init_grille(self):
        self.grille = [["." for _ in range(self.longueur)] for _ in range(self.largeur)]
        
        pop_sharks = 2
        pop_tunas = 6

        if pop_sharks > self.largeur * self.longueur:
            raise ValueError("Sharks population exceeds environment space")

        sharks_coord = []
        while pop_sharks > 0:
            x = random.randint(0, self.largeur - 1)
            y = random.randint(0, self.longueur - 1)
            if (x, y) not in sharks_coord:
                self.grille[x][y] = 'S'
                sharks_coord.append((x, y))
                pop_sharks -= 1

        tunas_coord = []
        while pop_tunas > 0:
            x = random.randint(0, self.largeur - 1)
            y = random.randint(0, self.longueur - 1)

            if (x, y) not in tunas_coord and (x, y) not in sharks_coord:
                self.grille[x][y] = 'T'
                tunas_coord.append((x, y))
                pop_tunas -= 1

        return self.grille, sharks_coord, tunas_coord


class Shark:
    def __init__(self, position: list | tuple, energy):
        
        self.position = position
        self.energy = energy
        self.baby_list = []
        self.compteur_tour = 0

    def check_and_move(self, grid):
        east_position = ((self.position[0]) % len(grid), (self.position[1] + 1) % len(grid[0]))
        west_position = ((self.position[0]) % len(grid), (self.position[1] - 1) % len(grid[0]))
        north_position = ((self.position[0] - 1) % len(grid), (self.position[1]) % len(grid[0]))
        south_position = ((self.position[0] + 1) % len(grid), (self.position[1]) % len(grid[0]))

        position_voisine = [east_position, west_position, north_position, south_position]

        thon_possible = []
        mouv_possible = []

        ancienne_position = (self.position[0], self.position[1])
        self.ancienne_position = ancienne_position

        for i in position_voisine:
            if 0 <= i[0] < len(grid) and 0 <= i[1] < len(grid[0]):
                controle_case = grid[i[0]][i[1]]

                if controle_case == ".":
                    mouv_possible.append(i)
                elif controle_case == "T":
                    thon_possible.append(i)

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

    def reproduce(self, grid):
        if self.compteur_tour == 5:
            baby_shark = Shark(self.position, 5)
            self.baby_list.append(baby_shark)
            self.compteur_tour = 0
        else:
            self.compteur_tour += 1

    def check_energy(self, grid):
        if self.energy == 0:
            grid[self.position[0]][self.position[1]] = "."
            return False
        return True


ma_planete = Environment(5, 5)
grid, shark_locations_on_grid, _ = ma_planete.init_grille()

shark = Shark(position=shark_locations_on_grid[0], energy=10)

while shark.check_energy(grid):
    print("Grille:")
    for ligne in grid:
        print("  ".join(ligne))

    shark.check_and_move(grid)
    shark.reproduce(grid)

    for baby in shark.baby_list:
        baby.check_and_move(grid)
        baby.reproduce(grid)

    time.sleep(1)

print("\nLe requin n'a plus d'énergie et ne peut plus se déplacer.")

