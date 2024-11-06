# import random
# import time
# # from Shark import Shark
# from Fish import Fish

# class Ocean:
#     def __init__(self, largeur, longueur):
#         self.largeur = largeur
#         self.longueur = longueur
#         self.grid = [["." for _ in range(self.longueur)] for _ in range(self.largeur)]
#         # self.instances_sharks = []
#         self.instances_fishes = []

#     def init_grille(self):
#         # pop_sharks = 1 # round(Settings.nb_sharks)
#         pop_tunas = 1 # round(Settings.nb_tunas)

#         # while pop_sharks > 0:
#         #     x, y = random.randint(0, self.largeur - 1), random.randint(0, self.longueur - 1)
#         #     if self.grid[x][y] == ".":
#         #         new_shark = Shark(energy=10, position=(x, y), grid=self.grid, instances_fishes=self.instances_fishes)
#         #         self.grid[x][y] = new_shark
#         #         self.instances_sharks.append(new_shark)
#         #         pop_sharks -= 1

#         while pop_tunas > 0:
#             x, y = random.randint(0, self.largeur - 1), random.randint(0, self.longueur - 1)
#             if self.grid[x][y] == ".":
#                 new_fish = Fish(position=(x, y), instances_fishes = self.instances_fishes, grid=self.grid)
#                 self.grid[x][y] = new_fish
#                 self.instances_fishes.append(new_fish)
#                 pop_tunas -= 1


#     # def babies_lists(self):
    
#     #     self.new_sharks = []
#     #     self.new_fishes = []

#     #     # for shark in self.instances_sharks[:]:
#     #     #     baby_shark = shark.reproduce()
#     #     #     self.new_sharks.append(baby_shark)

#     #     for fish in self.instances_fishes[:]:
#     #         baby_fish = fish.reproduce()
#     #         self.new_fishes.append(baby_fish)
        
#     #     return self.new_sharks, self.new_fishes


#     def move(self):

#         for fish in self.instances_fishes[:]:
#             fish.check_and_move()
#             fish.reproduce()

#         # for shark in self.instances_sharks[:]:
#         #     shark.check_and_move()
            
#         #     shark.reproduce()

#         #     for s_baby in self.babies_lists[0]:
#         #         s_baby.check_and_move()
#         #         s_baby.reproduce()


#     def start_simulation(self):
#         self.init_grille()
            
#         # while self.instances_sharks and self.instances_fishes:
#         while self.instances_fishes:
#             self.move()
                
#             for line in self.grid:
#                 print(" ".join(str(cell) for cell in line))
#             print("\n")

#             print(len(self.instances_fishes)) #, len(self.instances_sharks))

#             # print(f"Sharks: {len(self.instances_sharks)}, Fish: {len(self.instances_fishes)}\n")

#             time.sleep(1)

#         # End of simulation summary
#         # if not self.instances_sharks:
#         #     print("All sharks have perished. Fish dominate the ocean!")
#         # elif not self.instances_fishes:
#         #     print("All fish have been eaten. Sharks dominate the ocean!")

# # Initialize and run the ocean simulation
# ocean = Ocean(5, 5)
# ocean.start_simulation()


import random
import time
from Fish import Fish
from Shark import Shark

class Ocean:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur
        self.grid = [["." for _ in range(self.longueur)] for _ in range(self.largeur)]
        self.instances_fishes = []
        self.instances_sharks = []
        self.start_simulation()

    def init_grille(self):
        pop_tunas = 5
        pop_sharks = 1

        while pop_tunas > 0:
            x, y = random.randint(0, self.largeur - 1), random.randint(0, self.longueur - 1)
            if self.grid[x][y] == ".":
                new_fish = Fish(position=(x, y), instances_fishes=self.instances_fishes, grid=self.grid)
                self.grid[x][y] = new_fish
                self.instances_fishes.append(new_fish)
                pop_tunas -= 1

        while pop_sharks > 0:
            x, y = random.randint(0, self.largeur - 1), random.randint(0, self.longueur - 1)
            if self.grid[x][y] == ".":
                new_shark = Shark(energy=7, position=(x, y), instances_fishes = self.instances_fishes, instances_sharks=self.instances_sharks, grid=self.grid)
                self.grid[x][y] = new_shark
                self.instances_sharks.append(new_shark)
                pop_sharks -= 1

    def move(self):
        for fish in self.instances_fishes:
            fish.check_and_move()
            fish.reproduce()
        
        for shark in self.instances_sharks:
            shark.check_and_move()
            shark.reproduce()
            shark.check_energy

    def start_simulation(self):
        self.init_grille()

        chronos = 0 + 1

        while True:
            self.move()


            for line in self.grid:
                print(" ".join(str(cell) for cell in line))
            print("\n")

            print("Chronos :", chronos)
            print("Sharks :" , len(self.instances_sharks))
            print("Fishes : ", len(self.instances_fishes))

            time.sleep(0.4)
            chronos += 1

            if not self.instances_sharks:
                print("All sharks have perished. Fish dominate the ocean!")
                # break
            elif not self.instances_fishes:
                print("All fish have been eaten. Sharks dominate the ocean!")
                # break

# Initialize and run the ocean simulation
ocean = Ocean(5, 5)

