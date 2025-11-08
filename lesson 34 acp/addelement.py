import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game Screen")

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
BLACK = (0, 0, 0)

# Font settings
font = pygame.font.Font(None, 60)  # Default font, size 60
text = font.render("Welcome to My Game!", True, BLACK)  # Text surface
text_rect = text.get_rect(center=(screen_width/2, 100))  # Center position

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(WHITE)

    # Draw a rectangle (surface, color, [x, y, width, height])
    pygame.draw.rect(screen, BLUE, [300, 250, 200, 100])

    # Display text
    screen.blit(text, text_rect)

    # Update the screen
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()

