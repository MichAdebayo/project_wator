# import random
# import time
# import settings

# class Environment:
#     def __init__(self,largeur,longueur):
#         self.largeur = largeur
#         self.longueur = longueur

#     def init_grid(self):
#         self.grid = [["." for _ in range(self.longueur)] for _ in range(self.largeur)] # On initialise une grille vide
#         # population = round(settings.taux_occupation *(self.longueur*self.largeur))

#         pop_sharks = 1 #round(settings.nb_sharks*population)
#         pop_tunas =  2 #round(settings.nb_tunas*population)

#         if pop_sharks > self.largeur*self.longueur:
#             raise ValueError("Sharks population exceeds environment space")
         
#         sharks_coord = []
#         while pop_sharks > 0:
#             x = random.randint(0,self.longueur-1)
#             y = random.randint(0,self.largeur-1)
#             if (x,y) not in sharks_coord:
#                 self.grid[x][y] =  'S' #Shark.Shark(energy=10, position=(x,y))         #Shark.Shark(energy=10, position=(x,y)) 
#                 sharks_coord.append((x,y))
#                 pop_sharks -= 1

#         tunas_coord = []
#         while pop_tunas > 0:
#             x = random.randint(0,self.longueur-1)
#             y = random.randint(0,self.largeur-1)

#             if (x,y) not in tunas_coord and (x,y) not in sharks_coord:
#                 self.grid[x][y] = 'T' #Fish.Fish(position=(x,y)) #'T'
#                 tunas_coord.append((x,y))
#                 pop_tunas -= 1

#         return self.grid
    
# class Fish:
#     def __init__(self, position):
#         self.position = position
#         self.move_counter = 0

#     def check_and_move(self, grid):

#         east_position = ((self.position[0]) % len(grid), (self.position[1]+1) % len(grid))
#         west_position = ((self.position[0] )% len(grid), (self.position[1]-1 )% len(grid))
#         north_position = ((self.position[0]-1 )% len(grid), (self.position[1])% len(grid))
#         south_position = ((self.position[0]+1) % len(grid), (self.position[1]) % len(grid))

#         position_voisine = [east_position, west_position, north_position, south_position]

#         empty_positions = [empty_pos for empty_pos in position_voisine if grid[empty_pos[0]][empty_pos[1]] == "."]
#         # tuna_positions = [tuna_pos for tuna_pos in position_voisine if grid[tuna_pos[0]][tuna_pos[1]] == "T"]
#         # shark_positions = [shark_pos for shark_pos in position_voisine if grid[shark_pos[0]][shark_pos[1]] == "S"]

#         if empty_positions:
#             new_position = random.choice(empty_positions)
#             grid[self.position[0]][self.position[1]] = "."
#             grid[new_position[0]][new_position[1]] = "T" 
#             self.position = new_position

#         # elif not empty_positions and tuna_positions:
#         #     new_position = random.choice(empty_positions)
#         #     grid[self.position[0]][self.position[1]] = "."
#         #     grid[new_position[0]][new_position[1]] = "T" 
#         #     self.position = new_position
        
#         self.move_counter += 1

#     def reproduce(self, grid):
#         if self.move_counter == 5:
#             new_fish = Fish(position=(self.position[0], self.position[1]))
#             l_fish.append(new_fish)
#             grid[self.position[0]][self.position[1]] = "T"  # Keep the fish in place
#             self.move_counter = 0  # Reset move counter


# # Initialize shark with energy and position
# env = Environment(5,5)
# grid = env.init_grid()

# fish = [pos for pos in grid if grid[pos[0]][pos[1]] == "T"]
# l_fish = [fish]


# while True:
#     # print("\033[H\033[J")  # Clear terminal
#     # print("\nCurrent position:", shark.position)
#     # print("Current energy:", shark.energy)
#     # print("Number of moves:", shark.compteur_tour)
#     print("Grid:")

#     for ligne in grid:
#         print("  ".join(ligne))
#     print()

#     # time.sleep(1)

#     fish.check_and_move(grid)
#     #print(shark.position)
#     fish.reproduce(grid)
#     fish.check_energy(grid)

