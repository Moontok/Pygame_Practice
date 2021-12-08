import pygame as pg
from button import Button
from input_box import Input_Box
from label import Label

def main():
    pg.init()
    pg.display.set_caption("Calculator")

    screen = pg.display.set_mode((400, 160))
    clock = pg.time.Clock()

    app_running = True
    gui_font = pg.font.SysFont("Console", 30)

    input_label = Label(10, 10, 120, 41, pg.Color("grey"), pg.Color("white"), "Input:", gui_font, align="right")
    input_box = Input_Box(130, 10, 260, 40, pg.Color("grey"), pg.Color("cyan"), gui_font)

    output_label = Label(10, 110, 380, 40, pg.Color("grey"), pg.Color("white"), "Output", gui_font, align="center", border=2)
    calculate_button = Button(10, 60, 380, 40, pg.Color("grey"), pg.Color("white"), "CALCULATE", gui_font, action=lambda:calculate(input_box, output_label))

    while app_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                app_running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                input_box.check_if_clicked()
            if event.type == pg.KEYDOWN and input_box.input_active:
                if event.key == pg.K_BACKSPACE:
                    input_box.delete_char()
                elif event.key == pg.K_RETURN:
                    input_box.input_active = False
                else:
                    input_box.add_char(event.unicode)          

        screen.fill(pg.Color("black"))
        input_label.draw(screen)
        input_box.draw(screen)
        calculate_button.draw(screen)
        output_label.draw(screen)

        pg.display.update()
        clock.tick(60)
    pg.quit()
    exit()

def calculate(input_box, output_label):
    result = eval(input_box.text_input)
    output_label.update_text(str(result))


if __name__ == "__main__":
    main()