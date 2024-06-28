import sys

import pygame as pg

from scripts.entities import PhysicsEntity
from scripts.utils import load_image


class Game:
    def __init__(self):
        self.rate = 60
        self.width = 640
        self.height = 480
        self.running = True

        pg.init()
        pg.display.set_caption("Game")
        self.screen = pg.display.set_mode((self.width, self.height))
        self.display = pg.Surface((int(self.width / 2), int(self.height / 2)))

        self.clock = pg.time.Clock()

        self.movement = pg.math.Vector2(0, 0)

        self.assets = {
            "player": load_image("entities/player.png")
        }

        self.player = PhysicsEntity(self, "player", (50, 50), (8, 15))


    def run(self):

        while self.running:
            self.screen.fill((0, 200, 255))
            self.player.update(self.movement)
            self.player.render(self.screen)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = -1
                    if event.key == pg.K_RIGHT:
                        self.movement[0] = 1
                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = 0
                    if event.key == pg.K_RIGHT:
                        self.movement[0] = 0
            pg.display.update()
            self.clock.tick(self.rate)

        pg.quit()
        sys.exit()


Game().run()