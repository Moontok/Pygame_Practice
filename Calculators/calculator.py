import pygame as pg
import sys

from button import Button
from input_box import InputBox
from label import Label
from background_scroller import Background


def main():
    pg.init()
    pg.display.set_caption("Calculator")

    screen = pg.display.set_mode((400, 160))
    clock = pg.time.Clock()

    app_running = True
    gui_font = pg.font.SysFont("Console", 30)

    input_label = Label(
        10, 10, 120, 41,
        pg.Color("grey"),
        pg.Color("white"),
        "Input:",
        gui_font,
        align="right"
    )
    input_box = InputBox(
        130, 10, 260, 40,
        pg.Color("grey"),
        pg.Color("cyan"),
        gui_font
    )

    output_label = Label(
        10, 110, 380, 40,
        pg.Color("grey"),
        pg.Color("white"),
        "",
        gui_font,
        align="center",
        border=2
    )
    calculate_button = Button(
        10, 60, 380, 40,
        pg.Color("grey"),
        pg.Color("white"),
        "CALCULATE",
        gui_font,
        action=lambda: calculate(input_box, output_label)
    )

    # Images
    bg_image = "images/background.png"
    background = Background(bg_image, 5)

    while app_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                app_running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                input_box.check_if_clicked()
            if event.type == pg.KEYDOWN and input_box.input_active:
                if event.key == pg.K_BACKSPACE:
                    input_box.delete_char()
                elif event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                    input_box.input_active = False
                    calculate(input_box, output_label)
                else:
                    input_box.add_char(event.unicode)

        screen.fill(pg.Color("black"))
        background.draw(screen)
        input_label.draw(screen)
        input_box.draw(screen)
        calculate_button.draw(screen)
        output_label.draw(screen)

        pg.display.update()
        clock.tick(60)
        
    pg.quit()
    sys.exit()


def calculate(input_box, output_label):
    """ Calculates and displayes the result of the entered expression. """
    # potential security issue: eval() ex. eval(pythong code)
    # validating input in input_box.add_char()
    try:
        result = eval(input_box.text)
    except ZeroDivisionError:
        result = "Divide by Zero Error"
    except SyntaxError:
        result = "Invalid Expression"
    except NameError:  # For base calc upgrade "box" and eval no variable
        result = "Invalid Expression"

    output_label.update_text(str(result))
    input_box.clear_text()

if __name__ == "__main__":
    main()
