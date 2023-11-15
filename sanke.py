import pygame
import sys

from src import MAIN_GAME
from src.snake import TurnsEnum

CELL_NUMBER = 30
CELL_SIZE = 40
FPS = 6

pygame.init()


def build_game():
    return MAIN_GAME(
        cell_number=CELL_NUMBER,
        cell_size=CELL_SIZE,
        screen=pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE)),
        clock=pygame.time.Clock(),
        fps=FPS
    )


SCREEN_UPDATE = pygame.USEREVENT
main_game = build_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                main_game.snakes[0].change_direction(TurnsEnum.LEFT)
            if event.key == pygame.K_RIGHT:
                main_game.snakes[0].change_direction(TurnsEnum.RIGHT)

            if event.key == pygame.K_a:
                main_game.snakes[1].change_direction(TurnsEnum.LEFT)
            if event.key == pygame.K_d:
                main_game.snakes[1].change_direction(TurnsEnum.RIGHT)

            if event.key == pygame.K_b:
                main_game.snakes[2].change_direction(TurnsEnum.LEFT)
            if event.key == pygame.K_n:
                main_game.snakes[2].change_direction(TurnsEnum.RIGHT)

            if event.key == pygame.K_r:
                main_game = build_game()
                continue

            if event.key == pygame.K_ESCAPE:
                if main_game.run:
                    main_game.run = False
                else:
                    pygame.quit()
                    sys.exit()


        if main_game.run:
            main_game.screen.fill((175, 215, 70))
            main_game.draw_elements()
            pygame.display.update()
