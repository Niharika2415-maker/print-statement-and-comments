import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprites with Custom Color Change Event")

# Colors list
COLORS = [
    pygame.Color('red'),
    pygame.Color('green'),
    pygame.Color('blue'),
    pygame.Color('yellow'),
    pygame.Color('magenta'),
    pygame.Color('orange'),
    pygame.Color('cyan')
]

# Custom Event for Color Change
COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COLOR_CHANGE_EVENT, 1000)   # every 1 second

# Sprite rectangles
sprite1 = pygame.Rect(100, 150, 80, 80)
sprite2 = pygame.Rect(400, 150, 80, 80)

# Initial colors
sprite1_color = random.choice(COLORS)
sprite2_color = random.choice(COLORS)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle custom event
        if event.type == COLOR_CHANGE_EVENT:
            sprite1_color = random.choice(COLORS)
            sprite2_color = random.choice(COLORS)

    # Draw screen
    screen.fill("black")
    pygame.draw.rect(screen, sprite1_color, sprite1)
    pygame.draw.rect(screen, sprite2_color, sprite2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
