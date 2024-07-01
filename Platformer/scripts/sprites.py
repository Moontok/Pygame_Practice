import pygame

import scripts.settings as settings


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = pygame.Surface((settings.TILE_SIZE, settings.TILE_SIZE))
        self.image.fill('white')
        self.rect = self.image.get_frect(topleft=pos)
        self.old_rect = self.rect.copy()