import pygame as pg
import sys

from sorter import Sorter


def main():
    pg.init()
    pg.display.set_caption("Sorter")

    screen = pg.display.set_mode((800, 400))
    clock = pg.time.Clock()

    app_running = True
    gui_font = pg.font.SysFont("Console", 30)

    sorter = Sorter(30, 20)
    sort_speed = 10
    insertion_sorting = False
    temp_sorting = True

    while app_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                app_running = False

        if insertion_sorting:
            for i in range(len(sorter.values)):
                best = i

                sorter.values[i].color = pg.Color("yellow")  #############

                for j in range(i + 1, len(sorter.values)):
                    
                    sorter.values[j].color = pg.Color("cyan")  #############

                    if sorter.values[j].height < sorter.values[best].height:
                        if best != i:
                            sorter.values[best].color = pg.Color("grey")  #############
                        sorter.values[j].color = pg.Color("cyan")  #############
                        best = j

                    screen.fill(pg.Color("black"))
                    sorter.draw(screen, 10, 200)
                    pg.display.update()
                    clock.tick(sort_speed)
                    sorter.values[j].color = pg.Color("grey")  #############
                    if best != i:
                        sorter.values[best].color = pg.Color("red")

                swap(sorter.values, i, best)   
                sorter.values[i].color = pg.Color("green")  #############
                screen.fill(pg.Color("black"))
                sorter.draw(screen, 10, 200)

                pg.display.update()
                clock.tick(sort_speed)
        
                
            insertion_sorting = False
        elif temp_sorting:
            screen.fill(pg.Color("black"))
            sorter.values = list(sorter.selection_sort())
            sorter.draw(screen, 10, 200)

            pg.display.update()
            clock.tick(sort_speed)
        else:
            screen.fill(pg.Color("black"))
            sorter.draw(screen, 10, 200)
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