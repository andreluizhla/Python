import pygame
from colorama import init
init()


pygame.init()
pygame.mixer.music.load('Desafio021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('\033[4;36mTocando a música\033[m. Aproveite!')
