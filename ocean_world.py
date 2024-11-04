import random
import time
import settings

class Environment:
    def __init__(self,largeur,longueur):
        self.largeur = largeur
        self.longueur = longueur

    def init_grid(self):
        self.grid = [["." for _ in range(self.longueur)] for _ in range(self.largeur)] # On initialise une grille vide
        # population = round(settings.taux_occupation *(self.longueur*self.largeur))

        pop_sharks = 1 #round(settings.nb_sharks*population)
        pop_tunas =  2 #round(settings.nb_tunas*population)

        if pop_sharks > self.largeur*self.longueur:
            raise ValueError("Sharks population exceeds environment space")
         
        sharks_coord = []
        while pop_sharks > 0:
            x = random.randint(0,self.longueur-1)
            y = random.randint(0,self.largeur-1)
            if (x,y) not in sharks_coord:
                self.grid[x][y] =  'S' #Shark.Shark(energy=10, position=(x,y))         #Shark.Shark(energy=10, position=(x,y)) 
                sharks_coord.append((x,y))
                pop_sharks -= 1

        tunas_coord = []
        while pop_tunas > 0:
            x = random.randint(0,self.longueur-1)
            y = random.randint(0,self.largeur-1)

            if (x,y) not in tunas_coord and (x,y) not in sharks_coord:
                self.grid[x][y] = 'T' #Fish.Fish(position=(x,y)) #'T'
                tunas_coord.append((x,y))
                pop_tunas -= 1

        return self.grid
    
    class Fish:
        def __init__(self, position):
            self.position = position
            self.move_counter = 0

        def check_and_move(self, grid):
            x, y = self.position

            east_position = ((self.position[0]) % len(grid), (self.position[1]+1) % len(grid))
            west_position = ((self.position[0] )% len(grid), (self.position[1]-1 )% len(grid))
            north_position = ((self.position[0]-1 )% len(grid), (self.position[1])% len(grid))
            south_position = ((self.position[0]+1) % len(grid), (self.position[1]) % len(grid))

            position_voisine = [east_position, west_position, north_position, south_position]
            
            empty_positions = [empty_pos for empty_pos in position_voisine if grid[empty_pos[0]][empty_pos[1]] == "."]
            tuna_positions = [tuna_pos for tuna_pos in position_voisine if grid[tuna_pos[0]][tuna_pos[1]] == "T"]
            shark_positions = [shark_pos for shark_pos in position_voisine if grid[shar_pos[0]][tuna_pos[1]] == "T"]

            if empty_positions:
                new_position = random.choice(empty_positions)
                grid[self.position[0]][self.position[1]] = "."
                grid[new_position[0]][new_position[1]] = "T" 
                self.position = new_position

            elif not empty_positions and len(position_voisine)==4:
                new_mouv = random.choice() 
                self.position = new_mouv
                grid[new_mouv[0]][new_mouv[1]] = "T"
                grid[self.ancienne_position[0]][self.ancienne_position[1]] = "."

        def reproduce(self, grid):
            if self.move_counter == 7:
                grid[self.position[0]][self.position[1]] = "T"  # Keep the fish in place
                self.move_counter = 0  # Reset move counter
                
    class Shark:
        def __init__(self, energy, position, compteur_tour=1):
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

        def reproduce(self):
            if self.compteur_tour == 5:
                grid[self.ancienne_position[0]][self.ancienne_position[1]] = "S" 
                grid[shark.position[0]][shark.position[1]] = "S"
                self.compteur_tour = 0

        def check_energy(self):
            if self.energy == 0:
                grid[self.position[0]][self.position[1]] = "." #si requin n'a plus d'energie il est remplacé par une case vide (cad mort)