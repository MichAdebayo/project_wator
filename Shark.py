import random
from Fish import *
from colorama import Fore, Style


class Shark(Fish):
    """
    Represents a shark in the ocean environment, inheriting from the Fish class.

    This class manages the shark's energy, movement, and reproduction, allowing it to interact with its environment by moving, eating fish, and reproducing under certain conditions.

    Args:
        energy (int): The initial energy level of the shark.
        position (tuple): The initial position of the shark in the grid.
        grid (list): The grid representing the ocean environment.
        instances_fishes (list): A list to hold instances of fish in the ocean.
        instances_sharks (list): A list to hold instances of sharks in the ocean.
        turn_counter (int, optional): A counter to track the number of turns since the last reproduction. Defaults to 0.

    Attributes:
        energy (int): The current energy level of the shark.
        turn_counter (int): A counter to track the number of turns since the last reproduction.
        name (str): A character representing the shark.
        instances_fishes (list): A list to hold instances of fish in the ocean.
        instances_sharks (list): A list to hold instances of sharks in the ocean.

    Methods:
        __str__: Returns a string representation of the shark.
        check_and_move: Evaluates possible movements for the shark, allowing it to eat fish or move to an empty space.
        reproduce: Allows the shark to reproduce if certain conditions are met.
        check_energy: Checks the shark's energy level and removes it from the grid if it reaches zero.

    Examples:
        shark = Shark(energy=5, position=(0, 0), grid=grid, instances_fishes=instances_fishes, instances_sharks=instances_sharks)
        shark.check_and_move()
    """

    def __init__(self, energy :  int, position : tuple, grid : list, instances_fishes : list, instances_sharks : list, turn_counter : int = 0):
        """
        Initializes a new instance of the Shark class.

        This constructor sets the initial energy, position, and other attributes for the shark, allowing it to interact with its environment and other fish. It also initializes the turn counter for tracking reproduction.

        Args:
            energy (int): The initial energy level of the shark.
            position (tuple): The initial position of the shark in the grid.
            grid (list): The grid representing the ocean environment.
            instances_fishes (list): A list to hold instances of fish in the ocean.
            instances_sharks (list): A list to hold instances of sharks in the ocean.
            turn_counter (int, optional): A counter to track the number of turns since the last reproduction. Defaults to 0.

        Returns:
            None
        """

        super().__init__(position, grid, instances_fishes)
        self.energy = energy
        self.turn_counter = turn_counter
        self.name = f"{Fore.RED}S{Style.RESET_ALL}"
        self.instances_fishes = instances_fishes 
        self.instances_sharks = instances_sharks

    def __str__(self):
        """
        Returns a string representation of the shark.

        This method provides a simple way to represent the shark object as a string, returning its name for display purposes.

        Args:
            None

        Returns:
            str: The name of the shark.
        """

        return self.name

    def check_and_move(self):
        """
        Evaluates possible movements for the shark and updates its position accordingly.

        This method checks the surrounding grid for available spaces and fish to eat, allowing the shark to move to an empty space or to a position occupied by a fish. It also updates the shark's energy based on its actions and manages the grid representation.

        Args:
            None

        Returns:
            None
        """

        # Define possible movement directions: east, west, north, south
        directions = [
            ((self.position[0]) % len(self.grid), (self.position[1] + 1) % len(self.grid)),  # east
            ((self.position[0]) % len(self.grid), (self.position[1] - 1) % len(self.grid)),  # west
            ((self.position[0] + 1) % len(self.grid), (self.position[1]) % len(self.grid)),  # north
            ((self.position[0] - 1) % len(self.grid), (self.position[1]) % len(self.grid))   # south
        ]

        # Initialize lists to track possible fish positions and movement options
        fish_possible = []
        self.move_possible = []
        move_impossible = []

        # Increment the turn counter for the shark
        self.turn_counter += 1

        # Store the current position for later reference
        old_position = self.position
        self.old_position = old_position

        # Evaluate each possible direction for movement
        for pos in directions:

            # Check if the position is within the grid limits
            if 0 <= pos[0] < len(self.grid) and 0 <= pos[1] < len(self.grid[0]):  # limits of the grid
                control_case = self.grid[pos[0]][pos[1]]

                # If the cell contains a fish (not a shark), add it to possible fish positions
                if isinstance(control_case, Fish) and not isinstance(control_case, Shark): 
                    fish_possible.append(pos)

                # If the cell is empty, add it to possible movement options
                if control_case == ".":
                    self.move_possible.append(pos)

                # If the cell contains another shark, add it to impossible movements
                if isinstance(control_case, Shark): 
                    move_impossible.append(pos)

        # If there are possible fish positions, choose one to eat
        if fish_possible:
            eat_position = random.choice(fish_possible)

            # Check if the chosen position contains a fish
            if eat_position and isinstance(self.grid[eat_position[0]][eat_position[1]], Fish) and not isinstance(self.grid[eat_position[0]][eat_position[1]], Shark):
                fish_to_eat = self.grid[eat_position[0]][eat_position[1]]

                # Remove the eaten fish from the list of instances
                self.instances_fishes.remove(fish_to_eat) 

                # Update the shark's position to the location of the eaten fish
                self.position = eat_position
                self.grid[eat_position[0]][eat_position[1]] = self  # Place the shark in the new position
                self.energy += 1  # Increase the shark's energy
                self.grid[self.old_position[0]][self.old_position[1]] = "."  # Mark the old position as empty

        # If there are possible movements, choose one randomly
        elif self.move_possible:
            new_move = random.choice(self.move_possible)
            self.position = new_move  # Update the shark's position
            self.grid[self.position[0]][self.position[1]] = self  # Place the shark in the new position
            self.energy -= 1  # Decrease the shark's energy
            self.grid[old_position[0]][old_position[1]] = "."  # Mark the old position as empty

        # If there are impossible movements but not all directions are blocked
        elif move_impossible and len(move_impossible) != 4:
            alt_move = random.choice(directions)  # Choose an alternative move
            self.position = alt_move  # Update the shark's position
            self.grid[self.position[0]][self.position[1]] = self  # Place the shark in the new position
            self.energy -= 1  # Decrease the shark's energy
            self.grid[old_position[0]][old_position[1]] = "."  # Mark the old position as empty

        # If no movement is possible, keep the shark in its current position
        else: 
            self.grid[old_position[0]][old_position[1]] = self  # Ensure the shark remains in its old position


    def reproduce(self):
        """
        Allows the shark to reproduce if certain conditions are met.

        This method checks if the shark has reached the required number of turns and if there are possible movements available. If both conditions are satisfied, it creates a new shark at the previous position and resets the turn counter.

        Args:
            None

        Returns:
            None
        """

        # Check if the shark has reached the reproduction turn limit and has possible movements
        if self.turn_counter == 11 and self.move_possible:

            # Create a new baby shark instance at the previous position with initial energy
            baby_shark = Shark(energy=6, position=self.old_position, instances_fishes=self.instances_fishes, instances_sharks=self.instances_sharks, grid=self.grid)
            
            # Add the new baby shark to the list of shark instances
            self.instances_sharks.append(baby_shark)
            
            # Place the new baby shark in the grid at the previous position
            self.grid[self.old_position[0]][self.old_position[1]] = baby_shark
            
            # Reset the turn counter for the current shark
            self.turn_counter = 0


    def check_energy(self):
        """
        Checks the energy level of the shark and removes it from the grid if it has no energy left.

        This method verifies if the shark's energy has reached zero. If so, it removes the shark from the list of instances and marks its position in the grid as empty.

        Args:
            None

        Returns:
            bool: True if the shark was removed, False otherwise.
        """

        # Check if the shark's energy is zero and if it is still present in the grid
        if self.energy == 0 and isinstance(self.grid[self.position[0]][self.position[1]], Shark):
            
            # Store the reference to the shark that needs to be removed
            shark_to_remove = self.grid[self.position[0]][self.position[1]]
            
            # Remove the shark from the list of instances
            self.instances_sharks.remove(shark_to_remove)
            
            # Mark the shark's position in the grid as empty
            self.grid[self.position[0]][self.position[1]] = "."
            
            # Return True indicating the shark was removed
            return True

        # Return False indicating the shark is still alive
        return False

    