import pygame as pg
import sys

from game_settings import Settings
from tilemap import Tilemap


def main():
    pg.init()
    pg.display.set_caption("Project X-Space")

    settings = Settings()    
    screen = pg.display.set_mode((settings.window_width, settings.window_height))
    clock = pg.time.Clock()

    game_running = True

    level_map = load_level('level_map.txt')
    tilemap = Tilemap(settings.tile_size)
    tilemap.generate_map(level_map)

    while game_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False

        screen.fill(pg.Color("black"))
        tilemap.draw(screen)

        pg.display.update()

    pg.quit()
    sys.exit()
    

def load_level(level_map):
    """Load the level from a text file."""
    
    with open(level_map, "r") as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    main()