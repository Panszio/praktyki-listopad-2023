import pygame
import button
from tkinter import *

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

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

window = Tk()
x = IntVar()
def display():
    if(x.get()==1):
      print("you agree")
    else:
      print("You dont agree")





def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      if keys_button.draw(screen):
        print("check binding")
        #draw pause screen buttons
      if START_img .draw(screen):
        check_button = Checkbutton(window,
        text="I agree with something", variable=x,
                                   onvalue=1,
                                   offvalue=0,
                                   command=display)
    #check if the options menu is open
  if menu_state == "options":
      #draw the different options buttons
    if menu_state == "main":
      if back_button.draw(screen):
        if draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250):
  #event handler
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_SPACE:
                    game_paused = True
                if event.type == pygame.QUIT:
                  run = False

  pygame.display.update()
pygame.quit()