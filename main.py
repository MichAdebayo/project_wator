from Environment import *
from Fish import *
from settings import *
from Shark import *


ma_planete = Environment(5,5)
grid = ma_planete.init_grille()
for line in grid:
    print("  ".join(line))
# ma_planete.afficher_grille()

