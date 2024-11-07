import random  # Provides functions for generating random numbers
from colorama import Fore, Style

class Fish:
    """
    Represents a fish in the ocean environment, capable of moving and reproducing.

    This class manages the fish's position within the grid, allows it to check possible movements, and handles reproduction after a certain number of turns.

    Args:
        position (tuple): The current position of the fish in the grid.
        grid (list): The grid representing the ocean environment.
        instances_fishes (list): A list to hold instances of fish in the ocean.
        turn_counter (int, optional): A counter to track the number of turns since the last reproduction. Defaults to 0.

    Attributes:
        grid (list): The grid representing the ocean environment.
        position (tuple): The current position of the fish in the grid.
        turn_counter (int): A counter to track the number of turns since the last reproduction.
        name (str): A character representing the fish.
        instances_fishes (list): A list to hold instances of fish in the ocean.

    Methods:
        check_and_move: Checks possible movements and updates the fish's position accordingly.
        reproduce: Allows the fish to reproduce if the conditions are met.

    Examples:
        fish = Fish(position=(0, 0), grid=grid, instances_fishes=instances_fishes)
        fish.check_and_move()
    """

    def __init__(self, position : tuple, grid : list, instances_fishes : list, turn_counter=0):
        """
        Initializes a new instance of the Fish class.

        This constructor sets the initial position, grid, and other attributes for the fish, including a counter for tracking turns and a name for representation.

        Args:
            position (tuple): The initial position of the fish in the grid.
            grid (list): The grid representing the ocean environment.
            instances_fishes (list): A list to hold instances of fish in the ocean.
            compteur_tour (int, optional): A counter to track the number of turns since the last reproduction. Defaults to 0.

        Returns:
            None
        """

        self.grid = grid
        self.position = position
        self.turn_counter = turn_counter
        self.name = f"{Fore.GREEN}F{Style.RESET_ALL}"
        self.instances_fishes = instances_fishes

    def __str__(self):
        """
        Returns a string representation of the fish.

        This method provides a simple way to represent the fish object as a string, returning its name for display purposes.

        Args:
            None

        Returns:
            str: The name of the fish.
        """

        return self.name


    def __str__(self):
        return self.name
    
    def check_and_move(self):
        """
        Evaluates possible movements for the fish and updates its position accordingly.

        This method checks the surrounding grid for available spaces and other fish, allowing the fish to move to an empty space or to a position occupied by another fish. It also updates the fish's position in the grid based on the chosen movement.

        Args:
            None

        Returns:
            None
        """

        # Define possible movement directions: east, west, north, south
        directions = [
            (self.position[0], (self.position[1] + 1) % len(self.grid[0])),  # east
            (self.position[0], (self.position[1] - 1) % len(self.grid[0])),  # west
            ((self.position[0] + 1) % len(self.grid), self.position[1]),  # north
            ((self.position[0] - 1) % len(self.grid), self.position[1])   # south
        ]

        # Initialize lists to track possible and impossible movements
        self.move_possible = []
        self.move_impossible = []

        # Increment the turn counter
        self.turn_counter += 1

        # Store the current position before attempting movement
        old_position = self.position
        self.old_position = old_position

        # Check each direction to classify possible movements
        for pos in directions:

            # Ensure the position is within the grid boundaries
            if 0 <= pos[0] < len(self.grid) and 0 <= pos[1] < len(self.grid[0]):  # limits of the grid
                control_case = self.grid[pos[0]][pos[1]]

                # If the cell is empty, add it to the possible movements
                if control_case == ".": 
                    self.move_possible.append(pos) 

                # If there's another fish, add to impossible movements (occupied)
                elif isinstance(control_case, Fish):
                    self.move_impossible.append(pos)

        # If there are possible moves, choose one randomly and update position
        if self.move_possible:
            new_move = random.choice(self.move_possible)
            self.position = new_move
            self.grid[self.position[0]][self.position[1]] = self  # Update grid with new position
            self.grid[old_position[0]][old_position[1]] = "."  # Mark old position as empty

        # If there are impossible moves and not all directions are blocked
        elif self.move_impossible and len(self.move_impossible) != 4:
            new_move = random.choice(self.move_impossible) 
            self.position = new_move
            self.grid[self.position[0]][self.position[1]] = self  # Move to the new position on the grid (without clearing old fish)
            self.grid[old_position[0]][old_position[1]] = "."  # Mark old position as empty

    
    def reproduce(self):
        """
        Allows the fish to reproduce if certain conditions are met.

        This method checks if the fish has reached the required number of turns and if there are possible movements available. If so, it creates a new fish at the previous position and resets the reproduction counter.

        Args:
            None

        Returns:
            None
        """

        # Check if the fish has reached the reproduction turn limit and has possible movements
        if self.turn_counter == 9 and self.move_possible:

            # Create a new fish instance at the previous position
            baby_fish = Fish(position=self.old_position, instances_fishes=self.instances_fishes, grid=self.grid)
            
            # Place the new fish in the grid at the previous position
            self.grid[self.old_position[0]][self.old_position[1]] = baby_fish
            
            # Add the new fish to the list of fish instances
            self.instances_fishes.append(baby_fish)
            
            # Reset the reproduction counter for the current fish
            self.turn_counter = 0

