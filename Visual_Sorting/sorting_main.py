import pygame as pg
import sys

from sorter import Sorter


def main():
    pg.init()
    pg.display.set_caption("Sorter")

    screen = pg.display.set_mode((1600, 340))
    clock = pg.time.Clock()

    app_running = True
    gui_font = pg.font.SysFont("Console", 30)

    sorter = Sorter(70, 20)
    sort_speed = 200
    bubble_sorting = True
    selection_sorting = True
    insertion_sorting = True

    while app_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                app_running = False

        if bubble_sorting or selection_sorting or insertion_sorting:
            screen.fill(pg.Color("black"))
            if bubble_sorting:
                bubble_sorting = next(sorter.bubble_generator)
                sorter.draw_bubble(screen, 10, 110)
            else:
                sorter.draw_bubble(screen, 10, 110)
            if selection_sorting:
                selection_sorting = next(sorter.selection_generator)
                sorter.draw_selection(screen, 10, 220)
            else:
                sorter.draw_selection(screen, 10, 220)
            if insertion_sorting:
                insertion_sorting = next(sorter.insertion_generator)
                sorter.draw_insertion(screen, 10, 330)
            else:
                sorter.draw_insertion(screen, 10, 330)

            pg.display.update()
            clock.tick(sort_speed)
        else:
            screen.fill(pg.Color("black"))
            sorter.draw_bubble(screen, 10, 110)
            sorter.draw_selection(screen, 10, 220)
            sorter.draw_insertion(screen, 10, 330)
            pg.display.update()
            clock.tick(60)
        
    pg.quit()
    sys.exit()


def swap(values, i, j):
    """ Swap values[i] with values[j] inside of list values. """

    temp = values[i]
    values[i] = values[j]
    values[j] = temp

    values[j].color = pg.Color("grey")  #############


if __name__ == "__main__":
    main()