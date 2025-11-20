import pygame
import random
pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader – Part 1")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

# Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT-60))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Enemy Sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((35, 35))
        self.image.fill(RED)
        self.rect = self.image.get_rect(
            center=(random.randint(40, WIDTH-40), random.randint(40, HEIGHT-200))
        )

# Groups
player = Player()
player_group = pygame.sprite.Group(player)

enemies = pygame.sprite.Group()
for _ in range(7):
    enemies.add(Enemy())

all_sprites = pygame.sprite.Group(player, *enemies)

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    player_group.update()

    # Check collisions
    collided = pygame.sprite.spritecollide(player, enemies, True)
    score += len(collided)

    # Redraw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
