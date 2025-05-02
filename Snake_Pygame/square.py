import pygame as pg

from game_manager import GameManager
from snake_enums import Direction


class Square:
    """A class for a square on the screen."""

    def __init__(
        self,
        gm: GameManager,
        pos: tuple,
        direction: Direction,
        color: tuple,
        image_file: str,
    ) -> None:
        self.gm: GameManager = gm
        self.x: int = int(pos[0])
        self.y: int = int(pos[1])
        self.size: int = gm.size
        self.color: tuple = color
        self.direction: Direction = direction

        self.image: pg.Surface = pg.image.load(image_file)
        self.image: pg.Surface = pg.transform.scale(self.image, (gm.size, gm.size))
        self.surface: pg.Surface = None

    def get_pos(self) -> tuple:
        """Get the position of the square."""

        return (self.x, self.y)
    
    def draw(self) -> None:
        """Render the square to the screen."""

        degree: int = self.get_rotation(self.direction)
        self.surface = pg.transform.rotate(self.image, degree)
        self.gm.screen.blit(self.surface, (self.x, self.y))
    
    def get_rotation(self, direction: tuple) -> None:
        """Orient the body part of the snake."""

        if direction == Direction.up:
            return 0
        elif direction == Direction.down:
            return 180
        elif direction == Direction.left:
            return 90
        elif direction == Direction.right:
            return 270