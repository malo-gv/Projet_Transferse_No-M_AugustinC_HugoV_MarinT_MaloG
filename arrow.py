import pygame
from constants import *
import math

def showArrow(window, arrowX, arrowY, arrowAngle):
    arrowImage = pygame.image.load("sprites character/arrow.png")
    arrowImage = pygame.transform.scale(arrowImage, (int(arrowImage.get_width() * 0.1), int(arrowImage.get_height() * 0.1)))
    arrowImage = pygame.transform.rotate(arrowImage, arrowAngle)
    window.blit(arrowImage, (arrowX, arrowY))

def moveArrowStraight(arrowX, arrowSpeed):
    arrowX = arrowX + arrowSpeed
    return arrowX

def moveArrowParabolic(arrowY, arrowSpeed, gravity):
    arrowY += arrowSpeed * math.sin(arrowAngle) - gravity * 0.5
    return arrowY

def calculateArrowAngle(mouseX, mouseY):
    dx = mouseX - arrowX
    dy = mouseY - arrowY
    angle = math.degrees(math.atan2(dy, dx))
    return -angle

#def collision_cible:
# to do

#def afficher_trajectoire:
# to do (à la Angry Bird)

#def bouger_fleche_cloche:
# to do
# Utiliser formule physique pour prévoir la prochaine position de la flèche