#     time.sleep(1)

#     for fish in l_fish:
#         fish.check_and_move(grid)
#         fish.reproduce(grid)
#         fish.check_energy(grid)  

#     time.sleep(1)




    # class Shark(Fish):
    #     def __init__(self, energy, position, compteur_tour=1):
    #         super.__init__()
    #         self.position = position
    #         self.energy = energy
    #         self.compteur_tour = compteur_tour

    #     def check_and_move(self):

    #         east_position = ((self.position[0]) % len(grid), (self.position[1]+1) % len(grid))
    #         west_position = ((self.position[0] )% len(grid), (self.position[1]-1 )% len(grid))
    #         north_position = ((self.position[0]-1 )% len(grid), (self.position[1])% len(grid))
    #         south_position = ((self.position[0]+1) % len(grid), (self.position[1]) % len(grid))

    #         position_voisine = [east_position, west_position, north_position, south_position]

    #         thon_possible = []
    #         mouv_possible = []
    #         self.compteur_tour += 1

    #         ancienne_position = (shark.position[0], shark.position[1])
    #         self.ancienne_position = ancienne_position

    #         for i in position_voisine:

    #             if 0 <= i[0] < len(grid) and 0 <= i[1] < len(grid[0]):  # limites de la grille
    #                 controle_case = grid[i[0]][i[1]]

    #                 if controle_case == "T": 
    #                     thon_possible.append(i) 
    #                 elif controle_case == ".":
    #                     mouv_possible.append(i)

    #         if thon_possible: 
    #             eat = random.choice(thon_possible) 
    #             self.position = eat
    #             self.energy += 1
    #             grid[eat[0]][eat[1]] = "S"
    #             grid[self.ancienne_position[0]][self.ancienne_position[1]] = "."

    #         elif mouv_possible:
    #             mouv = random.choice(mouv_possible) 
    #             self.position = mouv
    #             self.energy -= 1
    #             grid[mouv[0]][mouv[1]] = "S"
    #             grid[self.ancienne_position[0]][self.ancienne_position[1]] = "."

    #     def reproduce(self):
    #         if self.compteur_tour == 5:
    #             grid[self.ancienne_position[0]][self.ancienne_position[1]] = "S" 
    #             grid[shark.position[0]][shark.position[1]] = "S"
    #             self.compteur_tour = 0

    #     def check_energy(self):
    #         if self.energy == 0:
    #             grid[self.position[0]][self.position[1]] = "." #si requin n'a plus d'energie il est remplacé par une case vide (cad mort)

# import random
# import time

# class Environment:
#     def __init__(self, largeur, longueur):
#         self.largeur = largeur
#         self.longueur = longueur

#     def init_grid(self):
#         self.grid = [["." for _ in range(self.longueur)] for _ in range(self.largeur)]
#         pop_sharks = 1
#         pop_tunas = 2

#         if pop_sharks > self.largeur * self.longueur:
#             raise ValueError("Sharks population exceeds environment space")

#         sharks_coord = []
#         while pop_sharks > 0:
#             x = random.randint(0, self.largeur - 1)
#             y = random.randint(0, self.longueur - 1)
#             if (x, y) not in sharks_coord:
#                 self.grid[x][y] = 'S'
#                 sharks_coord.append((x, y))
#                 pop_sharks -= 1

#         tunas_coord = []
#         while pop_tunas > 0:
#             x = random.randint(0, self.largeur - 1)
#             y = random.randint(0, self.longueur - 1)
#             if (x, y) not in tunas_coord and (x, y) not in sharks_coord:
#                 self.grid[x][y] = 'T'
#                 tunas_coord.append((x, y))
#                 pop_tunas -= 1

#         return self.grid

# class Fish:
#     def __init__(self, position, grid):
#         self.position = position
#         self.move_counter = 0
#         self.grid = grid

