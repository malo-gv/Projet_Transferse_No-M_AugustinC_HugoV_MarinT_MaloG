import pygame
from constants import *
import random

pygame.init()
window = pygame.display.set_mode((WIDTH, LENGTH))
def afficher_cible_random():
    target = pygame.image.load("sprites character/bullseye.png")
    target = pygame.transform.scale(target, (int(target.get_width() * 0.23), int(target.get_height() * 0.23)))
    x = random.randint(800, 1000)
    y = random.randint(440, 700)
    window.blit(target, (x, y))
    return target

#def bouger_cible:
# to do

#def supprimer_cible:
# to do
