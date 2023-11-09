import pygame
import random
from pygame.math import Vector2


class FRUIT:
    def __init__(
            self,
            cell_size: int,
            cell_number: int,
            screen
    ):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.screen = screen

        self.x = 0
        self.y = 0
        self.pos = Vector2(self.x, self.y)

        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            int(self.pos.x * self.cell_size),
            int(self.pos.y * self.cell_size),
            self.cell_size,
            self.cell_size
        )
        pygame.draw.rect(self.screen, (126, 166, 140), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)