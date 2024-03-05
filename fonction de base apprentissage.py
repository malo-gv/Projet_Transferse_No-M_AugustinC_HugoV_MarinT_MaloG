import pygame
from pygame.locals import *
from arrow import *
from random import randint
pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((1080, 720))

background = pygame.image.load("Images background/background v1.jpg").convert()
window.blit(background, (0,20))
base_ground = 440

character = pygame.image.load("sprites character/archer.png")
character = pygame.transform.scale(character, (int(character.get_width() * 0.25), int(character.get_height() * 0.25)))
character = pygame.transform.flip(character, True, False)
window.blit(character, (75, base_ground))

keys = pygame.key.get_pressed()

running = True
while running :
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                show_arrow(window)


    pygame.display.update()
    clock.tick(60)
pygame.quit()
