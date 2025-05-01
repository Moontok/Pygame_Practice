import pygame as pg

from food import Food
from game_manager import GameManager
from snake_enums import Color, Direction, ImageFile
from square import Square


class Snake:
    """Class to manage the snake."""

    def __init__(self, gm: GameManager) -> None:
        self.gm: GameManager = gm
        self.head: Segment = Segment(self.gm, gm.center(), Direction.up)
        self.segments: list = [self.head]

        self.head_img = pg.image.load(ImageFile.head)
        self.body_img = pg.image.load(ImageFile.body)
        self.tail_img = pg.image.load(ImageFile.tail)

        self.head_img = pg.transform.scale(self.head_img, (gm.size, gm.size))
        self.body_img = pg.transform.scale(self.body_img, (gm.size, gm.size))
        self.tail_img = pg.transform.scale(self.tail_img, (gm.size, gm.size))

    def draw(self) -> None:
        """Render the snake to the screen."""

        for index, segment in enumerate(self.segments):
            degree: int = self.get_rotation(segment.direction)
            if index == 0:
                body_part: pg.Surface = pg.transform.rotate(self.head_img, degree)
            elif index == len(self.segments) - 1:
                body_part: pg.Surface = pg.transform.rotate(self.tail_img, degree)
            else:
                if segment.direction in (Direction.up, Direction.down):
                    body_part: pg.Surface = self.body_img
                else:
                    body_part: pg.Surface = pg.transform.rotate(self.body_img, 90)
        
            self.gm.screen.blit(body_part, (segment.x, segment.y))

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
        segment: Segment = Segment(self.gm, (x_loc, y_loc), end.direction)

        self.segments.append(segment)

    def wall_hit(self) -> bool:
        """Check if the snake head is colliding with a wall."""

        x_hit: bool = self.head.x < 0 or self.head.x >= self.gm.width        
        y_hit: bool = self.head.y < 0 or self.head.y >= self.gm.height        

        return x_hit or y_hit

    def overlap(self, point: tuple) -> bool:
        """Check if point is overlapping with the snake."""

        for index, segment in enumerate(self.segments):
            if index > 2 and point == segment.get_pos():
                return True
        return False
    
    def body_hit(self) -> bool:
        """Check if snake is colliding with itself."""
        
        return self.overlap(self.head.get_pos())
    
    def food_hit(self, food: Food) -> bool:
        """Check if head overlaps food."""

        return self.head.get_pos() == food.get_pos()
    
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


class Segment(Square):
    """A class to represent a segment of the snake."""

    def __init__(
        self,
        gm: GameManager,
        pos: tuple,
        direction: Direction,
    ) -> None:
        
        super().__init__(gm, pos, Color.snake)
        self.direction: Direction = direction