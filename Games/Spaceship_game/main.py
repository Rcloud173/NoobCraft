import pygame
from random import randint

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 720,720
display_surface = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
pygame.display.set_caption("Spaceship game")
running = True
clock = pygame.time.Clock()

# plane surface
surf =  pygame.Surface((100,200))
surf.fill("green")
x = 100 

# importing an image
player_surf = pygame.image.load('Games/Spaceship_game/images/player.png').convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
player_direction = pygame.math.Vector2(1,0)
player_speed = 100

star_surf = pygame.image.load('Games/Spaceship_game/images/star.png').convert_alpha()
star_positions = [((randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT))) for i in range(20)]

meteor_surf = pygame.image.load('Games/Spaceship_game/images/meteor.png').convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surf = pygame.image.load('Games/Spaceship_game/images/laser.png').convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft =(20,WINDOW_HEIGHT -20))


while running:
    dt = clock.tick(10)/1000
    # event loop
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill("darkgray")
    for pos in star_positions:
        display_surface.blit(star_surf,pos)


    display_surface.blit(meteor_surf,meteor_rect)
    display_surface.blit(laser_surf,laser_rect)


    # player movement 
    player_rect.center += player_direction * player_speed * dt
    display_surface.blit(player_surf, player_rect)


    pygame.display.update()

pygame.quit()
  

    # if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
    #     player_direction *= -1