#     def check_and_move(self, grid):
#         east_position = (self.position[0], (self.position[1] + 1) % len(grid[0]))
#         west_position = (self.position[0], (self.position[1] - 1) % len(grid[0]))
#         north_position = ((self.position[0] - 1) % len(grid), self.position[1])
#         south_position = ((self.position[0] + 1) % len(grid), self.position[1])

#         position_voisine = [east_position, west_position, north_position, south_position]

#         empty_positions = [empty_pos for empty_pos in position_voisine if grid[empty_pos[0]][empty_pos[1]] == "."]

#         if empty_positions:
#             new_position = random.choice(empty_positions)
#             grid[self.position[0]][self.position[1]] = "."
#             grid[new_position[0]][new_position[1]] = "T"
#             self.position = new_position

#         self.move_counter += 1

#     def reproduce(self, grid):
#         if self.move_counter == 5:
#             new_fish = Fish(position=(self.position[0], self.position[1]))
#             l_fish.append(new_fish)
#             grid[self.position[0]][self.position[1]] = "T"
#             self.move_counter = 0

# class Shark(Fish):
#     def __init__(self, position, energy):
#         self.energy = energy
#         self.grid = grid
#         super().__init__(position)

#     def check_and_move(self, grid):
#         east_position = (self.position[0], (self.position[1] + 1) % len(grid[0]))
#         west_position = (self.position[0], (self.position[1] - 1) % len(grid[0]))
#         north_position = ((self.position[0] - 1) % len(grid), self.position[1])
#         south_position = ((self.position[0] + 1) % len(grid), self.position[1])

#         position_voisine = [east_position, west_position, north_position, south_position]

#         empty_positions = [empty_pos for empty_pos in position_voisine if grid[empty_pos[0]][empty_pos[1]] == "."]
#         tuna_positions = [tuna_pos for tuna_pos in position_voisine if grid[tuna_pos[0]][tuna_pos[1]] == "T"]

#         if tuna_positions:
#             new_position = random.choice(tuna_positions)
#             grid[self.position[0]][self.position[1]] = "."
#             grid[new_position[0]][new_position[1]] = "S"
#             self.position = new_position
        
#         if empty_positions:
#             new_position = random.choice(empty_positions)
#             grid[self.position[0]][self.position[1]] = "."
#             grid[new_position[0]][new_position[1]] = "S"
#             self.position = new_position

#         self.move_counter += 1

#     def reproduce(self, grid):
#         if self.move_counter == 12:
#             new_shark = Fish(position=(self.position[0], self.position[1]))
#             l_shark.append(new_shark)
#             grid[self.position[0]][self.position[1]] = "S"
#             self.move_counter = 0

#     def check_energy(self, grid):
#         if self.energy == 0:
#             grid[self.position[0]][self.position[1]] = "."
#             return True
#         return False 


# env = Environment(5, 5)
# grid = env.init_grid()

# l_fish = [Fish(position=(i, j)) for i in range(env.largeur) for j in range(env.longueur) if grid[i][j] == 'T']
# l_shark = [Shark(energy= 10, position=(i, j)) for i in range(env.largeur) for j in range(env.longueur) if grid[i][j] == 'S']

# while shark.check_energy(grid) > 0:

#     print("Grid:")
#     for ligne in grid:
#         print("  ".join(ligne))
#     print()

#     shark.check_and_move()
#     shark.reproduce()
#     shark.check_energy()
    
#     for shark in l_shark:
#         shark.check_and_move(grid)
#         shark.reproduce(grid)
#         shark.check_energy(grid)

#     fish.check_and_move()
#     fish.reproduce()

#     for fish in l_fish:
#         fish.check_and_move(grid)
#         fish.reproduce(grid)

#     time.sleep(1)


# import random
# import time

# class Environment:
#     def __init__(self, largeur, longueur):
#         self.largeur = largeur
#         self.longueur = longueur

#     def init_grid(self):
#         self.grid = [["." for _ in range(self.longueur)] for _ in range(self.largeur)]
#         pop_sharks = 1
#         pop_tunas = 2

#         if pop_sharks > self.largeur * self.longueur:
#             raise ValueError("Sharks population exceeds environment space")

