import pygame
import math

pygame.init()
screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True
dt = 0

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, 1],
    [1, _, 1, 1, _, _, _, _, 1, _, _, _, _, _, _, 1],
    [1, _, 1, _, _, _, _, _, _, _, _, 1, 1, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1, 1, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_map = {}

player_x = 5
player_y = 5
player_angle = 0
player_speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # Add your game logic here v

    for j, row in enumerate(mini_map):
        for i, value in enumerate(row):
            if value:
                world_map[(i, j)] = value

    [pygame.draw.rect(screen, "white", (pos[0] * 80, pos[1] * 80, 80, 80), 2) for pos in world_map]

    sin_angle = math.sin(player_angle)
    cos_angle = math.cos(player_angle)
    dx = 0
    dy = 0
    speed = player_speed * dt
    speed_sin = speed * sin_angle
    speed_cos = speed * cos_angle

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        dx += speed_cos
        dy += speed_sin
    if keys[pygame.K_s]:
        dx += -speed_cos
        dy += -speed_sin
    if keys[pygame.K_a]:
        dx += speed_sin
        dy += -speed_cos
    if keys[pygame.K_d]:
        dx += -speed_sin
        dy += speed_cos

    player_x += dx
    player_y += dy

    if keys[pygame.K_LEFT]:
        player_angle -= 5 * dt
    if keys[pygame.K_RIGHT]:
        player_angle += 5 * dt
    player_angle %= math.tau

    pygame.draw.line(screen, 'yellow', (player_x * 100, player_y * 100),
                     (player_x * 100 + screen_size[0] * math.cos(player_angle),
                     player_y * 100 + screen_size[1] * math.sin(player_angle)), 2)
    pygame.draw.circle(screen, 'blue', (player_x * 100, player_y * 100), 15)

    # Add your game logic here ^

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()