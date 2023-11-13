import sys

import pygame
from pygame.math import Vector2

from src import MAIN_GAME


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

        self.head_up = pygame.image.load('Graphic/Second Snake/head.red.up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphic/Second Snake/head.red.down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphic/Second Snake/head.red.right.png').convert_alpha()
        self.head_left = pygame.image.load('../Graphic/Second Snake/head.red.left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphic/Second Snake/tail.red.up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphic/Second Snake/tail.red.down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphic/Second Snake/tail.red.right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphic/Second Snake/tail.red.left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphic/Second Snake/body.red.vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphic/Second Snake/body.red.horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphic/Second Snake/body.red.tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphic/Second Snake/body.red.tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphic/Second Snake/body.red.br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphic/Second Snake/body.red.bl.png').convert_alpha()

    def draw_snake(self):
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
                if  previous_block.x == next_block.x:
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
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphic(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down


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




CELL_NUMBER = 40
CELL_SIZE = 30

pygame.init()

MAIN_GAME = MAIN_GAME(
cell_number=CELL_NUMBER,
cell_size=CELL_SIZE,
screen=pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE)),
clock=pygame.time.Clock()
)

SCREEN_UPDATE = pygame.USEREVENT

pygame.time.set_timer(SCREEN_UPDATE, 100)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            MAIN_GAME.update()

    # Move this part outside the event loop
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        MAIN_GAME.snake.direction = Vector2(0, -1)
    if keys[pygame.K_s]:
        MAIN_GAME.snake.direction = Vector2(0, 1)
    if keys[pygame.K_a]:
        MAIN_GAME.snake.direction = Vector2(-1, 0)
    if keys[pygame.K_d]:
        MAIN_GAME.snake.direction = Vector2(1, 0)

    MAIN_GAME.screen.fill((175, 215, 70))
    MAIN_GAME.draw_elements()
    pygame.display.update()
    MAIN_GAME.clock.tick(60)  # I reduced the tick to 10 for testing purposes; you can adjust it later