#         sharks_coord = []
#         while pop_sharks > 0:
#             x = random.randint(0, self.largeur - 1)
#             y = random.randint(0, self.longueur - 1)
#             if (x, y) not in sharks_coord:
#                 self.grid[x][y] = 'S'
#                 sharks_coord.append((x, y))
#                 pop_sharks -= 1

#         tunas_coord = []
#         while pop_tunas > 0:
#             x = random.randint(0, self.largeur - 1)
#             y = random.randint(0, self.longueur - 1)
#             if (x, y) not in tunas_coord and (x, y) not in sharks_coord:
#                 self.grid[x][y] = 'T'
#                 tunas_coord.append((x, y))
#                 pop_tunas -= 1

#         return self.grid

# class Fish:
#     def __init__(self, position, grid):
#         self.position = position
#         self.move_counter = 0
#         self.grid = grid

#     def check_and_move(self):
#         east_position = (self.position[0], (self.position[1] + 1) % len(self.grid[0]))
#         west_position = (self.position[0], (self.position[1] - 1) % len(self.grid[0]))
#         north_position = ((self.position[0] - 1) % len(self.grid), self.position[1])
#         south_position = ((self.position[0] + 1) % len(self.grid), self.position[1])

#         position_voisine = [east_position, west_position, north_position, south_position]

#         empty_positions = [empty_pos for empty_pos in position_voisine if self.grid[empty_pos[0]][empty_pos[1]] == "."]

#         if empty_positions:
#             new_position = random.choice(empty_positions)
#             self.grid[self.position[0]][self.position[1]] = "."
#             self.grid[new_position[0]][new_position[1]] = "T"
#             self.position = new_position

#         self.move_counter += 1

#     def reproduce(self):
#         if self.move_counter == 5:
#             new_fish = Fish(position=(self.position[0], self.position[1]), grid=self.grid)
#             l_fish.append(new_fish)
#             self.move_counter = 0

# class Shark(Fish):
#     def __init__(self, position, energy, grid):
#         self.energy = energy
#         super().__init__(position, grid)

#     def check_and_move(self):
#         east_position = (self.position[0], (self.position[1] + 1) % len(self.grid[0]))
#         west_position = (self.position[0], (self.position[1] - 1) % len(self.grid[0]))
#         north_position = ((self.position[0] - 1) % len(self.grid), self.position[1])
#         south_position = ((self.position[0] + 1) % len(self.grid), self.position[1])

#         position_voisine = [east_position, west_position, north_position, south_position]

#         empty_positions = [empty_pos for empty_pos in position_voisine if self.grid[empty_pos[0]][empty_pos[1]] == "."]
#         tuna_positions = [tuna_pos for tuna_pos in position_voisine if self.grid[tuna_pos[0]][tuna_pos[1]] == "T"]

#         if tuna_positions:
#             new_position = random.choice(tuna_positions)
#             self.grid[self.position[0]][self.position[1]] = "."
#             self.grid[new_position[0]][new_position[1]] = "S"
#             self.energy += 1
#             self.position = new_position

#         elif empty_positions:
#             new_position = random.choice(empty_positions)
#             self.grid[self.position[0]][self.position[1]] = "."
#             self.grid[new_position[0]][new_position[1]] = "S"
#             self.energy -= 1
#             self.position = new_position

#         self.move_counter += 1

#     def reproduce(self):
#         if self.move_counter == 12:
#             new_shark = Shark(position=(self.position[0], self.position[1]), energy=10, grid=self.grid)
#             l_shark.append(new_shark)
#             self.move_counter = 0

#     def check_energy(self):
#         if self.energy <= 0:
#             self.grid[self.position[0]][self.position[1]] = "."
#             return True
#         return False 

# env = Environment(5, 5)
# grid = env.init_grid()

# l_fish = [Fish(position=(i, j), grid=grid) for i in range(env.largeur) for j in range(env.longueur) if grid[i][j] == 'T']
# l_shark = [Shark(position=(i, j), energy=10, grid=grid) for i in range(env.largeur) for j in range(env.longueur) if grid[i][j] == 'S']

