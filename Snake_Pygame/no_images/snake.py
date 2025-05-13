import pygame as pg

from directions import Direction
from segment import Segment


class Snake:
    """
    Classes that manages the snake controlled by the player.
    """

    def __init__(self, pos, segment_size):
        self.segment_size = segment_size
        self.head = Segment(pos, (0, 1))
        self.segments = [self.head]


        self.head_img = pg.image.load("images/snake_head.png")
        self.body_img = pg.image.load("images/snake_body.png")
        self.tail_img = pg.image.load("images/snake_tail.png")

        # Scale images to segment size
        self.head_img = pg.transform.scale(self.head_img, (segment_size, segment_size))
        self.body_img = pg.transform.scale(self.body_img, (segment_size, segment_size))
        self.tail_img = pg.transform.scale(self.tail_img, (segment_size, segment_size))

    def draw_snake(self, screen):
        """
        Render snake to the screen.
        """

        for index, segment in enumerate(self.segments):
            if index == 0:
                if segment.direction == Direction.UP:
                    head = self.head_img
                elif segment.direction == Direction.DOWN:
                    head = pg.transform.rotate(self.head_img, 180)
                elif segment.direction == Direction.RIGHT:
                    head = pg.transform.rotate(self.head_img, 270)
                else:
                    head = pg.transform.rotate(self.head_img, 90)                
                screen.blit(head, [segment.x, segment.y, self.segment_size, self.segment_size])
            elif index == len(self.segments) - 1:
                if segment.direction == Direction.UP:
                    tail = self.tail_img
                elif segment.direction == Direction.DOWN:
                    tail = pg.transform.rotate(self.tail_img, 180)
                elif segment.direction == Direction.RIGHT:
                    tail = pg.transform.rotate(self.tail_img, 270)
                else:
                    tail = pg.transform.rotate(self.tail_img, 90)                
                screen.blit(tail, [segment.x, segment.y, self.segment_size, self.segment_size])
            else:
                if segment.direction == Direction.UP or segment.direction == Direction.DOWN:
                    body = self.body_img
                else:
                    body = pg.transform.rotate(self.body_img, 90) 
                screen.blit(body, [segment.x, segment.y, self.segment_size, self.segment_size])

    def move_snake(self):
        """
        Move each segment one size unit in its current direction and
        then update their current direction.
        """

        for segment in self.segments:
            segment.x += self.segment_size * segment.direction[0]
            segment.y += self.segment_size * segment.direction[1]
        
        self.update_segment_directions()

    def update_segment_directions(self):
        """
        Update the direction of each segment, beyond the first, to the direction
        of the segment of the index before.
        Starts from the back of the snake.
        """

        for segment_index in range(len(self.segments) - 1, 0, -1):
            segment_before = self.segments[segment_index - 1]
            new_direction = segment_before.direction
            self.segments[segment_index].direction = new_direction

    def add_segment(self):
        """
        Add a new segment to the end of the snake.
        """

        last_segment = self.segments[-1]
        x_location = last_segment.x + self.segment_size * -last_segment.direction[0]
        y_location = last_segment.y + self.segment_size * -last_segment.direction[1]
        pos = (x_location, y_location)
        new_segment = Segment(pos, last_segment.direction)

        self.segments.append(new_segment)

    def colliding_with_body(self):
        """
        Check if the head of the snake is colliding with any segment in its body.
        """

        head = self.segments[0]
        for index, body_segment in enumerate(self.segments):
            if index > 2 and head.get_pos() == body_segment.get_pos():
                return True
        return False

    def colliding_with_food(self, food):
        """
        Check if the head of the snake is colliding with Food.
        """

        head = self.segments[0]
        return head.get_pos() == food.get_pos()

    def colliding_with_walls(self, screen):
        """
        Check if the head of the snake is colliding with the borders of the screen.
        """

        head = self.segments[0]
        return head.x < 0 or head.x >= screen.get_width() or head.y < 0 or head.y >= screen.get_height()

