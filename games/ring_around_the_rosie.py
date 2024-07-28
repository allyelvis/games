import pygame
import random

pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Ring Around the Rosie')

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

def ring_around_the_rosie():
    running = True
    while running:
        screen.fill(WHITE)
        pygame.draw.circle(screen, BLUE, (300, 200), 50)
        pygame.display.flip()
        pygame.time.delay(3000)

        print("They all fall down!")
        pygame.time.delay(1000)

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

ring_around_the_rosie()
