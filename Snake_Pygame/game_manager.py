import pygame as pg

from snake_enums import FontFiles, State


class GameManager:
    """Manages the game and state."""

    def __init__(self):
        self.width: int = 800
        self.height: int = self.width
        self.speed: int = 10
        self.size: int = self.width // 20
        self.screen: pg.Surface = pg.display.set_mode((self.width, self.height))
        self.clock: pg.time.Clock = pg.time.Clock()

        self.state: int = State.menu

        self.large_font: pg.font.Font = pg.font.Font(FontFiles.large, 72)
        self.small_font: pg.font.Font = pg.font.Font(FontFiles.small, 24)

        self.text: dict = {
            "menu": [
                "Press 'ENTER' to",
                "play the game.",
            ],
            "game_over": [
                "Thanks for playing!",
                "Press 'ENTER' to go to the main menu.",
            ],
        }


    def center(self) -> tuple:
        """Returns the center of the screen."""

        return (self.width // 2, self.height // 2)
    
    def tick(self) -> None:
        """Controls the frame rate of the game."""

        self.clock.tick(self.speed)
