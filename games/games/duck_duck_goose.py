import pygame
import random
from gtts import gTTS
import playsound

pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Duck Duck Goose')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Positions
children = [("Duck", (100, 200)), ("Duck", (200, 200)), ("Duck", (300, 200)), ("Duck", (400, 200))]
goose_position = random.choice(children)
children.append(("Goose", goose_position[1]))

def draw_children():
    for child in children:
        color = BLACK if child[0] == "Goose" else WHITE
        pygame.draw.circle(screen, color, child[1], 20)

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('command.mp3')
    playsound.playsound('command.mp3')

def duck_duck_goose():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_children()
        pygame.display.flip()
        speak("Duck")
        time.sleep(1)
        speak("Duck")
        time.sleep(1)
        speak("Goose")
        time.sleep(1)

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

duck_duck_goose()
