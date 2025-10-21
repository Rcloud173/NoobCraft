# simple_runner.py
# Minimal Subway Surfers-like mechanics:
# - 3 lanes
# - player box moves left/right between lanes
# - player can jump
# - obstacles and coins spawn and move toward player
# - score increments for coins and distance; speed increases gradually

import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (30, 144, 255)
OBST_COLOR = (220, 20, 60)
COIN_COLOR = (255, 215, 0)

FPS = 60
LANES = 3
LANE_X = [WIDTH * 0.25, WIDTH * 0.5, WIDTH * 0.75]  # x positions of lanes
GROUND_Y = HEIGHT - 80

# Player
PLAYER_W, PLAYER_H = 40, 60
START_LANE = 1  # middle lane (0,1,2)
JUMP_V = -12
GRAVITY = 0.6

# Spawn timers
OBST_SPAWN_TIME = 900  # ms initial
COIN_SPAWN_TIME = 700

FONT = pygame.font.SysFont(None, 28)

clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.lane = START_LANE
        self.x = LANE_X[self.lane]
        self.y = GROUND_Y - PLAYER_H
        self.vy = 0
        self.rect = pygame.Rect(0,0,PLAYER_W,PLAYER_H)
        self.update_rect()

    def update_rect(self):
        self.rect.centerx = int(self.x)
        self.rect.bottom = int(self.y + PLAYER_H)
        # rect.top is rect.bottom - height
        self.rect.width = PLAYER_W
        self.rect.height = PLAYER_H
        self.rect.left = self.rect.centerx - PLAYER_W // 2
        self.rect.top = self.rect.bottom - PLAYER_H

    def move_left(self):
        if self.lane > 0:
            self.lane -= 1
            self.x = LANE_X[self.lane]

    def move_right(self):
        if self.lane < LANES - 1:
            self.lane += 1
            self.x = LANE_X[self.lane]

    def jump(self):
        if self.on_ground():
            self.vy = JUMP_V

    def on_ground(self):
        return self.y >= GROUND_Y - PLAYER_H - 0.1 and abs(self.vy) < 0.1

    def update(self):
        # apply gravity
        self.vy += GRAVITY
        self.y += self.vy
        if self.y > GROUND_Y - PLAYER_H:
            self.y = GROUND_Y - PLAYER_H
            self.vy = 0
        self.update_rect()

    def draw(self, surface):
        pygame.draw.rect(surface, PLAYER_COLOR, self.rect)

class Obstacle:
    def __init__(self, lane, speed):
        self.lane = lane
        self.x = WIDTH + 50
        self.y = GROUND_Y - 40  # obstacle height smaller than player
        self.w = 40
        self.h = 40
        self.speed = speed
        self.rect = pygame.Rect(self.x - self.w//2, self.y - self.h, self.w, self.h)

    def update(self, dt):
        self.x -= self.speed * dt
        self.rect.centerx = int(self.x)
        self.rect.bottom = int(self.y)

    def draw(self, surface):
        pygame.draw.rect(surface, OBST_COLOR, self.rect)

class Coin:
    def __init__(self, lane, speed):
        self.lane = lane
        self.x = WIDTH + 50
        self.y = GROUND_Y - PLAYER_H - 20  # slightly above ground
        self.r = 10
        self.speed = speed
        self.rect = pygame.Rect(self.x - self.r, self.y - self.r, self.r*2, self.r*2)

    def update(self, dt):
        self.x -= self.speed * dt
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

    def draw(self, surface):
        pygame.draw.circle(surface, COIN_COLOR, self.rect.center, self.r)

def draw_ground(surface):
    pygame.draw.rect(surface, (50,50,50), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))

