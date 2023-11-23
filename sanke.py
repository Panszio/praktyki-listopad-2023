import pygame
import sys
from src import MAIN_GAME

pygame.init()

def build_game(players_count):
    CELL_NUMBER = 25
    CELL_SIZE = 40
    FPS = 6
    return MAIN_GAME(
        cell_number=CELL_NUMBER,
        cell_size=CELL_SIZE,
        screen=pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE)),
        clock=pygame.time.Clock(),
        fps=FPS,
        players_count=players_count
    )

def game_loop(players_count = 2):
    main_game = build_game(players_count)
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
                main_game.move_snakes(event.key)

                if event.key == pygame.K_r:
                    main_game = build_game(players_count)
                elif event.key == pygame.K_ESCAPE:
                    if main_game.run:
                        main_game.run = False
                    else:
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    game_loop()
