import sys

import pygame as pg

import ui_toolbox as ui


def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    font = pg.font.SysFont('Console', 32)

    label = ui.Label(200, 100, 250, 50, "Hello World!")
    button = ui.Button(200, 200, 200, 50, "Click Me", action=print_text, string="Hello World!")
    input_box = ui.InputBox(200, 300, 200, 50)

    running = True
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            input_box.process_event(event)

        screen.fill(pg.Color("black"))
        label.draw(screen)
        button.draw(screen)
        input_box.draw(screen)

        pg.display.update()
        clock.tick(60)
    
    pg.quit()
    sys.exit()


def print_text(string):
    print(string)


main()