import pygame
import math
from settings import *

PLAYER_POS = 7, 5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.007
PLAYER_ROTATION_SPEED = 0.01

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def draw(self):
        pygame.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
                     (self.x * 100 + SCREEN_SIZE[0] * math.cos(self.angle),
                     self.y * 100 + SCREEN_SIZE[1] * math.sin(self.angle)), 2)
        pygame.draw.circle(self.game.screen, 'blue', (self.x * 100, self.y * 100), 15)

    def move(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = sin_a * speed
        speed_cos = cos_a * speed

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.angle -= PLAYER_ROTATION_SPEED * self.game.delta_time
        if keys[pygame.K_d ] or keys[pygame.K_RIGHT]:
            self.angle += PLAYER_ROTATION_SPEED * self.game.delta_time
        self.angle %= math.tau

        self.x += dx
        self.y += dy

    def update(self):
        self.move()

    @property
    def pos(self):
        return (self.x, self.y)
    
    @property
    def map_pos(self):
        return (int(self.x), int(self.y))