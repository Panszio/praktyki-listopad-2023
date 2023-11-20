import pygame
import pygame_menu
import random
import sys
from typing import Tuple, Any
from math import isclose

pygame.init()

display_width = 600
display_height = 400

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

'''
Game difficulty is assigned the following values:
* Easy = 25
* Medium = 50
* Hard = 100
'''
difficulty = 25;
win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game by Shehan Atukorala')
clock = pygame.time.Clock()
player_name = '';
default_player_name = True;


def setup_snake_food():
    new_food_position = [random.randrange(1, (display_width // 10)) * 10,
                         random.randrange(1, (display_height // 10)) * 10]
    return new_food_position


def setup_collision_obj():
    new_collision_obj = [random.randrange(1, (display_width // 10)) * 10,
                         random.randrange(1, (display_height // 10)) * 10]
    return new_collision_obj


def set_game_difficulty(selected: Tuple, value: Any):
    if (value == 1):
        difficulty = 25
    elif (value == 2):
        difficulty = 50
    elif (value == 3):
        difficulty = 100
    else:
        difficulty = 25


def show_game_score(font, size, game_score):
    game_score_font = pygame.font.SysFont(font, size);
    game_score_surface = game_score_font.render((player_name + "'s Game Score: " + str(game_score)), True, white)
    game_score_rect = game_score_surface.get_rect()
    game_score_rect.midtop = (display_height, 15)
    win.blit(game_score_surface, game_score_rect)


def show_collision_obj(collision_obj_position, snake_width, snake_height):
    collision_obj_rect = pygame.Rect(collision_obj_position[0], collision_obj_position[1], snake_width, snake_height)
    collision_obj_image = pygame.image.load("../Graphic/apple.png")
    collision_obj_image_resize = pygame.transform.scale(collision_obj_image, (snake_width, snake_height))
    win.blit(collision_obj_image_resize, collision_obj_rect)


def set_player_name(name):
    global player_name;
    global default_player_name;
    player_name = name;
    default_player_name = False;


def set_default_player_name():
    global player_name;
    global default_player_name;
    player_name = "Guest"
    default_player_name = False


def show_start_screen():
    start_menu = pygame_menu.Menu(width=display_width, height=display_height, title='Welcome to Snake Game!',
                                  theme=pygame_menu.themes.THEME_BLUE);
    start_menu.add.text_input("Your Name: ", default="Guest", onchange=set_player_name);
    start_menu.add.selector("Difficulty: ", [("Easy", 1), ("Medium", 2), ("Hard", 3)], onchange=set_game_difficulty);
    start_menu.add.button("Play", game_loop);
    start_menu.add.button("Quit", pygame_menu.events.EXIT);
    if default_player_name:
        set_default_player_name();
    start_menu.mainloop(win)


def replay_game():
    game_loop()


def show_end_screen(game_score):
    end_menu = pygame_menu.Menu(width=display_width, height=display_height, title='Game Over',
                                theme=pygame_menu.themes.THEME_BLUE);
    end_menu.add.label("Your Score:" + str(game_score));
    end_menu.add.button("Replay Game", replay_game);
    end_menu.add.button("Quit Game", pygame_menu.events.EXIT);
    end_menu.mainloop(win)


def game_loop():
    x = display_width / 2
    y = display_height / 2
    snake_position = [display_width / 2, display_height / 2]
    snake_body = [[display_width / 2, display_height / 2], [(display_width / 2) - 10, display_height / 2],
                  [(display_width / 2) - (2 * 10), display_width / 2]]
    snake_width = 20
    snake_height = 20
    snake_speed = 5
    snake_direction = "UP"
    new_direction = snake_direction
    gameExit = False
    game_score = 0;

    food_position = setup_snake_food()
    show_food = True

    collision_obj_position = setup_collision_obj()
    show_collision = True

    while not gameExit:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
            break
        if keys[pygame.K_LEFT]:
            new_direction = "LEFT";
        if keys[pygame.K_RIGHT]:
            new_direction = "RIGHT";
        if keys[pygame.K_UP]:
            new_direction = "UP";

        if keys[pygame.K_DOWN]:
            new_direction = "DOWN";
        if snake_direction != "UP" and new_direction == "DOWN":
            snake_direction = new_direction
        if snake_direction != "DOWN" and new_direction == "UP":
            snake_direction = new_direction
        if snake_direction != "LEFT" and new_direction == "RIGHT":
            snake_direction = new_direction
        if snake_direction != "RIGHT" and new_direction == "LEFT":
            snake_direction = new_direction

        if snake_direction == "UP":
            snake_position[1] -= snake_speed
        if snake_direction == "DOWN":
            snake_position[1] += snake_speed;
        if snake_direction == "LEFT":
            snake_position[0] -= snake_speed;
        if snake_direction == "RIGHT":
            snake_position[0] += snake_speed;

        snake_body.insert(0, list(snake_position));
        if isclose(snake_position[0], food_position[0], abs_tol=5) and isclose(snake_position[1], food_position[1],
                                                                               abs_tol=5):
            game_score += 10;
            show_food = False;
        else:
            snake_body.pop();

        if isclose(snake_position[0], collision_obj_position[0], abs_tol=(snake_width - 10)) and isclose(
                snake_position[1], collision_obj_position[1], abs_tol=(snake_height - 10)):
            show_end_screen(game_score);

        if not show_food:
            food_position = setup_snake_food();
            show_food = True;
        if not show_collision:
            collision_obj_position = setup_collision_obj();

            show_collision = True;

        win.fill(black);
        for pos in snake_body:
            pygame.draw.rect(win, (255, 255, 255), pygame.Rect(pos[0], pos[1], snake_width / 2, snake_height / 2));

        pygame.draw.rect(win, (255, 0, 255), (food_position[0], food_position[1], snake_width / 2, snake_height / 2));

        show_collision_obj(collision_obj_position, snake_width, snake_height);

        if snake_position[0] < 0 or snake_position[0] > (display_width - snake_width / 2):
            show_end_screen(game_score);
        if snake_position[1] < 0 or snake_position[1] > (display_height - snake_height / 2):
            show_end_screen(game_score);

        show_game_score('consolas', 20, game_score)
        pygame.display.update();

        clock.tick(difficulty);


show_start_screen()