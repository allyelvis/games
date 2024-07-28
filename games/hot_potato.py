import pygame
import random

pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Hot Potato')

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

def draw_potato():
    pygame.draw.circle(screen, RED, (300, 200), 20)

def hot_potato():
    children = ["Alice", "Bob", "Charlie", "Diana"]
    running = True
    while running:
        screen.fill(WHITE)
        draw_potato()
        pygame.display.flip()
        time.sleep(2)

        out = random.choice(children)
        children.remove(out)
        print(f"{out} is out!")
        pygame.time.delay(2000)

        if len(children) == 1:
            print(f"{children[0]} wins!")
            running = False

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

hot_potato()
