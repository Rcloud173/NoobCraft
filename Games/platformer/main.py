# import pygame
# import sys

# pygame.init()
# WIDTH, HEIGHT = 800, 400
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# clock = pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     screen.fill((100, 150, 255))  # sky blue background
#     pygame.display.flip()
#     clock.tick(60)

import pygame, sys

pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player setup
player = pygame.Rect(100, 300, 40, 60)
player_vel_y = 0
gravity = 0.8
on_ground = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Horizontal movement
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # Jump
    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = -15
        on_ground = False

    # Gravity
    player_vel_y += gravity
    player.y += player_vel_y

    # Ground collision
    if player.bottom >= HEIGHT - 50:
        player.bottom = HEIGHT - 50
        player_vel_y = 0
        on_ground = True

    screen.fill((100, 150, 255))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 200, 50), (0, HEIGHT - 50, WIDTH, 50))  # ground
    pygame.display.flip()
    clock.tick(60)
