import pygame
from pygame.locals import *
from arrow import Arrow
from random import randint

pygame.init()

window = pygame.display.set_mode((1080, 720))

background = pygame.image.load("Images background/background v1.jpg").convert()
window.blit(background, (0,20))
base_ground = 440

character = pygame.image.load("sprites character/archer.png")
character = pygame.transform.scale(character, (int(character.get_width() * 0.25), int(character.get_height() * 0.25)))
character = pygame.transform.flip(character, True, False)
window.blit(character, (75, 440))

arrow_list = []

running = True
while running :
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()

    for arrow in arrow_list:
        if not ((arrow.x < 1080 and arrow.x > 0) or (arrow.y < 720 and arrow.y > 0)):
            arrow_list.pop(arrow.index(arrow)) #si sortie de l'écran = arrow supprimé


    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:



pygame.quit()
