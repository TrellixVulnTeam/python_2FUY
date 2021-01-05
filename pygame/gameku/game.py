# 1. import library yang diperlukan
import pygame
from pygame.locals import *
import math

# 2. inisialisasi game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

keys = {
    "top": False,
    "bottom": False,
    "left": False,
    "right": False
}

running = True

playerpos = [100, 100]

# 3. load game assets
# load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

# 4. game loop
while(running):
    # 5. clear screen
    screen.fill(0)

    # 6. draw game object
    # draw grass
    for x in range(int(width/grass.get_width()+1)):
        for y in range(int(height/grass.get_width()+1)):
            screen.blit(grass, (x*100, y*100))

    # draw castle
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    # draw player
    mouse_position = pygame.mouse.get_pos()
    angle = math.atan2(mouse_position[1] - (playerpos[1]+32), mouse_position[0] - (playerpos[0]+26))
    player_rotation = pygame.transform.rotate(player, 360 - angle * 57.29)
    new_playerpos = (playerpos[0] - player_rotation.get_rect().width / 2, playerpos[1] - player_rotation.get_rect().height / 2)
    screen.blit(player_rotation, new_playerpos)

    # 7. update screen
    pygame.display.flip()

    # 8. event loop
    for event in pygame.event.get():
        #even while exit button onclick
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # cek key bawah dan key atas
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys["top"] = True
            elif event.key == K_a:
                keys["left"] = True
            elif event.key == K_s:
                keys["bottom"] = True
            elif event.key == K_d:
                keys["right"] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys["top"] = False
            elif event.key == K_a:
                keys["left"] = False
            elif event.key == K_s:
                keys["bottom"] = False
            elif event.key == K_d:
                keys["right"] = False

    if keys["top"]:
        playerpos[1] -= 5
    elif keys["bottom"]:
        playerpos[1] += 5
    elif keys["left"]:
        playerpos[0] -= 5
    elif keys["right"]:
        playerpos[0] += 5
