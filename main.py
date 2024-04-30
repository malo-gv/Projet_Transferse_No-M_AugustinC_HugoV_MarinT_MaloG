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
window.blit(character, (75, base_ground))

target = pygame.image.load("sprites character/target3.png")
target = pygame.transform.scale(target, (int(target.get_width() * 0.23), int(target.get_height() * 0.23)))
window.blit(target, (850,440))

prev_time = pygame.time.get_ticks()
keys = pygame.key.get_pressed()

running = True
arrow_moving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Pour obtenir les coord de la souris
            arrow_angle = calculate_arrow_angle(mouse_x,mouse_y) - 45
        if event.type == KEYDOWN:
            if event.key == K_DELETE:
                show_arrow(window, arrow_x, arrow_y, arrow_angle)
                arrow_visible = True

            if event.key == K_UP:
                arrow_rotate_up = True
                arrow_rotate_down = False

            if event.key == K_DOWN:
                arrow_rotate_down = True
                arrow_rotate_up = False

            if event.key == K_SPACE:
                arrow_moving = True

    if arrow_rotate_down :
        arrow_direction = -25
    if arrow_rotate_up:
        arrow_direction = 25

    if arrow_moving:
        current_time = pygame.time.get_ticks()
        dt = (current_time - prev_time) / 1000.0
        arrow_x = move_arrow_straight()
        prev_time = current_time

    window.blit(background, (0, 20))
    window.blit(character, (75, base_ground))
    window.blit(target, (850, 440))
    show_arrow(window, arrow_x, arrow_y, arrow_angle + arrow_direction)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
