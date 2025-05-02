import pygame as pg

from food import Food
from game_manager import GameManager
from snake_enums import Color, Direction, ImageFile
from square import Square


class Snake:
    """Class to manage the snake."""

    def __init__(self, gm: GameManager) -> None:
        self.gm: GameManager = gm
        self.head: Segment = Segment(self.gm, gm.center(), Direction.up, ImageFile.head)
        
        tail: Segment = Segment(
            self.gm,
            (self.head.x, self.head.y + gm.size),
            Direction.up,
            ImageFile.tail,
        )
        
        self.segments: list = [self.head, tail]

    def draw(self) -> None:
        """Render the snake to the screen."""

        for segment in self.segments:        
            segment.draw()

    def move(self) -> None:
        """Move all segments forward thier direction."""

        for segment in self.segments:
            segment.x += segment.size * segment.direction[0]
            segment.y += segment.size * segment.direction[1]

        self.update_directions()

    def update_directions(self) -> None:
        """Update direction of each segment starting with the back."""

        for index in range(len(self.segments)-1, 0, -1):
            before: Segment = self.segments[index - 1]
            self.segments[index].direction = before.direction

    def grow(self) -> None:
        """Add a new segment to the back of the snake."""

        end: Segment = self.segments[-1]
        x_loc: int = (end.x + self.gm.size * -end.direction[0])
        y_loc: int = (end.y + self.gm.size * -end.direction[1])
        segment: Segment = Segment(
            self.gm,
            (x_loc, y_loc),
            end.direction,
        )

        self.segments.append(segment)

    def wall_hit(self) -> bool:
        """Check if the snake head is colliding with a wall."""

        x_hit: bool = self.head.x < 0 or self.head.x >= self.gm.width        
        y_hit: bool = self.head.y < 0 or self.head.y >= self.gm.height        

        return x_hit or y_hit
    
    def body_hit(self, point: tuple = None) -> bool:
        """Check if if point is colliding with the snake body."""
        
        if point is None:
            point: tuple = self.head.get_pos()
            start_index: int = 2
        else:
            start_index: int = 0

        for index in range(start_index, len(self.segments)):
            segment: Segment = self.segments[index]
            if segment.get_pos() == point:
                return True
        return False
    
    def food_hit(self, food: Food) -> bool:
        """Check if head overlaps food."""

        return self.head.get_pos() == food.get_pos()


class Segment(Square):
    """A class to represent a segment of the snake."""

    def __init__(
        self,
        gm: GameManager,
        pos: tuple,
        direction: Direction,
        image_file: str = ImageFile.body,
    ) -> None:
        
        super().__init__(gm, pos, direction, Color.snake, image_file)