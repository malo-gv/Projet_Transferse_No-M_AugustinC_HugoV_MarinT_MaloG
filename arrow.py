import pygame
from constants import *
import math

def show_arrow(window, arrow_x, arrowY, arrow_angle):
    arrowImage = pygame.image.load("sprites character/arrow.png")
    arrowImage = pygame.transform.scale(arrowImage, (int(arrowImage.get_width() * 0.1), int(arrowImage.get_height() * 0.1)))
    arrowImage = pygame.transform.rotate(arrowImage, arrow_angle)
    window.blit(arrowImage, (arrow_x, arrowY))

def moveArrowStraight():
    global arrowX
    arrowX = arrowX + arrowSpeed
    return arrowX

def move_arrow_parabolic():
    global arrowX, arrow_y, arrowSpeed, gravity
    arrowX += arrowSpeed
    arrow_y += arrowSpeed * math.sin(arrow_angle) - gravity * 0.5
    return arrowX, arrow_y

def rotate_arrow(dir):
    global arrow_angle
    if dir == "up":
        arrow_angle += 15
    if dir == "down":
        arrow_angle -= 15
    return arrow_angle

def calculate_arrow_angle(mouseX, mouseY):
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

