import pygame as pg

from random import randrange

class Food:
    """
    Food object to be consumed by snake.
    """

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

        self.egg = pg.image.load("images/egg.png")
        self.egg = pg.transform.scale(self.egg, (size, size))

    def move_food_random(self, screen, snake):
        """
        Move food item at random location on screen.
        """

        finding_new_location = True

        while finding_new_location:
            self.x = randrange(0, int(screen.get_width() - self.size), self.size)
            self.y = randrange(0, int(screen.get_height() - self.size), self.size)

            finding_new_location = False

            for segment in snake.segments:
                if segment.x == self.x and segment.y == self.y:
                    finding_new_location = True
                    break

    def draw_food(self, screen):
        """
        Render food to the screen.
        """

        screen.blit(self.egg, [self.x, self.y, self.size, self.size])

    def get_pos(self):
        """
        Get the position of the food.
        """

        return (self.x, self.y)

