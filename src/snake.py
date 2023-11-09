import pygame
from pygame.math import Vector2


class SNAKE:
    def __init__(
            self,
            cell_size: int,
            screen
    ):
        self.cell_size = cell_size
        self.screen = screen

        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * self.cell_size)
            y_pos = int(block.y * self.cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, (183, 111, 122), block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True
