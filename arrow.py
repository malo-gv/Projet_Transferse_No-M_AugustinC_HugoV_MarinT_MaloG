import pygame

def show_arrow(window):
    arrow_image = pygame.image.load("sprites character/arrow.png")
    arrow_image = pygame.transform.scale(arrow_image,(int(arrow_image.get_width() * 0.1), int(arrow_image.get_height() * 0.1)))
    arrow_image = pygame.transform.rotate(arrow_image, -45)

    window.blit(arrow_image, (172,467))
