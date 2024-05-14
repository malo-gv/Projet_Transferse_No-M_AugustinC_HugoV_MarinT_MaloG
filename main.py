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

target = pygame.image.load("sprites character/bullseye.png")
target = pygame.transform.scale(target, (int(target.get_width() * 0.20), int(target.get_height() * 0.20)))
window.blit(target, (targetX,targetY))

prevTime = pygame.time.get_ticks()
keys = pygame.key.get_pressed()

running = True
arrowMoving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEMOTION and arrowMoving == False:
            mouseX, mouseY = pygame.mouse.get_pos()  # Pour obtenir les coord de la souris
            arrowAngle = calculateArrowAngle(mouseX, mouseY) - 45
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                arrowMoving = True

    if arrowMoving:
        currentTime = pygame.time.get_ticks()
        dt = (currentTime - prevTime) / 1000.0
        arrowX = moveArrowStraight(arrowX, arrowSpeed)
        """arrowYTravel = moveArrowParabolic(arrowY, arrowSpeed, gravity)"""
        prevTime = currentTime
        colisionActive = collision_cible(arrowX,arrowY,targetX,targetY)


    if colisionActive:
        arrowMoving = False

    window.blit(background, (0, 20))
    window.blit(character, (75, baseGround))
    window.blit(target, (targetX, targetY))
    showArrow(window, arrowX, arrowY, arrowAngle + arrowDirection)
    pygame.display.update()
    clock.tick(60)

pygame.quit()