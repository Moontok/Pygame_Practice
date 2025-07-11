import json
import sys

import pygame as pg

from food import Food
from game_manager import GameManager
from snake import Snake
from snake_enums import AudioFile, Color, Direction, ImageFile, State


def main():
    pg.init()

    gm: GameManager = GameManager()

    pg.display.set_caption("Snake")

    pg.mixer.music.load(AudioFile.music)
    pg.mixer.music.set_volume(0.1)
    pg.mixer.music.play(-1)

    while gm.state != State.end_game:
        try:
            menu_loop(gm)
            game_loop(gm)
            game_over_loop(gm)
        except UnboundLocalError:
            break

    pg.quit()
    sys.exit()


def menu_loop(gm: GameManager) -> None:
    """The main menu loop."""

    gm.high_score = load_highscore()

    while gm.state == State.menu:
        process_events(gm)

        background = load_background(gm)

        # Update the screen
        gm.screen.blit(background, (0, 0))
        menu_text(gm)
        pg.display.flip()


def game_loop(gm: GameManager) -> None:
    """The game loop."""

    gm.score = 0
    snake: Snake = Snake(gm)
    food: Food = Food(gm, (0, 0))
    food.move()

    while gm.state == State.in_game:
        gm.tick()
        process_events(gm, snake)

        background = load_background(gm)

        snake.move()

        process_collisions(gm, snake, food)

        # Update the screen
        gm.screen.blit(background, (0, 0))
        food.draw()
        snake.draw()
        
        score_text(gm)
        pg.display.flip()


def game_over_loop(gm: GameManager) -> None:
    """The game over loop."""

    if gm.score > gm.high_score:
        gm.high_score = gm.score
        save_highscore(gm.score)
    
    while gm.state == State.game_over:
        process_events(gm)

        background: pg.Surface = load_background(gm)

        # Update the screen
        gm.screen.blit(background, (0, 0))
        
        game_over_text(gm)
        score_text(gm)
        pg.display.flip()


def load_background(gm: GameManager) -> pg.Surface:
    """Load the background image."""

    if gm.state == State.menu:
        file: str = ImageFile.menu_bg
    elif gm.state == State.in_game:
        file: str = ImageFile.game_bg
    elif gm.state == State.game_over:
        file: str = ImageFile.game_over_bg

    background = pg.image.load(file)
    background = pg.transform.scale(background, (gm.width, gm.height))
    return background


def process_collisions(gm: GameManager, snake: Snake, food: Food) -> None:
    """Process collisions."""

    if snake.wall_hit() or snake.body_hit():
        gm.state = State.game_over
    elif snake.food_hit(food):
        gm.score += 1
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


def menu_text(gm: GameManager) -> None:
    """Display the menu text."""

    gm.screen.blit(
        gm.small_font.render("Press Enter to play.", True, Color.text),
        (gm.width * .50, gm.height * .94, gm.width, gm.height),
    )


def score_text(gm: GameManager) -> None:
    """Display the game text."""
    
    gm.screen.blit(
        gm.small_font.render(f"Score: {gm.score}", True, Color.text),
        (gm.width * .1, gm.height * .04, gm.width, gm.height),
    )
    gm.screen.blit(
        gm.small_font.render(f"High Score: {gm.high_score}", True, Color.text),
        (gm.width * .60, gm.height * .04, gm.width, gm.height),
    )


def game_over_text(gm: GameManager) -> None:
    """Display the game over text."""

    gm.screen.blit(
        gm.small_font.render("Press Enter to play again.", True, Color.text),
        (gm.width * .1, gm.height * .93, gm.width, gm.height),
    )


def load_highscore() -> list:
    """Load the high score."""

    try:
        with open("high_scores.json", "r") as file:
            data = json.load(file)
            return data["high_score"]
    except FileNotFoundError:
        with open("high_scores.json", "w") as file:
            json.dump({"high_score": 0}, file)
            return 0
        

def save_highscore(score: int) -> None:
    """Set the high score."""

    with open("high_scores.json", "w") as file:
        json.dump({"high_score": score}, file)


if __name__ == "__main__":
    main()