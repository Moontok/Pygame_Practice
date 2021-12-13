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


    def selection_sort(self):
        values = self.values
        for i in range(len(values)):
            best = i

            self.values[i].color = pg.Color("yellow")  #############

            for j in range(i + 1, len(values)):
                
                values[j].color = pg.Color("cyan")  #############

                if values[j].height < values[best].height:
                    if best != i:
                        values[best].color = pg.Color("grey")  #############
                    values[j].color = pg.Color("cyan")  #############
                    best = j
                values[j].color = pg.Color("grey")  #############
                if best != i:
                    self.values[best].color = pg.Color("red")
                print(values)
                yield values

            self.swap(self.values, i, best) 
        yield values

    def swap(self, values, i, j):
        """ Swap values[i] with values[j] inside of list values. """

        temp = values[i]
        values[i] = values[j]
        values[j] = temp

        values[j].color = pg.Color("grey")  #############


class Value:
    def __init__(self, height, color):
        self.height = height
        self.color = color

    def draw(self, screen, x, y, width):

        pg.draw.rect(screen, self.color, [x, y - self.height, width, self.height])