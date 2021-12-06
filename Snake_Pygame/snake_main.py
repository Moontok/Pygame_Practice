import pygame as pg

from game_settings import Settings
from snake import Snake


def main():
    pg.init()

    settings = Settings()

    screen = pg.display.set_mode((settings.window_width, settings.window_height))
    clock = pg.time.Clock()

    game_over = False

    pg.display.set_caption("Snake")
    screen.fill((0, 0, 0))

    segment_size = 10
    snake = Snake((settings.window_width - segment_size) / 2, (settings.window_height - segment_size) / 2, segment_size)

    while not game_over:
        clock.tick(settings.game_speed)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake.set_head_direction(0, 1)
            if event.key == pg.K_DOWN:
                snake.set_head_direction(0, -1)
            if event.key == pg.K_RIGHT:
                snake.set_head_direction(1, 0)
            if event.key == pg.K_LEFT:
                snake.set_head_direction(-1, 0)

        screen.fill((0, 0, 0))
        snake.move_snake()
        snake.draw_snake(screen)

        pg.display.update()

    pg.quit()


if __name__ == "__main__":
    main()