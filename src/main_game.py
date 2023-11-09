import pygame
import sys

from src.snake import SNAKE
from src.fruit import FRUIT


class MAIN_GAME:
    def __init__(
            self,
            cell_number: int,
            cell_size: int,
            screen,
            clock,
    ):
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.screen = screen
        self.clock = clock

        self.snake = SNAKE(cell_size=self.cell_size, screen=self.screen)
        self.fruit = FRUIT(
            cell_size=self.cell_size,
            cell_number=self.cell_number,
            screen=self.screen
        )

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        # jeżeli snake 0 wyjdzie z okna gra się wyłączy
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()
