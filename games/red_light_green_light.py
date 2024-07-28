import pygame
import random

pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Red Light Green Light')

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

def red_light_green_light():
    running = True
    while running:
        screen.fill(WHITE)
        light = random.choice(["Red light", "Green light"])
        print(light)
        color = GREEN if light == "Green light" else RED
        pygame.draw.circle(screen, color, (300, 200), 50)
        pygame.display.flip()
        pygame.time.delay(3000)

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

red_light_green_light()
