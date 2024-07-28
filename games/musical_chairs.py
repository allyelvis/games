import pygame
import random

pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Musical Chairs')

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Chairs setup
chairs = 5
chair_radius = 30
positions = [(i * 100 + 50, 200) for i in range(chairs)]

def draw_chairs():
    for pos in positions:
        pygame.draw.circle(screen, BLUE, pos, chair_radius)
        pygame.draw.circle(screen, WHITE, pos, chair_radius - 5)

def musical_chairs():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_chairs()
        pygame.display.flip()
        pygame.time.delay(2000)

        if len(positions) > 1:
            out_chair = random.choice(positions)
            positions.remove(out_chair)
            pygame.draw.circle(screen, RED, out_chair, chair_radius)
            pygame.display.flip()
            pygame.time.delay(2000)
        else:
            print("Game over. Only one chair left!")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    exit()

musical_chairs()
