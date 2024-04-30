import pygame
from pygame.locals import *
from arrow import *
from constants import *
from random import randint

pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, LENGTH))

background = pygame.image.load("Images background/background v1.jpg").convert()
window.blit(background, (0,20))


character = pygame.image.load("sprites character/archer.png")
character = pygame.transform.scale(character, (int(character.get_width() * 0.25), int(character.get_height() * 0.25)))
character = pygame.transform.flip(character, True, False)
window.blit(character, (75, baseGround))

target = pygame.image.load("sprites character/target3.png")
target = pygame.transform.scale(target, (int(target.get_width() * 0.23), int(target.get_height() * 0.23)))
window.blit(target, (850,440))

prevTime = pygame.time.get_ticks()
keys = pygame.key.get_pressed()

running = True
arrowMoving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()  # Pour obtenir les coord de la souris
            arrowAngle = calculate_arrow_angle(mouseX, mouseY) - 45
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                arrowMoving = True

    if arrowMoving:
        current_time = pygame.time.get_ticks()
        dt = (current_time - prevTime) / 1000.0
        arrowX = moveArrowStraight()
        prevTime = current_time

    window.blit(background, (0, 20))
    window.blit(character, (75, baseGround))
    window.blit(target, (850, 440))
    show_arrow(window, arrowX, arrowY, arrowAngle + arrowDirection)
    pygame.display.update()
    clock.tick(60)

pygame.quit()