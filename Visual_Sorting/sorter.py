import random as rm
import pygame as pg
import copy


class Sorter:
    def __init__(self, settings):
        self.settings = settings
        self.values = []
        self.values_for_bubble = []
        self.values_for_selection = []
        self.values_for_insertion = []
        self.bubble_generator = None
        self.selection_generator = None
        self.insertion_generator = None
        self.sorting = False
        self.bubble_sorting = True
        self.selection_sorting = True
        self.insertion_sorting = True

        self.setup_values()

    def setup_values(self):
        self.values.clear()
        for _ in range(self.settings.number_of_values):
            height = rm.randint(1, self.settings.value_height)
            rectangle = Value(height, pg.Color("grey"))
            self.values.append(rectangle)
        
        self.values_for_bubble = copy.deepcopy(self.values)
        self.values_for_selection = copy.deepcopy(self.values)
        self.values_for_insertion = copy.deepcopy(self.values)

        self.bubble_generator = self.bubble_sort()
        self.selection_generator = self.selection_sort()
        self.insertion_generator = self.insertion_sort()
    
    def draw_bubble(self, screen, x, y):
        for rectangle in self.values_for_bubble:
            rectangle.draw(screen, x, y, self.settings.value_width)
            x += self.settings.value_width + self.settings.value_horizontal_padding
    
    def draw_selection(self, screen, x, y):
        for rectangle in self.values_for_selection:
            rectangle.draw(screen, x, y, self.settings.value_width)
            x += self.settings.value_width + self.settings.value_horizontal_padding

    def draw_insertion(self, screen, x, y):
        for rectangle in self.values_for_insertion:
            rectangle.draw(screen, x, y, self.settings.value_width)
            x += self.settings.value_width + self.settings.value_horizontal_padding

    def draw_quick(self, screen, x, y):
        for rectangle in self.values_for_quicksort:
            rectangle.draw(screen, x, y, self.settings.value_width)
            x += self.settings.value_width + self.settings.value_horizontal_padding 

    def bubble_sort(self):
        done = False
        sorted = 0

        while not done:
            yield True  #############
            done = True
            self.values_for_bubble[-sorted - 1].color = pg.Color("grey")  ############# 
            for k in range(len(self.values_for_bubble) - sorted - 1):
                yield True
                if k > 0:  #############
                    self.values_for_bubble[k - 1].color = pg.Color("grey")  ############# 
                self.values_for_bubble[k].color = pg.Color("yellow")  #############
                self.values_for_bubble[k + 1].color = pg.Color("cyan")  #############
                if self.values_for_bubble[k].height > self.values_for_bubble[k + 1].height:
                    yield True  #############
                    self.swap(self.values_for_bubble, k, k + 1)
                    done = False
            sorted += 1
            self.values_for_bubble[-sorted].color = pg.Color("green")  ############# 

        if sorted < len(self.values_for_bubble):  #############
            yield True  #############
            for i in range(len(self.values_for_bubble) - sorted):  #############
                self.values_for_bubble[i].color = pg.Color("green")  #############
        yield False  #############

    def selection_sort(self):
        for i in range(len(self.values_for_selection)):
            yield True  #############
            best = i
            self.values_for_selection[-1].color = pg.Color("grey")  #############
            self.values_for_selection[i].color = pg.Color("yellow")  #############
            for j in range(i + 1, len(self.values_for_selection)):
                yield True  #############
                if j - 1 > i and j - 1 != best:  #############
                    self.values_for_selection[j - 1].color = pg.Color("grey")  #############
                self.values_for_selection[j].color = pg.Color("cyan")  #############
                if self.values_for_selection[j].height < self.values_for_selection[best].height:
                    if best != i:  #############
                        self.values_for_selection[best].color = pg.Color("grey")  #############
                    best = j
                    if best != i:  #############
                        self.values_for_selection[best].color = pg.Color("red")  #############
            yield True  #############
            self.swap(self.values_for_selection, i, best)
            self.values_for_selection[i].color = pg.Color("green")  #############
            if best != i:
                self.values_for_selection[best].color = pg.Color("grey")  #############
        yield False  #############

    def insertion_sort(self):        
        self.values_for_insertion[0].color = pg.Color("green")
        for j in range(1, len(self.values_for_insertion)):
            yield True  #############
            k = j - 1
            self.values_for_insertion[j].color = pg.Color("yellow")  #############
            while k >= 0 and self.values_for_insertion[k].height > self.values_for_insertion[k + 1].height:
                yield True  #############
                self.values_for_insertion[k].color = pg.Color("cyan")  #############
                yield True  #############
                self.swap(self.values_for_insertion, k, k + 1)
                self.values_for_insertion[k + 1].color = pg.Color("green")  #############
                self.values_for_insertion[k].color = pg.Color("yellow")  #############
                k -= 1
            self.values_for_insertion[k + 1].color = pg.Color("green")  #############
        yield False  #############

    def swap(self, values, i, j):
        """ Swap values[i] with values[j] inside of list values. """

        temp = values[i]
        values[i] = values[j]
        values[j] = temp


class Value:
    def __init__(self, height, color):
        self.height = height
        self.color = color

    def draw(self, screen, x, y, width):

        pg.draw.rect(screen, self.color, [x, y - self.height, width, self.height])