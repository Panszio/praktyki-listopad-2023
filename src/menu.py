import pygame
import pygame_menu
from sanke import game_loop
from enum import Enum

pygame.init()

# Utwórz okno gry
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu Główne")

class Key_Bindings(Enum):
    PURPLE = "Left K_left Right K_right"
    YELLOW = "Left K_a Right K_d"
    BLUE = "Left K_b Right K_n"
    RED = "Left K_o Right K_p"

# Wypełnij ekran kolorem
screen.fill((167, 209, 61))

current_menu = None  # Zmienna globalna przechowująca aktualne menu

def replay_game():
    game_loop()

# Zdefiniuj funkcję menu
def start_menu():
    global current_menu
    menu = pygame_menu.Menu(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title="Welcome in a snake Landrrr!",
                            theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button("Play", game_loop)
    menu.add.button("Key Binding", show_key_bindings_menu)
    menu.add.button("Quit", pygame_menu.events.EXIT)

    current_menu = menu  # Ustaw aktualne menu
    menu.mainloop(screen)

def show_key_bindings_menu():
    global current_menu
    key_menu = pygame_menu.Menu(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title="Key Bindings",
                                theme=pygame_menu.themes.THEME_BLUE)

    for binding in Key_Bindings:
        key_menu.add.label(binding.name + ": " + binding.value)

    key_menu.add.button("Back", show_previous_menu)
    current_menu = key_menu
    key_menu.mainloop(screen)

def show_previous_menu():
    global current_menu
    current_menu.mainloop(screen)

# Wywołaj funkcję start_menu, aby wyświetlić menu
start_menu()

# Dodaj pętlę gry tutaj, aby utrzymać otwarte okno
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
