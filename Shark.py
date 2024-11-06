import random
from Fish import *


class Shark(Fish):
    def __init__(self, energy, position, grid, instances_fishes, instances_sharks, compteur_tour=0):
        super().__init__(position, grid, instances_fishes)
        self.energy = energy
        self.compteur_tour = compteur_tour
        self.name = 'S'
        self.instances_fishes = instances_fishes 
        self.instances_sharks = instances_sharks

    def __str__(self):
        return self.name

    def check_and_move(self):
        directions = [
            ((self.position[0]) % len(self.grid), (self.position[1] + 1) % len(self.grid)),  # east
            ((self.position[0]) % len(self.grid), (self.position[1] - 1) % len(self.grid)),  # west
            ((self.position[0] + 1) % len(self.grid), (self.position[1]) % len(self.grid)),  # north
            ((self.position[0] - 1) % len(self.grid), (self.position[1]) % len(self.grid))   # south
        ]

        thon_possible = []
        self.move_possible = []
        move_impossible = []
        self.compteur_tour += 1

        ancienne_position = self.position
        self.ancienne_position = ancienne_position

        for pos in directions:
            if 0 <= pos[0] < len(self.grid) and 0 <= pos[1] < len(self.grid[0]):  # limits of the grid
                controle_case = self.grid[pos[0]][pos[1]]

                if isinstance(controle_case, Fish) and not isinstance(controle_case, Shark): 
                    thon_possible.append(pos)
                if controle_case == ".":
                    self.move_possible.append(pos)
                if isinstance(controle_case, Shark): 
                    move_impossible.append(pos)

        # print(f"Shark at {self.position} has possible moves: {move_possible}, fish to eat: {thon_possible}")
        
        if thon_possible:
            eat_position = random.choice(thon_possible)
            if eat_position and isinstance(self.grid[eat_position[0]][eat_position[1]], Fish) and not isinstance(self.grid[eat_position[0]][eat_position[1]], Shark):
                fish_to_eat = self.grid[eat_position[0]][eat_position[1]]
                self.instances_fishes.remove(fish_to_eat) 
                self.position = eat_position
                self.grid[eat_position[0]][eat_position[1]] = self
                # self.energy += 2
                self.grid[self.ancienne_position[0]][self.ancienne_position[1]] = "."      

        elif self.move_possible:
            new_move = random.choice(self.move_possible)
            self.position = new_move
            self.grid[self.position[0]][self.position[1]] = self
            self.energy -= 1  
            self.grid[ancienne_position[0]][self.ancienne_position[1]] = "."

        elif move_impossible and len(move_impossible) != 4:
            alt_move = random.choice(self.move_possible)
            self.position = alt_move
            self.grid[self.position[0]][self.position[1]] = self
            self.energy -= 1  
            self.grid[ancienne_position[0]][self.ancienne_position[1]] = "."

        else: 
            self.grid[ancienne_position[0]][ancienne_position[1]] = self

        # else:
        #     empty_cells = [(i, j) for i in range(len(self.grid)) for j in range(len(self.grid[0])) if self.grid[i][j] == "."]
        #     if empty_cells:
        #         random_empty_cell = random.choice(empty_cells)
        #         self.position = random_empty_cell
        #         self.grid[self.position[0]][self.position[1]] = self
        #         self.grid[ancienne_position[0]][ancienne_position[1]] = "."
        #         print(f"Shark teleported to empty cell at {random_empty_cell}")


    def reproduce(self):
        if self.compteur_tour == 15 and self.move_possible:
            # parent_shark_new_position = random.choice(self.mouv_possible)
            #if self.grid[self.ancienne_position[0]][self.ancienne_position[1]] == ".":
            baby_shark = Shark(energy=7, position=self.ancienne_position, instances_fishes = self.instances_fishes, instances_sharks=self.instances_sharks, grid=self.grid)
            self.instances_sharks.append(baby_shark)
            self.grid[self.ancienne_position[0]][self.ancienne_position[1]] = baby_shark
            self.compteur_tour = 0
        #     return baby_shark
        # return None

    def check_energy(self):
        if self.energy == 0:
            self.grid[self.position[0]][self.position[1]] = "."
            return True
        return False