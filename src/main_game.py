import pygame

from src.snake import SNAKE, ColorsEnum, RGB_VALUES, TurnsEnum
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
            players_count: int
    ):
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.screen = screen
        self.clock = clock
        self.players_count = players_count


        self._setup_snakes()

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
        self.check_if_hit_other()
        # self.kill_somebody()

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

    # def kill_somebody(self):
    #     for index, snake in enumerate(self.snakes):
    #         if snake.is_alive == False:
    #             return


                # print(f"nie żyje snake nr {index + 1}")


    def check_if_hit_himself(self):
        for index, snake in enumerate(self.snakes):
            if not snake.is_alive:
                continue

            head = snake.body[0]
            body = snake.body[1:]
            if head in body:
                snake.is_alive = False
                print(f"nie żyje snake nr {index + 1}")

    def check_if_hit_other(self):
        for index, snake in enumerate(self.snakes):
            # sprawdzamy dla wszystkich zywych wezy, czy nie weszly w kogos
            if not snake.is_alive:
                continue

            head = snake.body[0]  # glowa aktualnie sprawdzanego weza

            for jindex, other_snake in enumerate(self.snakes):
                # odrzucamy snake, ktory nie zyje, lub jezeli jest to ten sam snake
                # ktory wlasnie sprawdzamy
                if not snake.is_alive or index == jindex:
                    continue

                body = other_snake.body[1:]
                if head in body:
                    snake.is_alive = False
                    print(f"snake nr {index + 1} wszedl w {jindex + 1}")


    def game_over(self):
        # pygame.quit()
        # sys.exit()r
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


    def _setup_snakes(self):
        self.snakes = []
        available_colors = list(ColorsEnum)

        for i in range(self.players_count):
            self.snakes.append(
                SNAKE(
                    cell_size=self.cell_size,
                    cell_number=self.cell_number,
                    screen=self.screen,
                    color=available_colors[i]
                )
            )

    def move_snakes(self, key):
        for snake in self.snakes:
            snake.move(key)
