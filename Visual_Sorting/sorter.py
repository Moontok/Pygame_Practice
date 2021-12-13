import random as rm
import pygame as pg


class Sorter:
    def __init__(self, size, shape_width):
        self.size = size
        self.shape_width = shape_width
        self.values = []

        self.generate_values()

    def generate_values(self):
        """Generate random height values."""
        for i in range(self.size):
            height = rm.randint(1, 100)
            rectangle = Value(height, pg.Color("grey"))
            self.values.append(rectangle)

    def draw(self, screen, x, y):
        for rectangle in self.values:
            rectangle.draw(screen, x, y, self.shape_width)
            x += self.shape_width + 2

class Value:
    def __init__(self, height, color):
        self.height = height
        self.color = color

    def draw(self, screen, x, y, width):

        pg.draw.rect(screen, self.color, [x, y - self.height, width, self.height])