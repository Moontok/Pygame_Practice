from numpy import rot90
from pygame import draw


class Block:
    """Creates a block for the Tetris game.

    Different Block Types:\n
    \t-Column Shape = 0\n
    \t-Backward L Shape = 1\n
    \t-L Shape = 2\n
    \t-Short T Shape = 3\n
    \t-Square Shape = 4  
    """

    # List of blocks
    # 0 - Column, 1 - Backward L, 2 - L, 3 - T, 4 - Square    
    blocks = [
        [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
        [[0, 1, 1], [0, 1, 0], [0, 1, 0]],
        [[1, 1, 0], [0, 1, 0], [0, 1, 0]],
        [[0, 0, 0], [1, 1, 1], [0, 1, 0]],
        [[1, 1], [1, 1]]
    ]

    def __init__(self, x, y, block_type, size):
        self.x = x
        self.y = y
        self.shape = Block.blocks[block_type]
        self.size = size

    def rotate_left(self):
        self.shape = rot90(self.shape).tolist()

    def rotate_right(self):
        self.shape = rot90(self.shape, axes=(1,0)).tolist()

    def shape(self):
        return self.shape

    def draw_shape(self, screen):
        length = len(self.shape)
        for y in range(length):
            for x in range(length):
                if self.shape[y][x] == 1:
                    draw.rect(screen, (255, 255, 255), [self.x + x * self.size, self.y + y * self.size, self.size - 2, self.size - 2])




