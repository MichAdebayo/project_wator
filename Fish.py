class Fish:

    def __init__(self, x, y, chronos):
        self.name = 'f'
        self.x = x 
        self.y = y
        self.chronos = chronos

        self.chronos = 1

    @classmethod
    def movement(cls, Environment):

        element_position = []
        grid = Environment.init_grille()
        print("Grid type:", type(grid))

        for row in range(len(grid)):
            element_position.extend(
                (row, column)
                for column in range(len(grid[row]))
                if grid[row][column] == 't'
            )
        print("Initial Fish Positions:", element_position)

        for element in element_position:
            row, column = element

            if grid[row][column] == 't':
                direction = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])  # right, down, left, up
                new_x, new_y = Environment.toroidal_permission(row + direction[0], column + direction[1])

                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    if grid[new_x][new_y] != 't' and grid[new_x][new_y] == 0:
                        grid[new_x][new_y] = 't'
                        grid[row][column] = 0  # Clear original position
                    elif grid[new_x][new_y] == 't':
                        pass

        # Output the updated grid for debugging
        print("Updated Grid:")
        for line in grid:
            print(line)