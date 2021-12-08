import pygame as pg

class Label:
    def __init__(self, x, y, width, height, color, text_color, text, font, align="left", border=0):
        self.rect = pg.Rect(x, y, width, height)
        self.color = color
        self.text_color = text_color
        self.font = font
        self.text = font.render(text, True, text_color)
        self.border = border

        if align == "right":
            self.text_rect = self.text.get_rect(right=self.rect.right, centery=self.rect.centery)
        elif align == "center":
            self.text_rect = self.text.get_rect(center=self.rect.center)
        else:
            self.text_rect = self.text.get_rect(x=self.rect.x, centery=self.rect.centery)


    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect, self.border)
        screen.blit(self.text, self.text_rect)


    def update_text(self, text):
        self.text = self.font.render(text, True, self.text_color)

