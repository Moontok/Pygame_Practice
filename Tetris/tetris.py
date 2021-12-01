import pygame as pg
from shapes import Block

def main():
    pg.init()
    screen = pg.display.set_mode((500, 620))
    pg.display.set_caption("Tetris")

    grid_size = 30
    columns = screen.get_width() // grid_size
    rows = screen.get_height() // grid_size    
    row_padding = (screen.get_width() - columns * grid_size) // 2
    column_padding = (screen.get_height() - rows * grid_size) // 2

    game_over = False
    block = Block(5 * grid_size + row_padding, 7 * grid_size + column_padding, 4, grid_size)

    while not game_over:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
        
        screen.fill((0, 0, 0))

        draw_grid(rows, columns, screen, grid_size, row_padding, column_padding)
        block.draw_shape(screen)

        pg.display.update()

    pg.quit()

def draw_grid(rows, columns, screen, grid_size, row_padding, column_padding):

    for y in range(rows):
        for x in range(columns):
            pg.draw.rect(screen, (100, 100, 100), [x * grid_size + row_padding, y * grid_size + column_padding, grid_size, grid_size], 1)


if __name__ == "__main__":
    main()