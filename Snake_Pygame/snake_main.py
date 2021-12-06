import pygame as pg

from game_settings import Settings
from snake import Snake
from food import Food


def main():
    pg.init()

    settings = Settings()

    screen = pg.display.set_mode((settings.window_width, settings.window_height))
    clock = pg.time.Clock()

    game_running = True
    game_over = True

    pg.display.set_caption("Snake")
    screen.fill((0, 0, 0))

    segment_size = 10
    snake = Snake(settings.window_width / 2, settings.window_height / 2, segment_size)
    food = Food(0, 0)
    
    menu_text = ["Hello and welcome to the game Snake!", "Press 'RETURN' to play the game."]
    display_text(menu_text, settings, screen)

    while game_running:
        if game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        game_over = False
        else:
            if not food.spawned:
                food.random_spawn(screen)

            screen.fill((0, 0, 0))
            clock.tick(settings.game_speed)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP and snake.segments[0].direction != (0, 1):
                        snake.segments[0].direction = 0, -1
                    if event.key == pg.K_DOWN and snake.segments[0].direction != (0, -1):
                        snake.segments[0].direction = 0, 1
                    if event.key == pg.K_RIGHT and snake.segments[0].direction != (-1, 0):
                        snake.segments[0].direction = 1, 0
                    if event.key == pg.K_LEFT and snake.segments[0].direction != (1, 0):
                        snake.segments[0].direction = -1, 0
            snake.move_snake()
            
            if snake.colliding_with_body() or snake.colliding_with_walls(screen):
                game_over = True
                game_over_text = ["GAME OVER!"]
                display_text(game_over_text, settings, screen)
            elif snake.colliding_with_food(food):
                snake.add_segment()
                snake.draw_snake(screen)
                food.random_spawn(screen)
            else:
                snake.draw_snake(screen)
                food.draw_food(screen)

        pg.display.update()
    pg.quit() 


def display_text(text_lines, settings, screen):
    button_font = pg.font.SysFont("Arial", 20)
    for line_number, line_text in enumerate(text_lines):
        button_text = button_font.render(line_text, True, (0, 255, 255))
        screen.blit(button_text, (10, 10 + line_number * 22, settings.window_width - 10, settings.window_width - 10))


if __name__ == "__main__":
    main()