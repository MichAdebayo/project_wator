# Wa-Tor Simulation

## Overview

The WATOR simulation is a simple ecosystem model that simulates the interactions between two species: fish and sharks. The simulation is based on a grid where fish and sharks move, reproduce, and interact with each other. The goal is to observe how these species coexist and how their populations change over time.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Classes](#classes)
  - [Fish](#fish)
  - [Shark](#shark)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Grid-based Simulation**: The ocean is represented as a grid where each cell can be empty, contain a fish, or contain a shark.
- **Movement**: Fish and sharks can move in four directions (north, south, east, west) and wrap around the grid edges.
- **Reproduction**: Both fish and sharks can reproduce under certain conditions, increasing their populations.
- **Energy Management**: Sharks have an energy level that decreases with each move and increases when they eat fish. If their energy reaches zero, they are removed from the simulation.
- **Dynamic Interaction**: Sharks can eat fish, affecting the populations of both species.

## Installation

To run the WATOR simulation, clone the repository and install the required dependencies. You can use the following commands:

```bash
git clone https://github.com/yourusername/wator-simulation.git
cd wator-simulation

Make sure you have Python installed on your machine. You can run the simulation using Python 

3. Usage

To start the simulation, run the main.py file:
python [main.py](VALID_FILE)

You can modify the parameters such as the grid size, initial populations of fish and sharks, and other settings in the settings.py file.

Code Structure

The project consists of the following main files:

- main.py: The entry point of the simulation.
- settings.py: Configuration file for simulation parameters.
- Fish.py: Contains the Fish class, which defines the behavior of fish in the simulation.
- Shark.py: Contains the Shark class, which defines the behavior of sharks in the simulation.
- Environment.py: Manages the ocean environment and the interactions between fish and sharks.

Classes

Fish
The Fish class represents the fish in the simulation. It includes methods for movement, reproduction, and string representation.

- Attributes:
    - grid: The grid representing the ocean environment.
    - position: The current position of the fish in the grid.
    - turn_counter: A counter to track the number of turns since the last reproduction.
    - name: A character representing the fish.
    - instances_fishes: A list to hold instances of fish in the ocean.

- Methods:

    - check_and_move_or_eat(): Evaluates possible movements and eating opportunities for the fish.
    - reproduce(): Allows the fish to reproduce if conditions are met.

Shark
The Shark class represents the sharks in the simulation. It inherits from the Fish class and includes additional attributes and methods specific to sharks.

- Attributes:

    - energy: The current energy level of the shark.
    - turn_counter: A counter to track the number of turns since the last reproduction.
    - instances_sharks: A list to hold instances of sharks in the ocean.

- Methods:

    - check_and_move(): Evaluates possible movements for the shark, allowing it to eat fish or move to an empty space.
    - reproduce(): Allows the shark to reproduce if conditions are met.
    - check_energy(): Checks the shark's energy level and removes it from the grid if it reaches zero.
    
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the [Missing link] file for details.