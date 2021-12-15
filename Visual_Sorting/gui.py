import pygame as pg

from button import Button
from label import Label
from input_box import InputBox


class GUI:
    def __init__(self, settings, screen, sorter):
        self.settings = settings
        self.screen = screen
        self.sorter = sorter
        self.gui_elements = []
        self.gui_font = pg.font.SysFont("Console", 30)
        self.generate_gui()


    def generate_gui(self):
        start_button = Button(
            self.settings.window_padding,
            int(self.settings.screen_height - 40),
            self.settings.button_width,
            self.settings.button_height,
            pg.Color("grey"),
            pg.Color("white"),
            "Start",
            self.gui_font,
            action=self.start_sorts
        )
        self.gui_elements.append(start_button)

        restart_button = Button(
            self.settings.window_padding * 2 + self.settings.button_width,
            int(self.settings.screen_height - 40),
            self.settings.button_width,
            self.settings.button_height,
            pg.Color("grey"),
            pg.Color("white"),
            "Restart",
            self.gui_font,
            action=self.setup_new_sorts
        )
        self.gui_elements.append(restart_button)

        speed_up_button = Button(
            self.settings.window_padding * 3 + self.settings.button_width * 2, 
            int(self.settings.screen_height - 40),
            self.settings.button_width,
            self.settings.button_height,
            pg.Color("grey"),
            pg.Color("white"),
            "+Speed",
            self.gui_font,
            action=self.speed_up
        )
        self.gui_elements.append(speed_up_button)

        slow_down_button = Button(
            self.settings.window_padding * 4 + self.settings.button_width * 3, 
            int(self.settings.screen_height - 40),
            self.settings.button_width,
            self.settings.button_height,
            pg.Color("grey"), 
            pg.Color("white"), 
            "-Speed", 
            self.gui_font, 
            action=self.slow_down
        )
        self.gui_elements.append(slow_down_button)

        bubble_label = Label(
            self.settings.window_padding,
            self.settings.window_padding,
            self.settings.label_width,
            self.settings.label_height,
            pg.Color("grey"),
            pg.Color("cyan"),
            "Bubble",
            self.gui_font,
            align="center",
            border=2
        )
        self.gui_elements.append(bubble_label)

        selection_label = Label(
            self.settings.window_padding,
            self.settings.window_padding + self.settings.label_height,
            self.settings.label_width,
            self.settings.label_height,
            pg.Color("grey"),
            pg.Color("cyan"),
            "Selection",
            self.gui_font,
            align="center",
            border=2
        )
        self.gui_elements.append(selection_label)

        insertion_label = Label(
            self.settings.window_padding,
            self.settings.window_padding + self.settings.label_height* 2,
            self.settings.label_width,
            self.settings.label_height,
            pg.Color("grey"),
            pg.Color("cyan"),
            "Insertion",
            self.gui_font,
            align="center",
            border=2
        )
        self.gui_elements.append(insertion_label)

        change_value_label = Label(
            self.settings.window_padding * 5 + self.settings.button_width * 4, 
            self.settings.screen_height - 50,
            150,
            40,
            pg.Color("black"),
            pg.Color("grey"),
            "Values:",
            self.gui_font,
            align="right"
        )
        self.gui_elements.append(change_value_label)

        change_value_input_box = InputBox(
            self.settings.window_padding * 6 + self.settings.button_width * 4 + 150, 
            self.settings.screen_height - 50,
            50,
            40,
            pg.Color("grey"),
            pg.Color("cyan"),
            self.gui_font,
            char_limit=2
        )
        change_value_input_box.text = str(self.settings.number_of_values)
        self.gui_elements.append(change_value_input_box)


    def start_sorts(self):
        self.sorter.sorting = not self.sorter.sorting
        if self.sorter.sorting:
            self.gui_elements[0].update_text("Pause")
        else:
            self.gui_elements[0].update_text("Start")

    def setup_new_sorts(self):
        self.sorter.sorting = False
        self.sorter.bubble_sorting = True
        self.sorter.selection_sorting = True
        self.sorter.insertion_sorting = True
        self.sorter.setup_values()
        self.gui_elements[0].update_text("Start")

    def speed_up(self):
        if self.settings.sort_speed < 300:
            self.settings.sort_speed += 10

    def slow_down(self):
        if self.settings.sort_speed > 10:
            self.settings.sort_speed -= 10

    def update_number_of_values(self):
        self.settings.number_of_values = int(self.gui_elements[-1].text)
        self.sorter.sorting = False
        self.settings.update_screen_size()
        self.sorter.setup_values()
        pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))