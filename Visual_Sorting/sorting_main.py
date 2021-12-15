import pygame as pg
import sys

from sorter import Sorter
from game_settings import GameSettings
from gui import GUI
from background_scroller import Background


def main():
    pg.init()
    pg.display.set_caption("Visual Sorter")

    settings = GameSettings()
    sorter = Sorter(settings)
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    gui = GUI(settings, screen, sorter)
    clock = pg.time.Clock()
    bg = Background("images/space_bg.png", 1, settings)

    app_running = True

    while app_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                app_running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                gui.gui_elements[-1].check_if_clicked()
            if event.type == pg.KEYDOWN and gui.gui_elements[-1].input_active:
                if event.key == pg.K_BACKSPACE:
                    gui.gui_elements[-1].delete_char()
                elif event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                    gui.gui_elements[-1].input_active = False
                    gui.update_number_of_values()
                else:
                    gui.gui_elements[-1].add_char(event.unicode)
        
        # screen.fill(pg.Color("black"))
        bg.draw(screen)

        for gui_element in gui.gui_elements:
            gui_element.draw(screen)

        if sorter.sorting:            
            if sorter.bubble_sorting:
                sorter.bubble_sorting = next(sorter.bubble_generator)
            if sorter.selection_sorting:       
                sorter.selection_sorting = next(sorter.selection_generator)
            if sorter.insertion_sorting:     
                sorter.insertion_sorting = next(sorter.insertion_generator)
        sorter.draw_bubble(
            screen,
            settings.value_horizontal_padding + settings.label_width + settings.window_padding * 2,
            settings.value_height + settings.value_vertical_padding + settings.window_padding
        )
        sorter.draw_selection(
            screen,
            settings.value_horizontal_padding + settings.label_width + settings.window_padding * 2,
            2 * (settings.value_height + settings.value_vertical_padding) + settings.window_padding
        )
        sorter.draw_insertion(
            screen,
            settings.value_horizontal_padding + settings.label_width + settings.window_padding * 2,
            3 * (settings.value_height + settings.value_vertical_padding) + settings.window_padding
        )
        
        pg.display.update()
        clock.tick(settings.sort_speed)
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()