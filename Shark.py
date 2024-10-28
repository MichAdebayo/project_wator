import random
class Shark:
    def __init__(self, energy, position, compteur_thon_mangés) :
        self.position = position
        self.energy = 10
        self.compteur_thon_mangés = 0


    def check_and_move(self):
        east_position = (self.position[0]+1, self.position[1])
        west_position = (self.position[0]-1, self.position[1])
        north_position = (self.position[0], self.position[1]+1)
        south_position = (self.position[0], self.position[1]-1)

        position_voisine = [east_position, west_position, north_position, south_position]

    
        for i in position_voisine :
             
             controle_case = grid[i[0]][i[1]] 
             #compteur_thon_mangés = 0

             if controle_case == "." :
                  self.energy -= 1
                  self.position = i
                  self.compteur_thon_mangés += 1
                  break

             elif controle_case == "T":
                  self.energy += 1
                  self.position = i
                  break
             
             else : 
                  pass
             
    
    def energy(self) :
         if self.energy <= 0 :
            grid[self.position[0]][self.position[1]] = "."
    
    def reproduce(self):
         east_position = (self.position[0]+1, self.position[1])
         west_position = (self.position[0]-1, self.position[1])
         north_position = (self.position[0], self.position[1]+1)
         south_position = (self.position[0], self.position[1]-1)

         position_voisine = [east_position, west_position, north_position, south_position]

         for i in position_voisine :

            controle_case = grid[i[0]][i[1]] 
            if self.compteur_thon_mangés == 4 and controle_case == "." :
                self.position = i
                #A FINIR

         