import random as rm
import pygame as pg
import copy


class Sorter:
    def __init__(self, size, shape_width):
        self.size = size
        self.shape_width = shape_width
        self.values = []

        self.generate_values()
        
        self.values_for_bubble = copy.deepcopy(self.values)
        self.values_for_selection = copy.deepcopy(self.values)
        self.values_for_insertion = copy.deepcopy(self.values)

        self.bubble_generator = self.bubble_sort()
        self.selection_generator = self.selection_sort()
        self.insertion_generator = self.insertion_sort()
        self.sorting = True

    def generate_values(self):
        """Generate random height values."""

        # Random
        for _ in range(self.size):
            height = rm.randint(1, 100)
            rectangle = Value(height, pg.Color("grey"))
            self.values.append(rectangle)

        # Reverse sorted
        # values = [x for x in range(self.size, 0, -1)]
        # for height in values:
        #     rectangle = Value(height, pg.Color("grey"))
        #     self.values.append(rectangle)

        # Sorted
        # values = [x for x in range(self.size)]
        # for height in values:
        #     rectangle = Value(height, pg.Color("grey"))
        #     self.values.append(rectangle)

    
    def draw_bubble(self, screen, x, y):
        for rectangle in self.values_for_bubble:
            rectangle.draw(screen, x, y, self.shape_width)
            x += self.shape_width + 2
    
    def draw_selection(self, screen, x, y):
        for rectangle in self.values_for_selection:
            rectangle.draw(screen, x, y, self.shape_width)
            x += self.shape_width + 2

    def draw_insertion(self, screen, x, y):
        for rectangle in self.values_for_insertion:
            rectangle.draw(screen, x, y, self.shape_width)
            x += self.shape_width + 2   

    def bubble_sort(self):
        done = False
        sorted = 0

        while not done:
            yield True
            done = True
            for k in range(len(self.values_for_bubble) - sorted - 1):
                yield True
                self.values_for_bubble[k].color = pg.Color("yellow")  #############
                self.values_for_bubble[k + 1].color = pg.Color("cyan")  #############
                yield True
                if self.values_for_bubble[k].height > self.values_for_bubble[k + 1].height:
                    yield True
                    self.swap(self.values_for_bubble, k, k + 1)
                    done = False
                    self.values_for_bubble[k + 1].color = pg.Color("yellow")  #############
                self.values_for_bubble[k].color = pg.Color("grey")  #############             
                
            sorted += 1
            self.values_for_bubble[-sorted].color = pg.Color("green")  #############

        if sorted < len(self.values_for_bubble):
            yield True
            for i in range(len(self.values_for_bubble) - sorted):
                self.values_for_bubble[i].color = pg.Color("green")  #############
        yield False

    def selection_sort(self):
        for i in range(len(self.values_for_selection)):
            yield True
            best = i
            
            self.values_for_selection[i].color = pg.Color("yellow")  #############
            for j in range(i + 1, len(self.values_for_selection)):
                yield True
                self.values_for_selection[j].color = pg.Color("cyan")  #############
                yield True
                if self.values_for_selection[j].height < self.values_for_selection[best].height:
                    if best != i:
                        self.values_for_selection[best].color = pg.Color("grey")  #############
                    self.values_for_selection[j].color = pg.Color("cyan")  #############
                    best = j
                if best != i:
                    self.values_for_selection[best].color = pg.Color("red")
                self.values_for_selection[j].color = pg.Color("grey")  #############
            yield True
            self.swap(self.values_for_selection, i, best)
            self.values_for_selection[i].color = pg.Color("green")  #############
            # if best == i:
            #     break
        yield False

    def insertion_sort(self):
        for j in range(1, len(self.values_for_insertion)):
            yield True
            k = j - 1
            self.values_for_insertion[j].color = pg.Color("yellow")  #############
            self.values_for_insertion[k].color = pg.Color("cyan")  #############
            while k >= 0 and self.values_for_insertion[k].height > self.values_for_insertion[k + 1].height:
                yield True
                self.values_for_insertion[k + 1].color = pg.Color("yellow")  #############                
                self.values_for_insertion[k].color = pg.Color("cyan")  #############
                yield True
                self.swap(self.values_for_insertion, k, k + 1)

                self.values_for_insertion[k + 1].color = pg.Color("cyan")  #############                
                self.values_for_insertion[k].color = pg.Color("yellow")  #############
                self.values_for_insertion[k + 1].color = pg.Color("green")  #############
                self.values_for_insertion[k].color = pg.Color("green")  #############
                k -= 1
            self.values_for_insertion[k + 1].color = pg.Color("green")  #############
            if k > 0:
                self.values_for_insertion[k].color = pg.Color("green")  #############
        yield False

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