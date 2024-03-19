import pygame

arrow_speed = 10  # Vitesse de déplacement de la flèche
distance_travelled = 0  # Distance parcourue par la flèche depuis le début
arrow_x = 172
arrow_y = 467
arrow_angle = -45

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
    if (dir == "up"):
        arrow_angle = arrow_angle + 25
    if (dir == "down"):
        arrow_angle = arrow_angle - 25
    return arrow_angle