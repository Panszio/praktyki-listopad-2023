import pygame

from pygame.math import Vector2
from enum import Enum


class TurnsEnum(Enum):
    LEFT = 0
    RIGHT = 1


DIRECTIONS = [
    Vector2(0, -1),  # North - UP
    Vector2(-1, 0),  # East - RIGHT
    Vector2(0, 1),  # South - DOWN
    Vector2(1, 0)  # West - LEFT
]


class ColorsEnum(Enum):
    BLUE = 'blue'
    RED = 'red'
    YELLOW = 'yellow'
    PURPLE = 'purple'

START_POSITIONS={
    ColorsEnum.BLUE: [Vector2(13, 10), Vector2(12, 10), Vector2(11, 10)],
    ColorsEnum.RED: [Vector2(10,15), Vector2(9, 15), Vector2(8, 15)],
    ColorsEnum.YELLOW: [Vector2(13, 20), Vector2(12, 20), Vector2(1, 20)],
    ColorsEnum.PURPLE: [Vector2(8, 10), Vector2(7, 10), Vector2(6, 10)]
}


RGB_VALUES = {
    "blue": (0, 162, 232),
    "red": (232, 28, 36),
    "yellow": (255, 201, 14),
    "purple": (83, 58, 113),
}


class SNAKE:
    def __init__(
            self,
            cell_size: int,
            cell_number: int,
            screen,
            color: ColorsEnum = ColorsEnum.BLUE,
    ):

        self.cell_size = cell_size
        self.cell_number = cell_number
        self.screen = screen
        self.color = color
        self.points = 0

        self.body = START_POSITIONS[self.color]
        self.direction = Vector2(1, 0)
        self.new_block = False

        file_prefix = f'../Graphic/snake_{self.color.value}'

        self.head_up = pygame.image.load(file_prefix + '/head_up.png').convert_alpha()
        self.head_down = pygame.image.load(file_prefix + '/head_down.png').convert_alpha()
        self.head_right = pygame.image.load(file_prefix + '/head_right.png').convert_alpha()
        self.head_left = pygame.image.load(file_prefix + '/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load(file_prefix + '/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(file_prefix + '/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(file_prefix + '/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(file_prefix + '/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load(file_prefix + '/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(file_prefix + '/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load(file_prefix + '/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(file_prefix + '/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(file_prefix + '/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(file_prefix + '/body_bl.png').convert_alpha()

        self.head = self.head_down
        self.tail  = self.tail_down
    def draw_snakes(self):
        self.update_head_graphic()
        self.update_tail_graphic()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * self.cell_size)
            y_pos = int(block.y * self.cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size)

            if index == 0:
                self.screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                self.screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    self.screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    self.screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        self.screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        self.screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        self.screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        self.screen.blit(self.body_br, block_rect)

    def update_head_graphic(self):
        head_relation: Vector2 = self.body[1] - self.body[0]
        if head_relation == DIRECTIONS[3]:
            self.head = self.head_left
        elif head_relation == DIRECTIONS[1]:
            self.head = self.head_right
        elif head_relation == DIRECTIONS[2]:
            self.head = self.head_up
        elif head_relation == DIRECTIONS[0]:
            self.head = self.head_down

    def update_tail_graphic(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == DIRECTIONS[3]:
            self.tail = self.tail_left
        elif tail_relation == DIRECTIONS[1]:
            self.tail = self.tail_right
        elif tail_relation == DIRECTIONS[2]:
            self.tail = self.tail_up
        elif tail_relation == DIRECTIONS[0]:
            self.tail = self.tail_down

    def move_snakes(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            new_position = body_copy[0] + self.direction
            if new_position.x < 0:
                new_position.x = self.cell_number
            elif new_position.x >= self.cell_number:
                new_position.x = 0
            else:
                if new_position.y < 0:
                    new_position.y = self.cell_number
                elif new_position.y >= self.cell_number:
                    new_position.y = 0

            body_copy.insert(0, new_position)
            self.body = body_copy[:]
    def change_direction(self, turn: TurnsEnum):
        current_direction = self._direction_int()

        if turn == TurnsEnum.RIGHT:
            current_direction -= 1
        elif turn == TurnsEnum.LEFT:
            current_direction += 1

        if current_direction < 0:  # left turn overlap
            current_direction = 3
        if current_direction > 3:  # right turn overlap
            current_direction = 0

        self.direction = DIRECTIONS[current_direction]

    def _direction_int(self) -> int:
        return DIRECTIONS.index(self.direction)

    def add_block(self):
        self.new_block = True


