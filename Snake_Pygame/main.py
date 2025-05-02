import sys

import pygame as pg

from food import Food
from game_manager import GameManager
from snake import Snake
from snake_enums import AudioFile, Color, Direction, FontFiles, ImageFile, State


def main():
    pg.init()

    gm: GameManager = GameManager()
    pg.display.set_caption("Snake - by Zack Spink")

    pg.mixer.music.load(AudioFile.music)
    pg.mixer.music.set_volume(0.1)
    pg.mixer.music.play(-1)

    while not gm.state == State.end_game:
        menu_loop(gm)
        game_loop(gm)
        game_over_loop(gm)

    pg.quit()
    sys.exit()


def menu_loop(gm: GameManager) -> None:
    """The main menu loop."""
    
    while gm.state == State.menu:
        process_events(gm)

        background = pg.image.load(ImageFile.menu_bg)
        background = pg.transform.scale(background, (gm.width, gm.height))

        gm.screen.blit(background, (0, 0))
        display_text(
            gm.text["menu"], gm.small_font, gm, Color.text, (gm.width * .63, gm.height * .89)
        )
        pg.display.flip()


def game_loop(gm: GameManager) -> None:
    """The game loop."""


    snake: Snake = Snake(gm)
    food: Food = Food(gm, (0, 0))
    food.move()

    while gm.state == State.in_game:
        gm.tick()
        process_events(gm, snake)

        background = pg.image.load(ImageFile.game_bg)
        background = pg.transform.scale(background, (gm.width, gm.height))

        snake.move()

        process_collisions(gm, snake, food)

        gm.screen.blit(background, (0, 0))
        food.draw()
        snake.draw()
        pg.display.flip()


def game_over_loop(gm: GameManager) -> None:
    """The game over loop."""
    
    while gm.state == State.game_over:
        process_events(gm)

        background = pg.image.load(ImageFile.game_over_bg)
        background = pg.transform.scale(background, (gm.width, gm.height))

        gm.screen.blit(background, (0, 0))
        display_text(
            gm.text["game_over"], gm.small_font, gm, Color.text, (gm.width * .1, gm.height * .85)
        )
        pg.display.flip()


def process_collisions(gm: GameManager, snake: Snake, food: Food) -> None:
    """Process collisions."""

    if snake.wall_hit() or snake.body_hit():
        gm.state = State.game_over
    elif snake.food_hit(food):
        pg.mixer.Sound(AudioFile.eat).play()
        snake.grow()
        food.move()

        while snake.body_hit(food.get_pos()):
            food.move()


def process_events(gm: GameManager, snake: Snake=None) -> None:
    """Process events for the game."""

    for event in pg.event.get():
        if event.type == pg.QUIT:
            gm.state = State.end_game
            break
        if gm.state != State.in_game and event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            gm.state = State.next_state(gm.state)
            break

        if snake is not None and event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and snake.head.direction != Direction.down:
                snake.head.direction = Direction.up
            elif event.key == pg.K_DOWN and snake.head.direction != Direction.up:
                snake.head.direction = Direction.down
            elif event.key == pg.K_RIGHT and snake.head.direction != Direction.left:
                snake.head.direction = Direction.right
            elif event.key == pg.K_LEFT and snake.head.direction != Direction.right:
                snake.head.direction = Direction.left


def display_text(lines_of_text: list, font: pg.font.Font, gm: GameManager, color: str, pos: tuple) -> None:
    """Displays a list text to the screen."""
    
    font_size = 24
    line_height = font_size + 1

    for line_number, line_text in enumerate(lines_of_text):
        text = font.render(line_text, True, color)
        gm.screen.blit(
            text,
            (pos[0], pos[1] + line_number * line_height, gm.width - 10, gm.height - 10)
        )

if __name__ == "__main__":
    main()