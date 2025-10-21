import pygame
import random
import sys

# Initialize
pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Subway Surfer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (200, 0, 0)
BLUE  = (0, 150, 255)

clock = pygame.time.Clock()

# Game variables
lanes = [100, 200, 300]  # X positions for 3 lanes
player_x = 200
player_y = 500
player_width = 40
player_height = 40
lane_index = 1
is_jumping = False
jump_count = 10

obstacles = []
speed = 5
score = 0

font = pygame.font.SysFont(None, 30)

def draw_player():
    pygame.draw.rect(win, BLUE, (player_x - player_width//2, player_y, player_width, player_height))

def draw_obstacles():
    for obs in obstacles:
        pygame.draw.rect(win, RED, obs)

def move_obstacles():
    global obstacles, score
    for obs in obstacles:
        obs.y += speed
    obstacles = [obs for obs in obstacles if obs.y < HEIGHT]
    if random.randint(0, 30) == 0:  # Spawn rate
        lane = random.choice(lanes)
        obstacles.append(pygame.Rect(lane - 20, -50, 40, 40))
    score += 1

def check_collision():
    player_rect = pygame.Rect(player_x - player_width//2, player_y, player_width, player_height)
    for obs in obstacles:
        if player_rect.colliderect(obs):
            return True
    return False

# Game Loop
running = True
while running:
    clock.tick(30)
    win.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Lane switching
    if keys[pygame.K_LEFT] and lane_index > 0:
        lane_index -= 1
        player_x = lanes[lane_index]
        pygame.time.wait(100)
    elif keys[pygame.K_RIGHT] and lane_index < 2:
        lane_index += 1
        player_x = lanes[lane_index]
        pygame.time.wait(100)

    # Jump logic
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1 if jump_count > 0 else -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jump_count = 10
            is_jumping = False

    move_obstacles()
    if check_collision():
        print(f"Game Over! Final Score: {score}")
        pygame.quit()
        sys.exit()

    draw_player()
    draw_obstacles()
    score_text = font.render(f"Score: {score}", True, BLACK)
    win.blit(score_text, (10, 10))

    pygame.display.update()
