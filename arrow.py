import pygame

arrow_speed = 10  # Vitesse de déplacement de la flèche
distance_travelled = 0  # Distance parcourue par la flèche depuis le début
arrow_x = 172
arrow_y = 467


def show_arrow(window, arrow_x, arrow_y, angle):
    arrow_image = pygame.image.load("sprites character/arrow.png")
    arrow_image = pygame.transform.scale(arrow_image, (int(arrow_image.get_width() * 0.1), int(arrow_image.get_height() * 0.1)))
    arrow_image = pygame.transform.rotate(arrow_image, angle)
    window.blit(arrow_image, (arrow_x, arrow_y))

def move_arrow_straight():
    global arrow_x
    arrow_x = arrow_x + arrow_speed
    return arrow_x
