from Environment import *
import time
ma_planete = Environment(5,5)
grid = ma_planete.init_grille()
t= 0 
while t < 5:
    print(f"t = {t}")
    for line in grid:
        print(line)
    t +=1
    time.sleep(1)
        # print("  ".join(line))
    # ma_planete.afficher_grille()

