import pygame as pg


class GameSettings:
    def __init__(self):        
        self.number_of_values = 30
        self.value_height = 100
        self.value_width = 20
        self.value_horizontal_padding = 1
        self.value_vertical_padding = 10
        self.window_padding = 10
        self.sort_speed = 10
        self.button_width = 200
        self.button_height = 30
        self.label_width = 200
        self.label_height = self.value_height + self.value_vertical_padding
        self.min_width = (self.button_width + 10) * 4 + 240
        self.screen_width = 1
        self.screen_height = 1
        self.update_screen_size()

    def update_screen_size(self):
        self.screen_width = max(
            self.min_width,
            (
                (self.value_width + self.value_horizontal_padding) * self.number_of_values
                + self.label_width
                + self.window_padding * 3
            )
        )
        self.screen_height = (
            (self.value_height + self.value_vertical_padding) * 3
            + self.button_height * 2
            + self.window_padding * 2
        )
