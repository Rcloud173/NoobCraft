import pygame
import random

# --- Setup ---
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Bouncing Balls Simulation")

clock = pygame.time.Clock()

# --- Ball class ---
class Ball:
    def __init__(self, x, y, radius, color, velocity):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx, self.vy = velocity

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Collision with walls
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.vx *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.vy *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

# --- Create multiple balls ---
balls = []
for _ in range(10):
    radius = random.randint(10, 25)
    x = random.randint(radius, WIDTH - radius)
    y = random.randint(radius, HEIGHT - radius)
    color = [random.randint(50, 255) for _ in range(3)]
    velocity = [random.choice([-4, -3, -2, 2, 3, 4]),
                random.choice([-4, -3, -2, 2, 3, 4])]
    balls.append(Ball(x, y, radius, color, velocity))

# --- Main Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    for ball in balls:
        ball.move()
        ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
