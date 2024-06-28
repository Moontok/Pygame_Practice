import pygame as pg


class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.e_type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = pg.math.Vector2(0, 0)

    def update(self, movement=pg.math.Vector2(0, 0)):
        frame_movement = movement + self.velocity
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

    def render(self, surface):
        surface.blit(self.game.assets["player"], self.pos)