import pygame
from random import randint

arrow_image = pygame.image.load("sprites character/arrow.png")

image = "sprites character/arrow.png"

center = (70, 400)

class Arrow :
   def __init__(self,x,y,image):
       self.x = x
       self.y = y
       self.image = image

    def shooting_arrow_straight_speed5(self):
        speed = 5
