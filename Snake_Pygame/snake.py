from pygame import draw

class Snake:
    def __init__(self, x, y, segment_size=10):
        self.segment_size = segment_size
        self.segments = [Segment(x, y)]
        self.color = (255, 255, 255)


    def draw_snake(self, screen):
        for segment in self.segments:
            draw.rect(screen, self.color, [segment.x, segment.y, self.segment_size, self.segment_size])


    def move_snake(self):
        for segment in self.segments:
            segment.x = self.segment_size * segment.direction[0]
            segment.y = self.segment_size * segment.direction[1]


    def set_head_direction(self, x, y):
        self.segments[0].direction = x, y


class Segment:
    def __init__(self, x, y, direction=(0, 1)):
        self.x = x
        self.y = y
        # Up: 0, 1 Down: 0, -1 Right: 1, 0 Left: -1, 0
        self.direction = direction


    def set_direction(self, direction):
        self.direction = direction



