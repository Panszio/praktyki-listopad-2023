import pygame
import sys

from pygame.math import Vector2
from src import MAIN_GAME

CELL_NUMBER = 20
CELL_SIZE = 40

pygame.init()
main_game = MAIN_GAME(
    cell_number=CELL_NUMBER,
    cell_size=CELL_SIZE,
    screen=pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE)),
    clock=pygame.time.Clock()


)

SCREEN_UPDATE = pygame.USEREVENT

pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()

    # Move this part outside the event loop
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        main_game.snake.direction = Vector2(0, -1)
    if keys[pygame.K_DOWN]:
        main_game.snake.direction = Vector2(0, 1)
    if keys[pygame.K_LEFT]:
        main_game.snake.direction = Vector2(-1, 0)
    if keys[pygame.K_RIGHT]:
        main_game.snake.direction = Vector2(1, 0)

    main_game.screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    main_game.clock.tick(100)  # I reduced the tick to 10 for testing purposes; you can adjust it later
