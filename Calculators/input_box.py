import pygame as pg


class Input_Box:
    def __init__(self, x, y, width, height, color, font_color, font):
        self.rect = pg.Rect(x, y, width, height)
        self.color = color
        self.inactive_color = color
        self.active_color = font_color
        self.text_input = ""
        self.font = font
        self.font_color = font_color
        self.text = None
        self.text_rect = pg.Rect(x, y, width, height)

        self.input_active = False

    
    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect, 2)
        
        self.text = self.font.render(self.text_input, True, self.font_color)
        screen.blit(self.text, (self.text_rect.x + 5, self.text_rect.y + 5))


    def delete_char(self):
        self.text_input = self.text_input[:-1]


    def add_char(self, char):
        self.text_input += char


    def check_if_clicked(self):
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):            
            self.input_active = True
            self.color = self.active_color
            self.font_color = self.active_color
        else:
            self.input_active = False
            self.color = self.inactive_color
            self.font_color = self.inactive_color
