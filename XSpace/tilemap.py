import pygame as pg




class Tile(pg.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))


class Tilemap:

    def __init__(self, tile_size):
        self.tile_size = tile_size

        self.grass_l = pg.image.load("assets/tiles/tile_0001.png").convert_alpha()
        self.grass_l = pg.transform.scale(self.grass_l, (tile_size, tile_size))

        self.grass_m = pg.image.load("assets/tiles/tile_0002.png").convert_alpha()
        self.grass_m = pg.transform.scale(self.grass_m, (tile_size, tile_size))

        self.grass_r = pg.image.load("assets/tiles/tile_0003.png").convert_alpha()
        self.grass_r = pg.transform.scale(self.grass_r, (tile_size, tile_size))

        self.dirt_l = pg.image.load("assets/tiles/tile_0121.png").convert_alpha()
        self.dirt_l = pg.transform.scale(self.dirt_l, (tile_size, tile_size))

        self.dirt_m = pg.image.load("assets/tiles/tile_0122.png").convert_alpha()
        self.dirt_m = pg.transform.scale(self.dirt_m, (tile_size, tile_size))

        self.dirt_r = pg.image.load("assets/tiles/tile_0123.png").convert_alpha()
        self.dirt_r = pg.transform.scale(self.dirt_r, (tile_size, tile_size))        

        self.dirt_rb = pg.image.load("assets/tiles/tile_0123.png").convert_alpha()
        self.dirt_rb = pg.transform.scale(self.dirt_rb, (tile_size, tile_size))



        self.tile_images = {
            "G": self.grass_m,
            "L": self.grass_l,
            "R": self.grass_r,
            "D": self.dirt_m,
            "d": self.dirt_l,
            "b": self.dirt_r,

        }
        self.tiles = pg.sprite.Group()

    def generate_map(self, level_map,):
        """Generate the map from the level map."""

        for row_index, row in enumerate(level_map):
            for col_index, cell in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size
                tile_image = self.tile_images.get(cell)
                if tile_image:
                    tile = Tile(x, y, tile_image)
                    self.tiles.add(tile)

    
    def draw(self, surface):
        """Draw the tilemap to the screen."""

        self.tiles.draw(surface)