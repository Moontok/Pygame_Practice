from pygame import draw

class Snake:
    def __init__(self, x, y, segment_size=10):
        self.segment_size = segment_size
        self.segments = [Segment(x, y, (0, 1))]
        self.color = (255, 255, 255)


    def draw_snake(self, screen):
        for segment in self.segments:
            draw.rect(screen, self.color, [segment.x, segment.y, self.segment_size, self.segment_size])


    def move_snake(self):
        for segment in self.segments:
            segment.x += self.segment_size * segment.direction[0]
            segment.y += self.segment_size * segment.direction[1]
        
        self.update_segment_directions()


    def update_segment_directions(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            segment_before = self.segments[segment_index - 1]
            new_direction = segment_before.direction
            self.segments[segment_index].direction = new_direction
            

    def add_segment(self):
        last_segment = self.segments[-1]
        x_location = last_segment.x + self.segment_size * -last_segment.direction[0]
        y_location = last_segment.y + self.segment_size * -last_segment.direction[1]
        self.segments.append(Segment(x_location, y_location, last_segment.direction))


    def colliding_with_body(self):
        head_segment = self.segments[0]
        for index, body_segment in enumerate(self.segments):
            if index > 2 and head_segment.x == body_segment.x and head_segment.y == body_segment.y:
                return True
        return False


    def colliding_with_food(self, food):
        head_segment = self.segments[0]

        if head_segment.x == food.x and head_segment.y == food.y:
            return True
        return False


    def colliding_with_walls(self, screen):
        head_segment = self.segments[0]

        if head_segment.x < 0 or head_segment.x >= screen.get_width() or head_segment.y < 0 or head_segment.y >= screen.get_height():
            return True
        return False


class Segment:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        # Up: 0, 1 Down: 0, -1 Right: 1, 0 Left: -1, 0
        self.direction = direction

