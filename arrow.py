import pygame
from constants import *
import math

def showArrow(window, arrowX, arrowY, arrowAngle):
    arrowImage = pygame.image.load("sprites character/arrow.png")
    arrowImage = pygame.transform.scale(arrowImage, (int(arrowImage.get_width() * 0.1), int(arrowImage.get_height() * 0.1)))
    arrowImage = pygame.transform.rotate(arrowImage, arrowAngle)
    arrowRectange = arrowImage.get_rect(center = (arrowX, arrowY))
    window.blit(arrowImage, arrowRectange.topleft)

def moveArrow(initialArrowX, initialArrowY, shootForce, arrowAngle, timerShoot):
    time = timerShoot
    arrowX = initialArrowX + (shootForce * math.cos(math.radians(arrowAngle)) * time)
    arrowY = initialArrowY + 0.5 * gravity * (time ** 2) - ((shootForce * math.sin(math.radians(arrowAngle))) * time)
    return arrowX, arrowY

def calculateArrowAngle(mouseX, mouseY, arrowX, arrowY):
    dx = mouseX - arrowX
    dy = mouseY - arrowY
    angle = math.degrees(math.atan2(dy, dx))
    return -angle

def collisionCible(arrowX, arrowY, targetX, targetY):
    if (arrowX + 60 > targetX + 45 and arrowX + 60 < targetX + 103 ) and (arrowY + 60 > targetY + 45 and arrowY + 60 < targetY + 103):
        print("COLLISION")
        return True
    else :
        return False

#def afficher_trajectoire:
# to do (à la Angry Bird)