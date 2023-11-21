import pygame
import button
import pygame_menu

from main_game import MAIN_GAME
from sanke import  build_snake
from enum import Enum



pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAIN_GAME = MAIN_GAME
build_snake = build_snake

class Key_Bindings(Enum):
    PURPLE = "Left K_left Right K_right"
    YELLOW = "Left K_a Right K_d"
    BLUE = "Left K_b Right K_n"
    RED = "Left K_o Right K_p"







screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
START_img = pygame.image.load("../Graphic/button/START.png").convert_alpha()
quit_img = pygame.image.load("../Graphic/button/button_quit.png").convert_alpha()
keys_img = pygame.image.load('../Graphic/button/button_keys.png').convert_alpha()
back_img = pygame.image.load('../Graphic/button/button_back.png').convert_alpha()

#create button instances
START_img = button.Button(304, 125, START_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
keys_button = button.Button(246, 250, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)




def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop



screen.fill((167, 209, 61))

def Start_menu():
  start_menu = pygame_menu.Menu(width = SCREEN_WIDTH, height = SCREEN_HEIGHT, title= "Welcome to snake Game!",
                                theme=pygame_menu.themes.THEME_BLUE)
  start_menu.add.button("Play", MAIN_GAME ,build_snake)
  start_menu.add.button("Key Banding",Key_Bindings)


pygame.quit()