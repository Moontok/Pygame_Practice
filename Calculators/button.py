import pygame as pg

class Button:
    """ Class to creat a button for the program. """

    def __init__(self, x, y, width, height, color, text_color, text, font, action=lambda:None):
        self.rect = pg.Rect(x, y, width, height)
        self.color = color
        self.normal_color = color
        self.action = action
        self.text = font.render(text, True, text_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

        self.pressed = False
        self.elevation = 6
        self.dynamic_elevation = self.elevation
        self.original_y_pos = y
        self.bottom_rect = pg.Rect(x, y, width, self.elevation)


    def draw(self, screen):
        """ Draw the button to the screen. """

        self.rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.rect.center

        self.bottom_rect.midtop = self.rect.midtop
        self.bottom_rect.height = self.rect.height + self.dynamic_elevation

        pg.draw.rect(screen, pg.Color("darkgrey"), self.bottom_rect, border_radius=12)
        pg.draw.rect(screen, self.color, self.rect, border_radius=12)
        screen.blit(self.text, self.text_rect)
        self.check_if_clicked()


    def check_if_clicked(self):
        """ Check if the button has been clicked. """

        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    self.action()
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation

