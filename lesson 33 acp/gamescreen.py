# Import the pygame library
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("My First Game Screen")

# Define colors (R, G, B)
white = (255, 255, 255)
blue = (50, 100, 255)

# Game loop
running = True
while running:
    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color
    screen.fill(blue)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