# while l_shark and any(shark.check_energy() == False for shark in l_shark):

#     print("Grid:")
#     for ligne in grid:
#         print("  ".join(ligne))
#     print()

#     for shark in l_shark:
#         shark.check_and_move()
#         shark.reproduce()
#         shark.check_energy()

#     for fish in l_fish:
#         fish.check_and_move()
#         fish.reproduce()

#     time.sleep(1)






# import random
# import time

# class Fish:
#     def __init__(self, position, grid, compteur_tour=0):
#         self.grid = grid
#         self.position = position
#         self.compteur_tour = compteur_tour
#         self.name = 'T'  # Represents Tuna

#     def __str__(self):
#         return self.name

#     def check_and_move(self):
#         directions = [
#             ((self.position[0]) % len(self.grid), (self.position[1] + 1) % len(self.grid)),  # east
#             ((self.position[0]) % len(self.grid), (self.position[1] - 1) % len(self.grid)),  # west
#             ((self.position[0] - 1) % len(self.grid), (self.position[1]) % len(self.grid)),  # north
#             ((self.position[0] + 1) % len(self.grid), (self.position[1]) % len(self.grid))   # south
#         ]
        
#         self.compteur_tour += 1
#         ancienne_position = self.position
#         mouv_possible = [pos for pos in directions if 0 <= pos[0] < len(self.grid) and 0 <= pos[1] < len(self.grid[0]) and self.grid[pos[0]][pos[1]] == "."]
        
#         if mouv_possible:
#             new_position = random.choice(mouv_possible)
#             self.position = new_position
#             self.grid[new_position[0]][new_position[1]] = self.name
#             self.grid[ancienne_position[0]][ancienne_position[1]] = "."
#             print(f"Fish moved from {ancienne_position} to {new_position}")

#     def reproduce(self):
#         if self.compteur_tour >= 2:
#             self.compteur_tour = 0
#             new_fish_position = self.position
#             self.grid[new_fish_position[0]][new_fish_position[1]] = "T"
#             print(f"Fish reproduced at {new_fish_position}")


# class Shark(Fish):
#     def __init__(self, energy, position, grid, compteur_tour=0):
#         super().__init__(position, grid)
#         self.energy = energy
#         self.compteur_tour = compteur_tour
#         self.name = 'S'  # Represents Shark

#     def check_and_move(self):
#         directions = [
#             ((self.position[0]) % len(self.grid), (self.position[1] + 1) % len(self.grid)),  # east
#             ((self.position[0]) % len(self.grid), (self.position[1] - 1) % len(self.grid)),  # west
#             ((self.position[0] - 1) % len(self.grid), (self.position[1]) % len(self.grid)),  # north
#             ((self.position[0] + 1) % len(self.grid), (self.position[1]) % len(self.grid))   # south
#         ]
        
#         self.compteur_tour += 1
#         ancienne_position = self.position
#         thon_possible = [pos for pos in directions if self.grid[pos[0]][pos[1]] == "T"]
#         mouv_possible = [pos for pos in directions if self.grid[pos[0]][pos[1]] == "."]
        
#         if thon_possible:
#             eat_position = random.choice(thon_possible)
#             self.position = eat_position
#             self.energy += 1
#             self.grid[eat_position[0]][eat_position[1]] = "S"
#             self.grid[ancienne_position[0]][ancienne_position[1]] = "."
#             print(f"Shark ate fish at {eat_position} (moved from {ancienne_position})")
#         elif mouv_possible:
#             new_position = random.choice(mouv_possible)
#             self.position = new_position
#             self.energy -= 1
#             self.grid[new_position[0]][new_position[1]] = "S"
#             self.grid[ancienne_position[0]][ancienne_position[1]] = "."
#             print(f"Shark moved from {ancienne_position} to {new_position}")

#     def reproduce(self):
#         if self.compteur_tour >= 5:
#             self.compteur_tour = 0
#             new_shark_position = self.position
#             new_shark = Shark(energy=10, position=new_shark_position, grid=self.grid)
#             self.grid[new_shark_position[0]][new_shark_position[1]] = "S"
#             print(f"Shark reproduced at {new_shark_position}")

