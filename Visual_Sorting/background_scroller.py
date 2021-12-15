import pygame as pg
import math


class Background:
    """Class that creates a seamless background scrolling effect."""
    def __init__(self, image, speed_y, settings):        
        self.settings = settings
        self.background = pg.image.load(image)
        self.tile_rect = self.background.get_rect()
        self.bg_tiles = [self.tile_rect[:]]
        self.bg_tiles[0][1] = -self.tile_rect.height
        
        self.number_of_tiles = math.ceil(self.settings.screen_height / self.bg_tiles[0][3]) + 1
        for i in range(self.number_of_tiles):
            tile = self.bg_tiles[i][:]
            tile[1] = self.bg_tiles[i][1] + self.bg_tiles[i][3]
            self.bg_tiles.append(tile)

        self.speed_y = speed_y

    def draw(self, screen):
        """ Draw the background to the screen. """

        for tile in self.bg_tiles:
            if tile[1] > self.settings.screen_height:
                tile[1] = -self.tile_rect.height
            else:
                tile[1] += self.speed_y            
            screen.blit(self.background, tile)
