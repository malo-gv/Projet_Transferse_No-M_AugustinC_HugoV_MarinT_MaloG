import pygame.time
from pygame.locals import *
from arrow import *
from constants import *
from target import *

currentTime = pygame.time.get_ticks() / 1000
print(currentTime)
pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, LENGTH))

#test colision zone
zone = pygame.image.load("sprites character/circle.png")
zone = pygame.transform.scale(zone, (int(zone.get_width() * 0.11), int(zone.get_height() * 0.11)))
coinHG = pygame.image.load("sprites character/button.png")
coinHG = pygame.transform.scale(coinHG, (int(zone.get_width() * 0.3), int(zone.get_height() * 0.3)))

coinHD = pygame.image.load("sprites character/button.png")
coinHD = pygame.transform.scale(coinHG, (int(zone.get_width() * 0.3), int(zone.get_height() * 0.3)))

coinBG = pygame.image.load("sprites character/button.png")
coinBG = pygame.transform.scale(coinHG, (int(zone.get_width() * 0.3), int(zone.get_height() * 0.3)))

coinBD = pygame.image.load("sprites character/button.png")
coinBD = pygame.transform.scale(coinHG, (int(zone.get_width() * 0.3), int(zone.get_height() * 0.3)))

# fond
background = pygame.image.load("Images background/background v1.jpg").convert()

# archer
character = pygame.image.load("sprites character/archer.png")
character = pygame.transform.scale(character, (int(character.get_width() * 0.25), int(character.get_height() * 0.25)))
character = pygame.transform.flip(character, True, False)

target = pygame.image.load("sprites character/bullseye.png")
target = pygame.transform.scale(target, (int(target.get_width() * 0.20), int(target.get_height() * 0.20)))

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
        arrowX, arrowY = moveArrow(arrowX, arrowY, shootForce, arrowAngle, timerShoot)

        if collisionCible(arrowX,arrowY,arrowAngle, targetX,targetY, target):
            arrowMoving = False
            colisionActive = True
            waitingTimer = 0

    if (arrowMoving == False and colisionActive ):
        pygame.time.wait(2000)
        print("NEXT")
        colisionActive = False
        arrowX = baseX
        arrowY = baseY
        targetX, targetY = bougerCible()

    if (arrowX > 1080 or arrowY > 720):
        arrowX = baseX
        arrowY = baseY
        arrowMoving = False


    window.blit(background, (0, 20))
    window.blit(character, (75, baseGround))
    window.blit(target, (targetX, targetY))
    zoneX = targetX + 25
    zoneY = targetY + 25
    window.blit(zone,(zoneX, zoneY))
    window.blit(coinHG, (zoneX + 3, zoneY))
    window.blit(coinHD, (zoneX + 35, zoneY))
    window.blit(coinBG, (zoneX + 3, zoneY + 35))
    window.blit(coinBD, (zoneX + 35, zoneY + 35))



    if (not arrowMoving) and colisionActive == False:
        drawTrajectory(window, initialArrowX, initialArrowY, shootForce, arrowAngle)

    showArrow(window, arrowX, arrowY, arrowAngle)
    pygame.display.update()
    clock.tick(60)

pygame.quit()