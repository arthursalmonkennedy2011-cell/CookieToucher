from tokenize import group

import pygame
import random
import sys

pygame.init()

screenWidth = 1000
screenHeight = 700

screen = pygame.display.set_mode((screenWidth, screenHeight))

clock = pygame.time.Clock()

def cookie(x, y):
    pygame.draw.circle(screen, (255, 218, 116), (x, y), 20)
    for n in range(3):
        chipsX = random.randrange(-10, 10)
        chipsY = random.randrange(-10, 10)
        pygame.draw.circle(screen, (123, 63, 0), (x + chipsX, y + chipsY), 5)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#def runOnce(fn):
 #   global runOnceTemp
  #  if runOnceTemp == :
   #     return cookie(random.randrange(690, 690), random.randrange(690, 690))


bakeCookie = False

running = True

while running:

    screen.fill((255, 253, 208))

    #only makes a cookie if bakeCookie is true
    if bakeCookie:
        cookie(random.randrange(690, 690), random.randrange(690, 690))
    player = pygame.draw.circle(screen, (0, 0, 0), player_pos, 30)
    # movement
    keys = pygame.key.get_pressed()
    dt = clock.tick(60) / 1000
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()