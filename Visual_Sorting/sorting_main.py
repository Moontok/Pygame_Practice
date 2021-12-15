import pygame as pg
import sys

from sorter import Sorter
from button import Button
from label import Label


def main():
    pg.init()
    pg.display.set_caption("Sorter")
    number_of_values = 70
    value_height = 100
    value_width = 20
    padding = 2
    sort_speed = 10
    screen_width = max(840, (value_width + padding) * number_of_values+padding + 240)
    screen_height = (value_height + 10) * 3 + 40
    screen = pg.display.set_mode((screen_width, screen_height))
    clock = pg.time.Clock()

    app_running = True

    sorter = Sorter(number_of_values, value_height, value_width, sort_speed)
    
    gui_font = pg.font.SysFont("Console", 30)

    start_button = Button(
        int(screen.get_width() / 2) - 410,
        int(screen.get_height() - 40),
        200, 30,
        pg.Color("grey"),
        pg.Color("white"),
        "Start",
        gui_font,
        action=lambda: start_sorts(sorter, start_button)
    )

    restart_button = Button(
        int(screen.get_width() / 2) - 205,
        int(screen.get_height() - 40),
        200, 30,
        pg.Color("grey"),
        pg.Color("white"),
        "Restart",
        gui_font,
        action=lambda: setup_new_sorts(sorter, start_button)
    )

    speed_up_button = Button(
        int(screen.get_width() / 2) + 5, 
        int(screen.get_height() - 40),
        200, 30,
        pg.Color("grey"),
        pg.Color("white"),
        "+Speed",
        gui_font,
        action=lambda: speed_up(sorter)
    )

    slow_down_button = Button(
        int(screen.get_width() / 2) + 210, 
        int(screen.get_height() - 40), 
        200, 
        30, 
        pg.Color("grey"), 
        pg.Color("white"), 
        "-Speed", 
        gui_font, 
        action=lambda: slow_down(sorter)
    )

    bubble_label = Label(
        10, 10, 200,
        value_height,
        pg.Color("grey"),
        pg.Color("cyan"),
        "Bubble",
        gui_font,
        align="center",
        border=2
    )

    selection_label = Label(
        10, 10 + value_height, 200,
        value_height, pg.Color("grey"),
        pg.Color("cyan"),"Selection",
        gui_font,
        align="center",
        border=2
    )

    insertion_label = Label(
        10, 10 + value_height * 2, 200,
        value_height, pg.Color("grey"),
        pg.Color("cyan"),
        "Insertion",
        gui_font,
        align="center",
        border=2
    )

    while app_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                app_running = False
        
        screen.fill(pg.Color("black"))
        start_button.draw(screen)
        restart_button.draw(screen)
        speed_up_button.draw(screen)
        slow_down_button.draw(screen)
        bubble_label.draw(screen)
        selection_label.draw(screen)
        insertion_label.draw(screen)
        if sorter.sorting:            
            if sorter.bubble_sorting:
                sorter.bubble_sorting = next(sorter.bubble_generator)
            if sorter.selection_sorting:       
                sorter.selection_sorting = next(sorter.selection_generator)
            if sorter.insertion_sorting:     
                sorter.insertion_sorting = next(sorter.insertion_generator)
        sorter.draw_bubble(screen, padding + 220, value_height + 10)
        sorter.draw_selection(screen, padding + 220, 2 * value_height + 10)
        sorter.draw_insertion(screen, padding + 220, 3 * value_height + 10)
        
        pg.display.update()
        clock.tick(sorter.sort_speed)
    pg.quit()
    sys.exit()


def start_sorts(sorter, button):
    sorter.sorting = not sorter.sorting
    if sorter.sorting:
        button.update_text("Pause")
    else:
        button.update_text("Start")


def setup_new_sorts(sorter, button):
    sorter.sorting = False
    sorter.bubble_sorting = True
    sorter.selection_sorting = True
    sorter.insertion_sorting = True
    sorter.setup_values()
    button.update_text("Start")


def speed_up(sorter):
    if sorter.sort_speed < 300:
        sorter.sort_speed += 10


def slow_down(sorter):
    if sorter.sort_speed > 10:
        sorter.sort_speed -= 10


if __name__ == "__main__":
    main()