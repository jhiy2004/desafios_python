import pygame
import sys

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('dt.mp3')
pygame.mixer.music.play()
pygame.event.wait()
