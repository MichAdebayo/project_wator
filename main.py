from Environment import *

t= 0 
while t < 3:
    ma_planete = Environment(5,5)
    grid = ma_planete.init_grille()
    for line in grid:
        print(line)
    t +=1
        # print("  ".join(line))
    # ma_planete.afficher_grille()

