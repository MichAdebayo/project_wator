import random

class Fish:
    def __init__(self, position, grid, instances_fishes, compteur_tour=0):
        self.grid = grid
        self.position = position
        self.compteur_tour = compteur_tour
        self.name = 'T'  
        self.instances_fishes = instances_fishes

    def __str__(self):
        return self.name

    def check_and_move(self):
        directions = [
            (self.position[0], (self.position[1] + 1) % len(self.grid[0])),  # east
            (self.position[0], (self.position[1] - 1) % len(self.grid[0])),  # west
            ((self.position[0] + 1) % len(self.grid), self.position[1]),  # north
            ((self.position[0] - 1) % len(self.grid), self.position[1])   # south
        ]

        self.mouv_possible = []
        self.mouv_impossible = []
        self.compteur_tour += 1

        ancienne_position = self.position
        self.ancienne_position = ancienne_position

        for pos in directions:
            if 0 <= pos[0] < len(self.grid) and 0 <= pos[1] < len(self.grid[0]):  # limits of the grid
                controle_case = self.grid[pos[0]][pos[1]]

                if controle_case == ".": 
                    self.mouv_possible.append(pos) 
                elif isinstance(controle_case, Fish):
                    self.mouv_impossible.append(pos)

        if self.mouv_possible:
            new_move = random.choice(self.mouv_possible)
            self.position = new_move
            self.grid[self.position[0]][self.position[1]] = self
            self.grid[ancienne_position[0]][ancienne_position[1]] = "."

        elif self.mouv_impossible and len(self.mouv_impossible) != 4:
            new_move = random.choice(self.mouv_impossible) 
            self.position = new_move
            self.grid[self.position[0]][self.position[1]] = self
            self.grid[ancienne_position[0]][ancienne_position[1]] = "."

    def reproduce(self):
        if self.compteur_tour == 5 and self.mouv_possible:
            baby_fish = Fish(position=self.ancienne_position, instances_fishes=self.instances_fishes, grid=self.grid)
            self.grid[self.ancienne_position[0]][self.ancienne_position[1]] = baby_fish
            self.instances_fishes.append(baby_fish)
            self.compteur_tour = 0