#     def check_energy(self):
#         if self.energy <= 0:
#             print(f"Shark at {self.position} has perished (energy depleted)")
#             self.grid[self.position[0]][self.position[1]] = "."
#             return True
#         return False


# class Ocean:
#     def __init__(self, largeur, longueur):
#         self.largeur = largeur
#         self.longueur = longueur
#         self.grid = [["." for _ in range(self.longueur)] for _ in range(self.largeur)]
#         self.instances_sharks = []
#         self.instances_fishes = []

#     def init_grille(self, pop_sharks=1, pop_tunas=3):
#         while pop_sharks > 0:
#             x, y = random.randint(0, self.longueur - 1), random.randint(0, self.largeur - 1)
#             if self.grid[x][y] == ".":
#                 new_shark = Shark(energy=10, position=(x, y), grid=self.grid)
#                 self.grid[x][y] = new_shark
#                 self.instances_sharks.append(new_shark)
#                 pop_sharks -= 1

#         while pop_tunas > 0:
#             x, y = random.randint(0, self.longueur - 1), random.randint(0, self.largeur - 1)
#             if self.grid[x][y] == ".":
#                 new_fish = Fish(position=(x, y), grid=self.grid)
#                 self.grid[x][y] = new_fish
#                 self.instances_fishes.append(new_fish)
#                 pop_tunas -= 1

#     def mouv_ok(self):
#         for shark in self.instances_sharks[:]:
#             shark.check_and_move()
#             shark.reproduce()
#             if shark.check_energy():
#                 self.instances_sharks.remove(shark)

#         for fish in self.instances_fishes[:]:
#             fish.check_and_move()
#             fish.reproduce()

#     def display_grid(self):
#         """Display the current state of the grid."""
#         for row in self.grid:
#             print(" ".join(str(cell) for cell in row))
#         print("\n")
#         time.sleep(1)
#     def run_simulation(self):
#         while self.instances_sharks and self.instances_fishes:
#             self.mouv_ok()
#             self.display_grid()
#             print(f"Sharks: {len(self.instances_sharks)}, Fish: {len(self.instances_fishes)}\n")
            
#         if not self.instances_sharks:
#             print("All sharks have perished. Fish dominate the ocean!")
#         elif not self.instances_fishes:
#             print("All fish have been eaten. Sharks dominate the ocean!")

        


# # Initialize and run the ocean simulation
# ocean = Ocean(5, 5)
# ocean.init_grille()
# ocean.run_simulation()



import random
import time

class Fish:
    def __init__(self, position, grid, compteur_tour=0):
        self.grid = grid
        self.position = position
        self.compteur_tour = compteur_tour
        self.name = 'T'  # Represents Tuna

    def __str__(self):
        return self.name

    def check_and_move(self):
        directions = [
            ((self.position[0]) % len(self.grid), (self.position[1] + 1) % len(self.grid)),  # east
            ((self.position[0]) % len(self.grid), (self.position[1] - 1) % len(self.grid)),  # west
            ((self.position[0] - 1) % len(self.grid), (self.position[1]) % len(self.grid)),  # north
            ((self.position[0] + 1) % len(self.grid), (self.position[1]) % len(self.grid))   # south
        ]
        
        self.compteur_tour += 1
        ancienne_position = self.position
        mouv_possible = [pos for pos in directions if 0 <= pos[0] < len(self.grid) and 0 <= pos[1] < len(self.grid[0]) and self.grid[pos[0]][pos[1]] == "."]
        
        if mouv_possible:
            new_position = random.choice(mouv_possible)
            self.position = new_position
            self.grid[new_position[0]][new_position[1]] = self
            self.grid[ancienne_position[0]][ancienne_position[1]] = "."
            print(f"Fish moved from {ancienne_position} to {new_position}")

    def reproduce(self):
        if self.compteur_tour >= 2:
            self.compteur_tour = 0
            # Find an empty neighboring cell for reproduction
            directions = [
                ((self.position[0]) % len(self.grid), (self.position[1] + 1) % len(self.grid)),  # east
                ((self.position[0]) % len(self.grid), (self.position[1] - 1) % len(self.grid)),  # west
                ((self.position[0] - 1) % len(self.grid), (self.position[1]) % len(self.grid)),  # north
                ((self.position[0] + 1) % len(self.grid), (self.position[1]) % len(self.grid))   # south
            ]
            empty_positions = [pos for pos in directions if self.grid[pos[0]][pos[1]] == "."]
            if empty_positions:
                baby_position = random.choice(empty_positions)
                new_fish = Fish(position=baby_position, grid=self.grid)
                self.grid[baby_position[0]][baby_position[1]] = new_fish
                print(f"Fish reproduced at {baby_position}")
                return new_fish
            return None


