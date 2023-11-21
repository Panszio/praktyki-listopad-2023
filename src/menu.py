import pygame
import pygame_menu
# from main_game_file import MAIN_GAME
from sanke import game_loop
from enum import Enum

pygame.init()

# create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

class Key_Bindings(Enum):
    print("dupa")
    # PURPLE = "Left K_left Right K_right"
    # YELLOW = "Left K_a Right K_d"
    # BLUE = "Left K_b Right K_n"
    # RED = "Left K_o Right K_p"

# Fill the screen with color
screen.fill((167, 209, 61))

# Define the menu function
def Start_menu():
    menu = pygame_menu.Menu(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title="Welcome to Snake Game!",
                            theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button("Play", game_loop)
    menu.add.button("Key Binding", Key_Bindings)  # Assuming you have a function to handle key bindings
    menu.add.button("Quit", pygame_menu.events.EXIT)
    menu.mainloop(screen)

# Call the Start_menu function to display the menu
Start_menu()

# Add the game loop here to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