def main():
    player = Player()
    obstacles = []
    coins = []
    score = 0
    distance = 0
    running = True

    # spawn timers (pygame events)
    OBST_EVENT = pygame.USEREVENT + 1
    COIN_EVENT = pygame.USEREVENT + 2
    pygame.time.set_timer(OBST_EVENT, OBST_SPAWN_TIME)
    pygame.time.set_timer(COIN_EVENT, COIN_SPAWN_TIME)

    speed = 200.0  # pixels per second; world speed
    speed_inc_timer = 0

    while running:
        dt = clock.tick(FPS) / 1000.0  # seconds since last frame
        distance += speed * dt
        speed_inc_timer += dt

        # increase speed every 5 seconds (small increments)
        if speed_inc_timer > 5.0:
            speed += 12
            speed_inc_timer = 0
            # make spawns slightly more frequent as game progresses
            new_obst = max(350, OBST_SPAWN_TIME - int(distance // 1000) * 20)
            new_coin = max(300, COIN_SPAWN_TIME - int(distance // 1000) * 15)
            pygame.time.set_timer(OBST_EVENT, new_obst)
            pygame.time.set_timer(COIN_EVENT, new_coin)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.move_left()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.move_right()
                elif event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.jump()
                elif event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == OBST_EVENT:
                lane = random.randrange(LANES)
                obstacles.append(Obstacle(lane, speed))
            if event.type == COIN_EVENT:
                lane = random.randrange(LANES)
                coins.append(Coin(lane, speed))

        # Update
        player.update()
        for o in obstacles:
            o.update(dt * speed / 200.0 * (speed/200.0))  # adapt to speed for consistent feel
        for c in coins:
            c.update(dt * speed / 200.0 * (speed/200.0))

        # Collision detection
        # Only check obstacles/coins that are in same lane roughly by x — lanes are horizontal x positions,
        # but our obstacles are moving horizontally: to simulate alignment, we use lane index to match player lane.
        for o in obstacles[:]:
            # place obstacle at lane's x so collision makes sense visually:
            o.rect.centerx = int(o.x)
            # if obstacle is near the player's lane center x, check vertical collision
            if o.lane == player.lane and o.rect.colliderect(player.rect):
                # if player is jumping above obstacle (i.e., player's bottom is above obstacle top) ignore
                if player.rect.bottom <= o.rect.top + 5:
                    pass  # jumped over
                else:
                    game_over_screen(WIN, score, distance)
                    return
            if o.x < -100:
                obstacles.remove(o)

        for c in coins[:]:
            c.rect.centerx = int(c.x)
            if c.lane == player.lane and c.rect.colliderect(player.rect):
                score += 10
                coins.remove(c)
            elif c.x < -100:
                coins.remove(c)

        # Draw
        WIN.fill((135, 206, 235))  # sky blue
        draw_ground(WIN)

        # draw lanes as vertical markers to help visual
        for x in LANE_X:
            pygame.draw.line(WIN, (200,200,200), (x, 0), (x, GROUND_Y), 1)

        # draw coins and obstacles
        for c in coins:
            # align coin to lane x
            c.rect.centerx = int(c.x)
            c.draw(WIN)
        for o in obstacles:
            o.draw(WIN)

        player.draw(WIN)

        # HUD
        hud = FONT.render(f"Score: {score}   Distance: {int(distance)}", True, BLACK)
        WIN.blit(hud, (10, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def game_over_screen(surface, score, distance):
    clock = pygame.time.Clock()
    over = True
    font_big = pygame.font.SysFont(None, 48)
    font_small = pygame.font.SysFont(None, 28)
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # restart on any key
                over = False

        surface.fill((20,20,20))
        text = font_big.render("GAME OVER", True, (255,255,255))
        s1 = font_small.render(f"Score: {score}", True, (255,255,255))
        s2 = font_small.render(f"Distance: {int(distance)}", True, (255,255,255))
        prompt = font_small.render("Press any key to exit", True, (180,180,180))

        surface.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50)))
        surface.blit(s1, s1.get_rect(center=(WIDTH//2, HEIGHT//2)))
        surface.blit(s2, s2.get_rect(center=(WIDTH//2, HEIGHT//2 + 30)))
        surface.blit(prompt, prompt.get_rect(center=(WIDTH//2, HEIGHT//2 + 90)))

        pygame.display.flip()
        clock.tick(15)

if __name__ == "__main__":
    main()
