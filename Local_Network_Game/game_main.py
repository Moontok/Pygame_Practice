import pygame as pg
import sys

from player import Player


def main():
    pg.init()
    width = 500
    height = 500
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Client")
    clock = pg.time.Clock()

    game_running = True
    player = Player(50, 50, 100, 100, pg.Color("green"))
    
    client_number = 0

    while game_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False

        player.move()

        screen.fill(pg.Color("black"))
        player.draw(screen)

        pg.display.update()
        clock.tick(60)

    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()