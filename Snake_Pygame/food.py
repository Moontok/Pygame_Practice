from random import randrange
from pygame import draw

class Food:
    def __init__(self, x, y, size=10):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 255, 0)
        self.spawned = False


    def random_spawn(self, screen):
        self.x = randrange(0, int(screen.get_width()) - self.size, self.size)
        self.y = randrange(0, int(screen.get_height()) - self.size, self.size)
        self.spawned = True

    
    def draw_food(self, screen):
        draw.rect(screen, self.color, [self.x, self.y, self.size, self.size])


    def consume_food(self):
        self.spawned = False

