import pygame
import sys
from settings import *
from player import *
from map import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)

    def update(self):
        pygame.display.flip()
        self.clock.tick(FPS)
        pygame.display.set_caption(f"FPS: {self.clock.get_fps():.2f}")
        self.delta_time = self.clock.tick(FPS)
        self.player.update()

    def draw(self):
        self.screen.fill("black")
        self.map.draw()
        self.player.draw()
        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()
    