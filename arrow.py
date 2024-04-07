import pygame
from constants import *
import math

def show_arrow(window, arrow_x, arrow_y, arrow_angle):
    arrow_image = pygame.image.load("sprites character/arrow.png")
    arrow_image = pygame.transform.scale(arrow_image, (int(arrow_image.get_width() * 0.1), int(arrow_image.get_height() * 0.1)))
    arrow_image = pygame.transform.rotate(arrow_image, arrow_angle)
    window.blit(arrow_image, (arrow_x, arrow_y))

def move_arrow_straight():
    global arrow_x
    arrow_x = arrow_x + arrow_speed
    return arrow_x

def rotate_arrow(dir):
    global arrow_angle
    if dir == "up":
        arrow_angle += 15
    if dir == "down":
        arrow_angle -= 15
    return arrow_angle

def calculate_arrow_angle(mouse_x, mouse_y):
    dx = mouse_x - arrow_x
    dy = mouse_y - arrow_y
    angle = math.degrees(math.atan2(dy, dx))
    return -angle

#def collision_cible:
# to do

#def afficher_trajectoire:
# to do (à la Angry Bird)

#def bouger_fleche_cloche:
# to do
# Utiliser formule physique pour prévoir la prochaine position de la flèche

