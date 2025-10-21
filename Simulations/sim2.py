import pygame
import math

# ---- Simulation parameters ----
WIDTH, HEIGHT = 800, 600
ORIGIN = (WIDTH//2, HEIGHT//4)
G = 9.81
DT = 0.02

# ---- Pendulum parameters ----
m1, m2 = 10.0, 10.0     # masses
L1, L2 = 200.0, 200.0   # lengths
theta1, theta2 = math.pi/2, math.pi/2  # initial angles
omega1, omega2 = 0.0, 0.0               # angular velocities

# ---- Pygame setup ----
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Double Pendulum Simulation")
clock = pygame.time.Clock()
traj_color = (0, 255, 0)
background = (12, 12, 30)
pend_color = (200, 200, 200)
bob_radius = 15

# ---- Trajectory history for the second bob ----
trajectory = []

# ---- Equations of motion (from Lagrangian mechanics) ----
def acceleration(theta1, theta2, omega1, omega2):
    delta = theta2 - theta1
    denom1 = (m1 + m2) * L1 - m2 * L1 * math.cos(delta)**2
    denom2 = (L2/L1) * denom1

    a1 = (m2*L2*omega2**2*math.sin(delta) + m2*G*math.sin(theta2)*math.cos(delta)
          + m2*L2*omega2**2*math.sin(delta)*math.cos(delta) - (m1+m2)*G*math.sin(theta1)) / denom1

    a2 = (-L1/L2*omega1**2*math.sin(delta) - math.sin(delta)*G*(m1+m2)/L2 + omega1**2*L1*math.sin(delta) / L2) # simplified
    # Use small-step approximation to keep it stable
    return a1, a2

# Better version using standard formulas:
def derivatives(theta1, theta2, omega1, omega2):
    delta = theta2 - theta1
    denom1 = (m1 + m2)*L1 - m2*L1*math.cos(delta)**2
    domega1 = (m2*L1*omega1**2*math.sin(delta)*math.cos(delta) +
               m2*G*math.sin(theta2)*math.cos(delta) +
               m2*L2*omega2**2*math.sin(delta) -
               (m1 + m2)*G*math.sin(theta1)) / denom1

    denom2 = (L2/L1)*denom1
    domega2 = (-m2*L2*omega2**2*math.sin(delta)*math.cos(delta) +
               (m1 + m2)*(G*math.sin(theta1)*math.cos(delta) -
               L1*omega1**2*math.sin(delta) - G*math.sin(theta2))) / denom2
    return domega1, domega2

# ---- Main loop ----
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RK4 or simple Euler integration
    domega1, domega2 = derivatives(theta1, theta2, omega1, omega2)
    omega1 += domega1 * DT
    omega2 += domega2 * DT
    theta1 += omega1 * DT
    theta2 += omega2 * DT

    # Compute positions
    x1 = ORIGIN[0] + L1*math.sin(theta1)
    y1 = ORIGIN[1] + L1*math.cos(theta1)
    x2 = x1 + L2*math.sin(theta2)
    y2 = y1 + L2*math.cos(theta2)

    trajectory.append((x2, y2))
    if len(trajectory) > 1000:  # limit trajectory length
        trajectory.pop(0)

    # ---- Draw ----
    screen.fill(background)

    # Draw trajectory
    for i in range(1, len(trajectory)):
        pygame.draw.line(screen, traj_color, trajectory[i-1], trajectory[i], 2)

    # Draw rods
    pygame.draw.line(screen, pend_color, ORIGIN, (x1, y1), 3)
    pygame.draw.line(screen, pend_color, (x1, y1), (x2, y2), 3)

    # Draw bobs
    pygame.draw.circle(screen, pend_color, (int(x1), int(y1)), bob_radius)
    pygame.draw.circle(screen, (255, 0, 0), (int(x2), int(y2)), bob_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
