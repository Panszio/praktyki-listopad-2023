import pygame

from src.snake import SNAKE, ColorsEnum
from src.fruit import FRUIT


class MAIN_GAME:
    def __init__(
            self,
            cell_number: int,
            cell_size: int,
            screen,
            clock,
            fps: int,

    ):
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.screen = screen
        self.clock = clock
        self.snakes = [
            SNAKE(
                cell_size=self.cell_size,
                screen=self.screen,
                color=ColorsEnum.PURPLE
            ),
            SNAKE(
                cell_size=self.cell_size,
                screen=self.screen,
                color=ColorsEnum.RED
            ),
        ]
        self.fruit = FRUIT(
            cell_size=self.cell_size,
            cell_number=self.cell_number,
            screen=self.screen
        )

        self.fps = fps
        pygame.time.set_timer(pygame.USEREVENT, int(1000 / self.fps))

        self.run = True

    def update(self):
        self.snakes[0].move_snakes()
        self.check_collision()
        self.check_if_hit_himself()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.snakes[0].draw_snakes()
        # self.snakes[1].draw_snakes()
        self.fruit.draw_fruit()
        self.draw_score()
        self.clock.tick(self.fps * 10)

    def check_collision(self):
        if self.fruit.pos == self.snakes[0].body[0]:
            self.fps += 1
            pygame.time.set_timer(pygame.USEREVENT, int(1000 / self.fps))
            self.fruit.randomize()
            self.snakes[0].add_block()

    def check_fail(self):
        # jeżeli snakes 0 wyjdzie z okna gra się wyłączy
        if not 0 <= self.snakes[0].body[0].x < self.cell_number or not 0 <= self.snakes[0].body[0].y < self.cell_number:
            self.game_over()

    def check_if_hit_himself(self):
        snakes_head = self.snakes[0].body[0]
        snakes_body = self.snakes[0].body[1:]

        if snakes_head in snakes_body:
            self.game_over()

    def game_over(self):
        # pygame.quit()
        # sys.exit()
        self.run = False

    def draw_grass(self):
        for row in range(self.cell_number):
            grass_color = (167, 209, 61)
            if row % 2 == 0:
                for col in range(self.cell_number):
                    grass_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, grass_color, grass_rect)

            else:
                for col in range(self.cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size,
                                                 self.cell_size)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)

    def draw_score(self):
        game_font = pygame.font.Font('../Fonts/PoetsenOne-Regular.ttf', 25)
        score_text = str(len(self.snakes[0].body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(self.cell_size * self.cell_number - 60)
        score_y = int(self.cell_size * self.cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        self.screen.blit(score_surface, score_rect)
