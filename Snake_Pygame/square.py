import pygame as pg

from game_manager import GameManager


class Square:
    """A class for a square on the screen."""

    def __init__(
        self,
        gm: GameManager,
        pos: tuple,
        color: tuple,
    ) -> None:
        self.gm: GameManager = gm
        self.x: int = int(pos[0])
        self.y: int = int(pos[1])
        self.size: int = gm.size
        self.color: tuple = color

    def get_pos(self) -> tuple:
        """Get the position of the square."""

        return (self.x, self.y)
    
    def draw(self) -> None:
        """Render the square to the screen."""

        rect: pg.Rect = pg.Rect(self.x, self.y, self.size, self.size)
        pg.draw.rect(self.gm.screen, self.color, rect)