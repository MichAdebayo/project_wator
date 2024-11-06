import pygame
import random
import settings
from Fish import Fish
from Shark import Shark

CELL_SIZE = 30

class Fish:
    def __init__(self, position: tuple, grid: list, instances_fishes: list, turn_counter=0):
        self.grid = grid
        self.position = position
        self.turn_counter = turn_counter
        self.name = 'T'
        self.instances_fishes = instances_fishes

    def check_and_move(self):
        directions = [
            (self.position[0], (self.position[1] + 1) % len(self.grid[0])),
            (self.position[0], (self.position[1] - 1) % len(self.grid[0])),
            ((self.position[0] + 1) % len(self.grid), self.position[1]),
            ((self.position[0] - 1) % len(self.grid), self.position[1])
        ]

        self.move_possible = []
        self.move_impossible = []
        self.turn_counter += 1
        old_position = self.position

        for pos in directions:
            if 0 <= pos[0] < len(self.grid) and 0 <= pos[1] < len(self.grid[0]):
                controle_case = self.grid[pos[0]][pos[1]]
                if controle_case == ".":
                    self.move_possible.append(pos)
                elif isinstance(controle_case, Fish):
                    self.move_impossible.append(pos)

        if self.move_possible:
            new_move = random.choice(self.move_possible)
            self.position = new_move
            self.grid[self.position[0]][self.position[1]] = self
            self.grid[old_position[0]][old_position[1]] = "."
        elif self.move_impossible and len(self.move_impossible) != 4:
            new_move = random.choice(self.move_impossible)
            self.position = new_move
            self.grid[self.position[0]][self.position[1]] = self
            self.grid[old_position[0]][old_position[1]] = "."

    def reproduce(self):
        if self.turn_counter == 8 and self.move_possible:
            baby_fish = Fish(position=self.position, grid=self.grid, instances_fishes=self.instances_fishes)
            self.grid[self.position[0]][self.position[1]] = baby_fish
            self.instances_fishes.append(baby_fish)
            self.turn_counter = 0

class Shark(Fish):
    def __init__(self, energy, position, grid, instances_fishes, instances_sharks, turn_counter=0):
        super().__init__(position, grid, instances_fishes)
        self.energy = energy
        self.turn_counter = turn_counter
        self.name = 'S'
        self.instances_sharks = instances_sharks

    def check_and_move(self):
        directions = [
            ((self.position[0]) % len(self.grid), (self.position[1] + 1) % len(self.grid)),
            ((self.position[0]) % len(self.grid), (self.position[1] - 1) % len(self.grid)),
            ((self.position[0] + 1) % len(self.grid), (self.position[1]) % len(self.grid)),
            ((self.position[0] - 1) % len(self.grid), (self.position[1]) % len(self.grid))
        ]

        tuna_possible = []
        self.move_possible = []
        move_impossible = []
        self.turn_counter += 1
        old_position = self.position

        for pos in directions:
            if 0 <= pos[0] < len(self.grid) and 0 <= pos[1] < len(self.grid[0]):
                controle_case = self.grid[pos[0]][pos[1]]
                if isinstance(controle_case, Fish) and not isinstance(controle_case, Shark):
                    tuna_possible.append(pos)
                if controle_case == ".":
                    self.move_possible.append(pos)
                if isinstance(controle_case, Shark):
                    move_impossible.append(pos)
        if tuna_possible:
            eat_position = random.choice(tuna_possible)
            if eat_position and isinstance(self.grid[eat_position[0]][eat_position[1]], Fish):
                fish_to_eat = self.grid[eat_position[0]][eat_position[1]]
                self.instances_fishes.remove(fish_to_eat)
                self.position = eat_position
                self.grid[eat_position[0]][eat_position[1]] = self
                self.energy += 1
                self.grid[old_position[0]][old_position[1]] = "."
        elif self.move_possible:
            new_move = random.choice(self.move_possible)
            self.position = new_move
            self.grid[self.position[0]][self.position[1]] = self
            self.energy -= 1
            self.grid[old_position[0]][old_position[1]] = "."
        elif move_impossible and len(move_impossible) != 4:
            alt_move = random.choice(self.move_possible)
            self.position = alt_move
            self.grid[self.position[0]][self.position[1]] = self
            self.energy -= 1
            self.grid[old_position[0]][old_position[1]] = "."

    def reproduce(self):
        if self.turn_counter == 11 and self.move_possible:
            baby_shark = Shark(energy=5, position=self.position, grid=self.grid, instances_fishes=self.instances_fishes, instances_sharks=self.instances_sharks)
            self.instances_sharks.append(baby_shark)
            self.grid[self.position[0]][self.position[1]] = baby_shark
            self.turn_counter = 0

    def check_energy(self):
        if self.energy <= 0:
            self.instances_sharks.remove(self)
            self.grid[self.position[0]][self.position[1]] = "."

class Ocean:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [["." for _ in range(self.height)] for _ in range(self.width)]
        self.instances_fishes = []
        self.instances_sharks = []
        self.init_grid()

    def init_grid(self):
        population = round(settings.occupation_rate * (self.height * self.width))
        pop_sharks = round(settings.number_of_sharks * population)
        pop_fish = round(settings.number_of_fish * population)

        if pop_sharks > self.width * self.height:
            raise ValueError("Sharks population exceeds environment space")

        while pop_fish > 0:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if self.grid[x][y] == ".":
                new_fish = Fish(position=(x, y), grid=self.grid, instances_fishes=self.instances_fishes)
                self.grid[x][y] = new_fish
                self.instances_fishes.append(new_fish)
                pop_fish -= 1

        while pop_sharks > 0:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if self.grid[x][y] == ".":
                new_shark = Shark(energy=7, position=(x, y), grid=self.grid, instances_fishes=self.instances_fishes, instances_sharks=self.instances_sharks)
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
            shark.check_energy()

    def get_grid(self):
        return self.grid

def draw_grid(screen, grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if isinstance(grid[y][x], Fish):
                color = (0, 255, 0)
            elif isinstance(grid[y][x], Shark):
                color = (255, 0, 0)
            else:
                color = (255, 255, 255)
            
            # Print cell type for debugging
            print(f"Drawing cell at ({x}, {y}): {'Shark' if isinstance(grid[y][x], Shark) else 'Fish' if isinstance(grid[y][x], Fish) else 'Empty'}")

            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    pygame.init()
    screen_width = settings.width * CELL_SIZE
    screen_height = settings.height * CELL_SIZE
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("WATOR Simulation")

    ocean = Ocean(settings.width, settings.height)

    clock = pygame.time.Clock()
    running = True
    frame_count = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ocean.move()
        screen.fill((255, 255, 255))
        draw_grid(screen, ocean.get_grid())
        pygame.display.flip()

        clock.tick(4)
        frame_count += 1

        if frame_count > 500:
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
