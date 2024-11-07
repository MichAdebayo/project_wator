import random  # Provides functions for generating random numbers
import time    # Provides time-related functions
import settings  # Custom settings module for configuration
from fish import Fish  # Importing the Fish class from the Fish module
from shark import Shark  # Importing the Shark class from the Shark module
import matplotlib.pyplot as plt # Provides graphical plotting functions

class Ocean:
    """
    Represents an ocean environment for simulating the interactions between fish and sharks.

    This class initializes the ocean grid, populates it with fish and sharks, and manages their movement and reproduction during the simulation.

    Args:
        width (int): The width of the ocean grid.
        height (int): The length of the ocean grid.

    Attributes:
        width (int): The width of the ocean grid.
        height (int): The length of the ocean grid.
        grid (list): A 2D list representing the ocean grid.
        instances_fishes (list): A list to hold instances of fish in the ocean.
        instances_sharks (list): A list to hold instances of sharks in the ocean.
    """
    def __init__(self, width : int, height : int) -> None:       
        """
        Initializes the Ocean class with specified dimensions and starts the simulation.

        This constructor sets up the ocean grid based on the provided width and length, initializes empty lists for fish and shark instances, and begins the simulation process.

        Args:
            largeur (int): The width of the ocean grid.
            longueur (int): The length of the ocean grid.

        Returns:
            None
        """

        # Set the width of the ocean grid
        self.width = width

        # Set the height of the ocean grid
        self.height = height

        # Initialize the ocean grid with empty cells represented by "."
        self.grid = [["." for _ in range(self.height)] for _ in range(self.width)]

        # Stores the list of the time_counter per loop
        self.time = []

        # Create an empty list to hold instances of fish in the ocean
        self.instances_fishes = []

        # Create an empty list to store the population of fishes per loop
        self.total_fishes = []

        # Create an empty list to hold instances of sharks in the ocean
        self.instances_sharks = []
        
        # Create an empty list to store the population of sharks per loop
        self.total_sharks = []

        # Initialize grid
        self.init_grid()


    def init_grid(self) -> None:
        """
        Initializes the ocean grid by populating it with a specified number of fish and sharks.

        This method randomly places fish and sharks in the grid, ensuring that they occupy empty spaces. It sets the initial population of fish and sharks.

        Args:
            None

        Returns:
            None
        """

        # Calculate the total population based on the occupation rate and grid size
        population = round(settings.occupation_rate * (self.height * self.width))

        # Determine the number of sharks and fish based on the calculated population
        pop_sharks = round(settings.number_of_sharks * population)
        pop_fish = round(settings.number_of_fish * population)

        # Check if the shark population exceeds the available space in the environment
        if pop_sharks > self.width * self.height:
            raise ValueError("Sharks population exceeds environment space")

        # Populate the grid with fish until the desired population is reached
        while pop_fish > 0:

            # Randomly select a position in the grid
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)

            # Check if the selected position is empty
            if self.grid[x][y] == ".":

                # Create a new fish instance and place it in the grid
                new_fish = Fish(position=(x, y), instances_fishes=self.instances_fishes, grid=self.grid)
                self.grid[x][y] = new_fish
                self.instances_fishes.append(new_fish)
                
                # Decrease the remaining fish to be placed
                pop_fish -= 1

        # Append the total number of fishes per loop to the total_fishes list
        self.total_fishes.append(len(self.instances_fishes)) 


        # Populate the grid with sharks until the desired population is reached
        while pop_sharks > 0:

            # Randomly select a position in the grid
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)

            # Check if the selected position is empty
            if self.grid[x][y] == ".":

                # Create a new shark instance and place it in the grid
                new_shark = Shark(energy=7, position=(x, y), instances_fishes=self.instances_fishes, instances_sharks=self.instances_sharks, grid=self.grid)
                self.grid[x][y] = new_shark
                self.instances_sharks.append(new_shark)

                # Decrease the remaining sharks to be placed
                pop_sharks -= 1

        # Append the total number of sharks per loop to the total_fishes list
        self.total_sharks.append(len(self.instances_sharks)) 


    def move(self) -> None:      
        """
        Updates the positions of fish and sharks in the ocean.

        This method iterates through all fish and sharks, allowing them to check their surroundings, move, reproduce, and for sharks to check their energy levels.

        Args:
            None

        Returns:
            None
        """

        # Iterate through all fish in the ocean
        for fish in self.instances_fishes:

            # Check the fish's surroundings and move to a new position if possible
            fish.check_and_move()

            # Allow the fish to reproduce if conditions are met
            fish.reproduce()

        # Iterate through all sharks in the ocean
        for shark in self.instances_sharks:

            # Check the shark's surroundings and move to a new position if possible
            shark.check_and_move()

            # Allow the shark to reproduce if conditions are met
            shark.reproduce()

            # Check the shark's energy level and determine if it can continue to survive
            shark.check_energy()


    def start_simulation(self) -> None: 
        """
        Begins the simulation of the ocean environment.

        This method initializes the grid, then continuously updates the state of the ocean by moving fish and sharks, printing the current state, and checking for the end conditions of the simulation.

        Args:
            None

        Returns:
            None
        """

        # Initialize the ocean grid with fish and sharks
        self.init_grid()

        # Start the simulation time counter
        chronos = 0 + 1

        # Add the total number of loops to the time list
        self.time.append(chronos)

        # Continue the simulation while there are sharks with energy
        while any(shark.check_energy() == False for shark in self.instances_sharks):
            
            # Update the positions and states of fish and sharks
            self.move()

            # Print the current state of the ocean grid
            for line in self.grid:
                print(" ".join(str(cell) for cell in line))
            print("\n")

            # Display the current simulation time and population counts
            print("Chronos :", chronos)
            print("Sharks :" , len(self.instances_sharks))
            print("Fishes : ", len(self.instances_fishes))
            self.total_sharks.append(len(self.instances_sharks))
            self.total_fishes.append(len(self.instances_fishes))
            self.time.append(chronos)

            # Pause the simulation for a short duration to visualize the changes
            time.sleep(0.0001)

            # Increment the simulation time counter
            chronos += 1

            # Check if all sharks have perished
            if not self.instances_sharks:
                print("All sharks have perished. Fish dominate the ocean!")
                break
            
            # Check if all fishes have been eaten
            elif not self.instances_fishes:
                print("All fishes have been eaten. Sharks dominate the ocean!")
                break

            # If time = 1000, stop!
            # if chronos ==1000:
            #     print("Time out")

                # break
        
        # Plot the final time series of the shark vs fish population after 1000 loops
        plt.plot(self.total_fishes, label="Fish Population")
        plt.plot(self.total_sharks, label="Shark Population")
        plt.xlabel("chronons")
        plt.ylabel("Population")
        plt.legend()
        plt.title("Evolution of Fish and Shark Populations Over Time")
        plt.show()

        # Plot the final time series of the shark vs fish population after 1000 loops
        ratio = [r / p if p != 0 else 0 for p, r in zip(self.total_fishes, self.total_sharks)]

        plt.figure(figsize=(10, 6))
        plt.plot(ratio, label="fish/sharks ratio", color="purple")
        plt.xlabel("Chronos")
        plt.ylabel("Ratio")
        plt.title("Evolution of sharks to fish ratio over time")
        plt.show()