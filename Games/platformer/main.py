import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((100, 150, 255))  # sky blue background
    pygame.display.flip()
    clock.tick(60)
