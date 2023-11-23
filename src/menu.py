import pygame
import pygame_menu as pygameMenu
from sanke import game_loop
from enum import Enum

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
    menu = pygameMenu.Menu(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title="Welcome in a snake Land!",
                            theme=pygameMenu.themes.THEME_BLUE)

    menu.add.button("Choose Snake", checkbox_menu)
    menu.add.button("Key Binding", show_key_bindings_menu)
    menu.add.button("Quit", pygameMenu.events.EXIT)

    current_menu = menu
    menu.mainloop(screen)

def show_key_bindings_menu():
    global current_menu
    key_menu = pygameMenu.Menu(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title="Key Bindings",
                                theme=pygameMenu.themes.THEME_BLUE)

    for binding in Key_Bindings:
        key_menu.add.label(binding.name + ": " + binding.value)

    key_menu.add.button("Back", show_previous_menu)
    current_menu = key_menu
    key_menu.mainloop(screen)

def checkbox_menu():
        global current_menu

        Check_menu = pygameMenu.Menu(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title="Choose a SNAKE",
                                     theme=pygameMenu.themes.THEME_BLUE)

        Check_menu.add.toggle_switch('One Snake', state_text=('On', 'Off'), state=0)
        Check_menu.add.toggle_switch('Two Snakes', state_text=('On', 'Off'), state=0)
        Check_menu.add.toggle_switch('Three Snakes', state_text=('On', 'Off'), state=0)
        Check_menu.add.toggle_switch('Four Snakes', state_text=('On', 'Off'), state=0)

        Check_menu.add.button('Play', game_loop)

        current_menu = Check_menu
        Check_menu.mainloop(screen)

        Check_menu.mainloop(screen)
def show_previous_menu():
    global current_menu
    if current_menu is not None:
        current_menu.set_attribute("return")
    else:
        print("Current menu is None")







# Wywołaj funkcję start_menu, aby wyświetlić menu
start_menu()

# Dodaj pętlę gry tutaj, aby utrzymać otwarte okno
running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
finally:
    pygame.quit()
