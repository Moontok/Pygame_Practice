import pygame
from pygame.math import Vector2

import scripts.settings as settings


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = Vector2()

    def draw(self, target_pos):
        self.offset.x = -(target_pos[0] - settings.WINDOW_WIDTH / 2)
        self.offset.y = -(target_pos[1] - settings.WINDOW_HEIGHT / 2)

        for sprite in sorted(self, key=lambda sprite: sprite.z):
            offset_pos = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image, offset_pos)