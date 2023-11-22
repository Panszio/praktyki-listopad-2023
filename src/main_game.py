import pygame
import sys



from src.snake import SNAKE, ColorsEnum, RGB_VALUES
from src.fruit import FRUIT



pygame.init()


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
            SNAKE(  # player 1
                cell_size=self.cell_size,
                cell_number=self.cell_number,
                screen=self.screen,
                color=ColorsEnum.PURPLE
            ),
            SNAKE(  # player 2
                cell_size=self.cell_size,
                cell_number=self.cell_number,
                screen=self.screen,
                color=ColorsEnum.YELLOW
            ),
            SNAKE(
                cell_size=self.cell_size,
                cell_number=self.cell_number,
                screen=self.screen,
                color=ColorsEnum.BLUE
            ),
            SNAKE(
                cell_size=self.cell_size,
                cell_number=self.cell_number,
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
        for snake in self.snakes:
            snake.move_snakes()
        self.check_collision()
        self.check_if_hit_himself()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        for snake in self.snakes:
            snake.draw_snakes()
        self.fruit.draw_fruit()
        self.draw_score()
        self.draw_score()
        self.clock.tick(self.fps * 10)

    def check_collision(self):
        for snake in self.snakes:
            if self.fruit.pos == snake.body[0]:
                self.fps += 1
                # pygame.time.set_timer(pygame.USEREVENT, int(1000 / self.fps))
                snake.add_block()
                self.fruit.randomize()
                snake.points += 1

    def check_fail(self):
        return
        # for snake in self.snakes:
        #     if not 0 <= snake.body[0].x < self.cell_number or not 0 <= snake.body[0].y < self.cell_number:
        #         print("nie żyje")
        #         self.game_over()
    def check_if_hit_himself(self):
        for snake in self.snakes:
            head = snake.body[0]
            body = snake.body[1:]
            if head in body:
                self.game_over()

    def game_over(self):
        # pygame.quit()
        # sys.exit()r
        end = self.run = False
        print(end)

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
        game_font = pygame.font.Font('../Fonts/PoetsenOne-Regular.ttf',30 )
        x_offset = 15
        y_offset = 100
        decrement_y = 25

        for snake in self.snakes:
            points_str = f" {snake.points} "
            score_surface = game_font.render(points_str, True ,RGB_VALUES[snake.color.value])

            score_x = int(self.cell_size * self.cell_number - x_offset)
            score_y = int(self.cell_size * self.cell_number - y_offset)
            y_offset -= decrement_y
            score_rect = score_surface.get_rect(center=(score_x, score_y))
            self.screen.blit(score_surface, score_rect)

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.display.flip()

    pygame.quit()
    sys.exit()





