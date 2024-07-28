import pygame
import random

pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Hide and Seek')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def hide_and_seek():
    running = True
    count_to = 10  # Set counting to 10 seconds
    start_time = pygame.time.get_ticks()

    while running:
        screen.fill(WHITE)
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

        if elapsed_time >= count_to:
            print("Ready or not, here I come!")
            running = False

        pygame.display.flip()

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

hide_and_seek()
