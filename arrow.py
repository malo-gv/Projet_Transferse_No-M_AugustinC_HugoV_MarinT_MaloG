import pygame
from constants import *
import math

def showArrow(window, arrowX, arrowY, arrowAngle):
    arrowImage = pygame.image.load("sprites character/arrow.png")
    arrowImage = pygame.transform.scale(arrowImage, (int(arrowImage.get_width() * 0.1), int(arrowImage.get_height() * 0.1)))
    arrowImage = pygame.transform.rotate(arrowImage, arrowAngle)
    arrowRectange = arrowImage.get_rect(center = (arrowX, arrowY))
    window.blit(arrowImage, arrowRectange.topleft)

def moveArrow(arrowX, arrowY, shootForce, arrowAngle, timerShoot):
    time = timerShoot
    arrowX = arrowX + (shootForce * math.cos(math.radians(arrowAngle)) * time)
    arrowY = arrowY + 0.5 * gravity * (time ** 2) - ((shootForce * math.sin(math.radians(arrowAngle))) * time)
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

"""def drawTrajectory(window, arrowX, arrowY, shootForce, arrowAngle, steps=50):
    for step in range(steps):
        t = step / 10.0  # Échelonner le temps pour obtenir des points plus rapprochés
        arrowX = arrowX + (shootForce * math.cos(math.radians(arrowAngle)) * t)
        arrowY = arrowY + 0.5 * gravity * (t ** 2) - ((shootForce * math.sin(math.radians(arrowAngle))) * t)
        pygame.draw.circle(window, (0, 0, 0), (int(arrowX), int(arrowY)), 2)"""