class Shark(Fish):
    def __init__(self, energy, position, grid, compteur_tour=0):
        super().__init__(position, grid)
        self.energy = energy
        self.compteur_tour = compteur_tour
        self.name = 'S'  # Represents Shark

    def check_and_move(self):
        directions = [
            ((self.position[0]) % len(self.grid), (self.position[1] + 1) % len(self.grid)),  # east
            ((self.position[0]) % len(self.grid), (self.position[1] - 1) % len(self.grid)),  # west
            ((self.position[0] - 1) % len(self.grid), (self.position[1]) % len(self.grid)),  # north
            ((self.position[0] + 1) % len(self.grid), (self.position[1]) % len(self.grid))   # south
        ]
        
        self.compteur_tour += 1
        ancienne_position = self.position
        thon_possible = [pos for pos in directions if self.grid[pos[0]][pos[1]] == "T"]
        mouv_possible = [pos for pos in directions if self.grid[pos[0]][pos[1]] == "."]
        
        if thon_possible:
            eat_position = random.choice(thon_possible)
            self.position = eat_position
            self.energy += 2  # Gain energy on eating fish
            self.grid[eat_position[0]][eat_position[1]] = "S"
            self.grid[ancienne_position[0]][ancienne_position[1]] = "."
            print(f"Shark ate fish at {eat_position} (moved from {ancienne_position})")
        elif mouv_possible:
            new_position = random.choice(mouv_possible)
            self.position = new_position
            self.energy -= 1  # Lose energy on a regular move
            self.grid[new_position[0]][new_position[1]] = "S"
            self.grid[ancienne_position[0]][ancienne_position[1]] = "."
            print(f"Shark moved from {ancienne_position} to {new_position}")

    def reproduce(self):
        if self.compteur_tour >= 5:
            self.compteur_tour = 0
            empty_positions = [pos for pos in directions if self.grid[pos[0]][pos[1]] == "."]
            if empty_positions:
                baby_position = random.choice(empty_positions)
                new_shark = Shark(energy=10, position=baby_position, grid=self.grid)
                self.grid[baby_position[0]][baby_position[1]] = new_shark
                print(f"Shark reproduced at {baby_position}")
                return new_shark
            return None

    def check_energy(self):
        if self.energy <= 0:
            print(f"Shark at {self.position} has perished (energy depleted)")
            self.grid[self.position[0]][self.position[1]] = "."
            return True
        return False


# Now create and run the simulation
def start_simulation(self):
    self.init_grille()
        
    # while self.instances_sharks and self.instances_fishes:
    while self.instances_sharks and self.instances_fishes:
        self.move()
            
        for line in self.grid:
            print(" ".join(str(cell) for cell in line))
        print("\n")

        print(len(self.instances_fishes), len(self.instances_sharks))

        # print(f"Sharks: {len(self.instances_sharks)}, Fish: {len(self.instances_fishes)}\n")

        time.sleep(1)

    # End of simulation summary
    # if not self.instances_sharks:
    #     print("All sharks have perished. Fish dominate the ocean!")
    # elif not self.instances_fishes:
    #     print("All fish have been eaten. Sharks dominate the ocean!")

# Initialize and run the ocean simulation
ocean = Ocean(5, 5)
ocean.start_simulation()
