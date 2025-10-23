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

# import pygame, sys

# pygame.init()
# WIDTH, HEIGHT = 800, 400
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# clock = pygame.time.Clock()

# # Player setup
# player = pygame.Rect(100, 300, 40, 60)
# player_vel_y = 0
# gravity = 0.8
# on_ground = False

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     keys = pygame.key.get_pressed()

#     # Horizontal movement
#     if keys[pygame.K_LEFT]:
#         player.x -= 5
#     if keys[pygame.K_RIGHT]:
#         player.x += 5

#     # Jump
#     if keys[pygame.K_SPACE] and on_ground:
#         player_vel_y = -15
#         on_ground = False

#     # Gravity
#     player_vel_y += gravity
#     player.y += player_vel_y

#     # Ground collision
#     if player.bottom >= HEIGHT - 50:
#         player.bottom = HEIGHT - 50
#         player_vel_y = 0
#         on_ground = True

#     screen.fill((100, 150, 255))
#     pygame.draw.rect(screen, (255, 0, 0), player)
#     pygame.draw.rect(screen, (0, 200, 50), (0, HEIGHT - 50, WIDTH, 50))  # ground
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

# Platforms (list of rectangles)
platforms = [
    pygame.Rect(0, HEIGHT - 50, WIDTH, 50),  # ground
    pygame.Rect(200, 300, 120, 20),
    pygame.Rect(400, 250, 120, 20),
    pygame.Rect(600, 200, 120, 20),
]

def move_player():
    global player_vel_y, on_ground

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0

    # Horizontal
    if keys[pygame.K_LEFT]:
        dx = -5
    if keys[pygame.K_RIGHT]:
        dx = 5

    # Jump
    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = -15
        on_ground = False

    # Gravity
    player_vel_y += gravity
    dy += player_vel_y

    # Collision
    on_ground = False
    player.x += dx
    player.y += dy

    for plat in platforms:
        if player.colliderect(plat):
            if player_vel_y > 0:  # falling down
                player.bottom = plat.top
                player_vel_y = 0
                on_ground = True
            elif player_vel_y < 0:  # hitting head
                player.top = plat.bottom
                player_vel_y = 0

def draw():
    screen.fill((135, 206, 235))  # sky blue
    pygame.draw.rect(screen, (255, 50, 50), player)  # player
    for plat in platforms:
        pygame.draw.rect(screen, (50, 200, 50), plat)
    pygame.display.flip()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    move_player()
    draw()
    clock.tick(60)
