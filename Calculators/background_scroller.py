import pygame as pg


class Background:
    """Class that creates a seamless background scrolling effect."""
    def __init__(self, image, speed_y):
        self.background = pg.image.load(image)
        self.background_rect = self.background.get_rect()
        self.speed_y = speed_y

    def draw(self, screen):
        """ Draw the background to the screen. """

        if self.background_rect.y > self.background_rect.height:
            self.background_rect.y = 0
        else:
            self.background_rect.y += self.speed_y
            
        screen.blit(self.background, self.background_rect)
        second_background = self.background_rect[:]
        
        second_background[1] -= second_background[3]
        screen.blit(self.background, second_background)
