import pygame as pg



FONT_TYPE = "Console"
FONT_SIZE = 32
FONT_COLOR = pg.Color("black")
BASE_COLOR = pg.Color("darkgray")
HIGHLIGHT_COLOR = pg.Color("lightgray")


class Label:

    def __init__(self, x, y, width, height, text):
        self.rect = pg.Rect(x, y, width, height)
        self.font = pg.font.SysFont(FONT_TYPE, FONT_SIZE, True)
        self.text = self.font.render(text, True, FONT_COLOR)

        self.text_rect = self.text.get_rect(center=self.rect.center)

    def draw(self, screen):
        pg.draw.rect(screen, HIGHLIGHT_COLOR, self.rect)
        screen.blit(self.text, self.text_rect)

    def update_text(self, text):
        self.text = self.font.render(text, True, FONT_COLOR)
        self.text_rect = self.text.get_rect(center=self.rect.center)


class Button:
    def __init__(self, x, y, width, height, text, action, **action_kwargs):

        self.rect = pg.Rect(x, y, width, height)
        self.font = pg.font.SysFont(FONT_TYPE, FONT_SIZE, True)
        self.text = self.font.render(text, True, FONT_COLOR)
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.action = action
        self.action_kwargs = action_kwargs

        self.pressed = False

    def draw(self, screen):
        self.text_rect.center = self.rect.center

        if self.pressed:
            pg.draw.rect(screen, HIGHLIGHT_COLOR, self.rect)
        else:
            pg.draw.rect(screen, BASE_COLOR, self.rect)

        screen.blit(self.text, self.text_rect)
        self.check_if_clicked()

    def check_if_clicked(self):
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0]:
                self.pressed = True
            elif self.pressed:
                self.action(**self.action_kwargs)
                self.pressed = False


class InputBox:
    def __init__(
        self, 
        x,
        y,
        width,
        height,
    ):
        self.rect = pg.Rect(x, y, width, height)

        self.text = ""
        self.font = pg.font.SysFont(FONT_TYPE, FONT_SIZE)
        self.color = BASE_COLOR
        self.rendered_text = None
        self.input_active = False
    
    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        
        self.rendered_text = self.font.render(self.text, True, FONT_COLOR)
        screen.blit(self.rendered_text, (self.rect.x + 5, self.rect.y + 5))

    def delete_char(self):
        self.text = self.text[:-1]

    def clear_text(self):
        self.text = ""

    def add_char(self, char):
        self.text += char

    def process_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.input_active = True
                self.color = HIGHLIGHT_COLOR
            else:
                self.input_active = False
                self.color = BASE_COLOR
        
        if event.type == pg.KEYDOWN and self.input_active:
            if event.key == pg.K_BACKSPACE:
                self.delete_char()
            else:
                self.add_char(event.unicode)