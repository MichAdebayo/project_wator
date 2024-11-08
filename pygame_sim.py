import pygame
import os
import time
import matplotlib.pyplot as plt
import seaborn as sns
from environment import Ocean


# Initialize Pygame
pygame.init()

# Initialize the ocean simulation
ocean = Ocean(60, 40)

# Define cell size per cell
CELL_SIZE =  20

# Set up the display
WINDOW_WIDTH = ocean.width * CELL_SIZE
WINDOW_HEIGHT = ocean.height * CELL_SIZE
DATA_HEIGHT = 50  # Height reserved for displaying data
simulation_height = WINDOW_HEIGHT - DATA_HEIGHT  # Height for the simulation area
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ocean Simulation")

# Load images
shark_image = pygame.image.load(os.path.join("Assets", "shark.webp"))
fish_image = pygame.image.load(os.path.join("Assets", "fish.webp"))
background_image = pygame.image.load(os.path.join("Assets", "background_image.jpeg"))  # Replace with your static image path

# Scale the images to fit the grid cells
shark_image = pygame.transform.scale(shark_image, (32, 32))
fish_image = pygame.transform.scale(fish_image, (32, 32))
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))  # Scale background to fit window

# Button settings
BUTTON_WIDTH = 160  # Increased width
BUTTON_HEIGHT = 60  # Increased height
BUTTON_X = (WINDOW_WIDTH - BUTTON_WIDTH) // 2  # Center the button
BUTTON_Y = WINDOW_HEIGHT - BUTTON_HEIGHT - 80  # Move the button closer to the bottom

# Draw the buttons (outside the game loop)
start_button_font = pygame.font.Font(None, 24)
start_button_text = start_button_font.render("Start Wator", True, (0, 0, 0))  # Black text

# Loop counter settings
loop_counter = 0  # Initialize loop counter

# Lists to store population data
shark_population_history = []
fish_population_history = []

# Game loop
running = True
simulation_running = False
while running:
    if not simulation_running:
        # Display the starting screen with the static background and start button
        screen.blit(background_image, (0, 0))  # Draw the background image

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.Rect(BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)

        # Check if the mouse is hovering over the button
        if button_rect.collidepoint(mouse_pos):
            # Draw the button with hover effect (pressed down)
            pygame.draw.rect(screen, (50, 50, 50), button_rect)  # Dark gray for hover
            pygame.draw.rect(screen, (100, 100, 100), button_rect.inflate(-10, -10))  # Lighter gray for inner
        else:
            # Draw the button with normal 3D effect
            pygame.draw.rect(screen, (0, 0, 139), button_rect)  # Deep blue for normal
            pygame.draw.rect(screen, (100, 150, 200), button_rect.inflate(-10, -10))  # Lighter blue for inner

        # Draw the button text without background
        start_text_rect = start_button_text.get_rect(center=(BUTTON_X + BUTTON_WIDTH // 2, BUTTON_Y + BUTTON_HEIGHT // 2))
        screen.blit(start_button_text, start_text_rect)

        # Display quit message below the button
        quit_message_font = pygame.font.Font(None, 24)
        quit_message_text = quit_message_font.render("Press Esc to Mute Sound", True, (255, 255, 255))  # White text
        quit_text_rect = quit_message_text.get_rect(center=(WINDOW_WIDTH // 2, BUTTON_Y + BUTTON_HEIGHT + 30))  # Increased spacing
        screen.blit(quit_message_text, quit_text_rect)

        # Update the display
        pygame.display.flip()

        # Handle events for the starting screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(mouse_pos):
                    simulation_running = True
                    # Start playing audio when the simulation starts
                    pygame.mixer.music.load("Assets/water-bubbles-2.wav")  # Replace with your audio file path
                    pygame.mixer.music.play(-1)  # Play the audio in a loop

    else:
        # Clear the screen for the simulation
        screen.fill((0, 191, 255))  # Water color

        # Draw the grid
        cell_width = (WINDOW_WIDTH - 20) // ocean.width  # Width for the grid
        cell_height = simulation_height // ocean.height  # Height for the grid
        for x in range(ocean.width):
            for y in range(ocean.height):
                if (x, y) in [shark.position for shark in ocean.instances_sharks]:
                    screen.blit(shark_image, (x * cell_width, y * cell_height))
                elif (x, y) in [fish.position for fish in ocean.instances_fishes]:
                    screen.blit(fish_image, (x * cell_width, y * cell_height))
                else:
                    pygame.draw.rect(screen, (0, 191, 255), (x * cell_width, y * cell_height, cell_width, cell_height), 1)

        # Increment the loop counter
        loop_counter += 1

        # Store the current populations
        num_sharks = len(ocean.instances_sharks)  # Get the number of sharks
        num_fishes = len(ocean.instances_fishes)  # Get the number of fishes
        shark_population_history.append(num_sharks)
        fish_population_history.append(num_fishes)

        # Display the loop counter, number of sharks, and number of fishes horizontally
        # Prepare text for display
        info_font = pygame.font.Font(None, 24)
        chronos_text = info_font.render(f"Chronos: {loop_counter}", True, (0, 0, 0))  # Black text
        sharks_text = info_font.render(f"Sharks: {num_sharks}", True, (0, 0, 0))  # Black text
        fishes_text = info_font.render(f"Fishes: {num_fishes}", True, (0, 0, 0))  # Black text

        # Calculate positions to center the text horizontally
        total_width = chronos_text.get_width() + sharks_text.get_width() + fishes_text.get_width() + 40  # 40 for spacing
        start_x = (WINDOW_WIDTH - total_width) // 2  # Center the text

        # Position the text horizontally at the bottom of the screen
        text_y = WINDOW_HEIGHT - DATA_HEIGHT + 10  # Move down slightly
        screen.blit(chronos_text, (start_x, text_y))
        screen.blit(sharks_text, (start_x + chronos_text.get_width() + 20, text_y))  # Adjust x position for spacing
        screen.blit(fishes_text, (start_x + chronos_text.get_width() + sharks_text.get_width() + 40, text_y))  # Adjust x position for spacing

        # Update the display
        pygame.display.flip()

        # Handle events for the simulation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Allow quitting with Esc key
                    # Stop the audio when Esc is pressed
                    pygame.mixer.music.stop()  # Stop the music
                    simulation_ended = True  # Set the flag to indicate simulation has ended
                    
                running = False # Exit the simulation loop
                    

        # Update the simulation
        ocean.move()
        time.sleep(0.0001)

        

# After exiting the simulation loop, plot the population data
if simulation_ended:
                    
# Plot the population data using Matplotlib
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=shark_population_history, label='Sharks', color='blue')
    sns.lineplot(data=fish_population_history, label='Fishes', color='orange')
    plt.title("Evolution of Fish and Shark Populations Over Time", fontweight='bold', fontsize=13)
    plt.xlabel("Chronos (Loops)", fontsize=10)
    plt.ylabel("Population",  fontsize=10)
    plt.legend(loc="upper right", frameon=False)
    plt.grid(False)
    plt.show()  # Display the plot

# Quit Pygame
pygame.quit()
