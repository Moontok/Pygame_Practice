class Segment:
    """
    A class to represent a segment of the snake.
    """

    def __init__(self, pos, direction):
        self.x = pos[0]
        self.y = pos[1]
        self.direction = direction

    def get_pos(self):
        """
        Get the position of the segment.
        """

        return (self.x, self.y)