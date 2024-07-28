import pygame
import random
from gtts import gTTS
import playsound

pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Hide and Seek')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('count.mp3')
    playsound.playsound('count.mp3')

def hide_and_seek():
    running = True
    count_to = 10  # Set counting to 10 seconds
    start_time = pygame.time.get_ticks()

    while running:
        screen.fill(WHITE)
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

        if elapsed_time >= count_to:
            speak("Ready or not, here I come!")
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
