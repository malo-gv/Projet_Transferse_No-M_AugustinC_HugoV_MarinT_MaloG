from pygame.locals import *
from arrow import *
from constants import *

currentTime = pygame.time.get_ticks() / 1000
print(currentTime)
pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, LENGTH))

# fond
background = pygame.image.load("Images background/background v1.jpg").convert()

# archer
character = pygame.image.load("sprites character/archer.png")
character = pygame.transform.scale(character, (int(character.get_width() * 0.25), int(character.get_height() * 0.25)))
character = pygame.transform.flip(character, True, False)

target = pygame.image.load("sprites character/bullseye.png")
target = pygame.transform.scale(target, (int(target.get_width() * 0.20), int(target.get_height() * 0.20)))

prevTime = pygame.time.get_ticks() / 1000
keys = pygame.key.get_pressed()

running = True
arrowMoving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEMOTION and arrowMoving == False and colisionActive == False:
            mouseX, mouseY = pygame.mouse.get_pos()  # Pour obtenir les coord de la souris
            arrowAngle = calculateArrowAngle(mouseX, mouseY, arrowX, arrowY)
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                shootStartTime = pygame.time.get_ticks()
        if event.type == KEYUP:
            if event.key == K_SPACE:
                shootEndTime = pygame.time.get_ticks()
                shootDuration = (shootEndTime - shootStartTime) / 1000.0
                shootForce = min(maxForce, shootDuration * 10)
                initialArrowX = arrowX
                initialArrowY = arrowY
                arrowMoving = True
                startTime = pygame.time.get_ticks() / 1000


    if arrowMoving:
        currentTime = pygame.time.get_ticks() / 1000
        timerShoot = currentTime - startTime
        print(timerShoot)
        arrowX, arrowY = moveArrow(initialArrowX, initialArrowY, shootForce, arrowAngle, timerShoot)
        prevTime = currentTime
        colisionActive = collisionCible(arrowX, arrowY, targetX, targetY)


    if colisionActive:
        arrowMoving = False

    window.blit(background, (0, 20))
    window.blit(character, (75, baseGround))
    window.blit(target, (targetX, targetY))
    showArrow(window, arrowX, arrowY, arrowAngle)
    initialArrowX = arrowX
    initialArrowY = arrowY
    pygame.display.update()
    clock.tick(60)

pygame.quit()