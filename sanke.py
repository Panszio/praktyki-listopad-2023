import pygame
import sys

from src import MAIN_GAME
from src.snake import TurnsEnum

CELL_NUMBER = 40
CELL_SIZE = 30
FPS = 6

pygame.init()

MAIN_GAME = MAIN_GAME(
    cell_number=CELL_NUMBER,
    cell_size=CELL_SIZE,
    screen=pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE)),
    clock=pygame.time.Clock(),
    fps=FPS
)


SCREEN_UPDATE = pygame.USEREVENT


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            MAIN_GAME.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                MAIN_GAME.snake.change_direction(TurnsEnum.LEFT)
            if event.key == pygame.K_RIGHT:
                MAIN_GAME.snake.change_direction(TurnsEnum.RIGHT)

    if MAIN_GAME.run:
        MAIN_GAME.screen.fill((175, 215, 70))
        MAIN_GAME.draw_elements()
        pygame.display.update()
