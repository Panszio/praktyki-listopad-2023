import pygame
import sys
from src import MAIN_GAME
from src.snake import TurnsEnum

pygame.init()

def build_game():
    CELL_NUMBER = 25
    CELL_SIZE = 40
    FPS = 6
    return MAIN_GAME(
        cell_number=CELL_NUMBER,
        cell_size=CELL_SIZE,
        screen=pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE)),
        clock=pygame.time.Clock(),
        fps=FPS
    )

def game_loop():
    main_game = build_game()
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 1000 // main_game.fps)  # Ustawienie zdarzenia ekranu co określoną liczbę milisekund

    while True:
        main_game.screen.fill((175, 215, 70))
        main_game.draw_elements()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    main_game.snakes[0].change_direction(TurnsEnum.LEFT)
                elif event.key == pygame.K_RIGHT:
                    main_game.snakes[0].change_direction(TurnsEnum.RIGHT)
                elif event.key == pygame.K_a:
                    main_game.snakes[1].change_direction(TurnsEnum.LEFT)
                elif event.key == pygame.K_d:
                    main_game.snakes[1].change_direction(TurnsEnum.RIGHT)
                elif event.key == pygame.K_b:
                    main_game.snakes[2].change_direction(TurnsEnum.LEFT)
                elif event.key == pygame.K_n:
                    main_game.snakes[2].change_direction(TurnsEnum.RIGHT)
                elif event.key == pygame.K_o:
                    main_game.snakes[3].change_direction(TurnsEnum.LEFT)
                elif event.key == pygame.K_p:
                    main_game.snakes[3].change_direction(TurnsEnum.RIGHT)
                elif event.key == pygame.K_r:
                    main_game = build_game()
                elif event.key == pygame.K_ESCAPE:
                    if main_game.run:
                        main_game.run = False
                    else:
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    game_loop()
