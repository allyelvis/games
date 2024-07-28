import pygame
import random
import time
from gtts import gTTS
import playsound

pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Simon Says')

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Shapes
circle_radius = 50

def draw_circle(color, position):
    pygame.draw.circle(screen, color, position, circle_radius)

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('command.mp3')
    playsound.playsound('command.mp3')

def simon_says():
    commands = ["jump", "clap", "spin", "run in place"]
    running = True
    while running:
        screen.fill((0, 0, 0))
        command = random.choice(commands)
        color = random.choice([GREEN, RED, BLUE, YELLOW])
        draw_circle(color, (300, 200))
        pygame.display.flip()
        speak(f"Simon says {command}")
        time.sleep(3)

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

simon_says()
