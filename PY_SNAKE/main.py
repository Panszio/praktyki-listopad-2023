from curses import window
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
#narysuj okondla snake
def draw_window(surface):
   surface.fill((0, 200 ,0))
   draw_grid(size, rows, surface)
   pygame.display.update()
   def draw_grid(w, rows, surface):
      size_between = w // rows;

      x = 0;
      y = 0;
      for l in range(rows):
         x = x + size_between
         y = y + size_between
      pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
      pygame.draw.line(surface, (255, 255, 255), (y, 0), (y, w))


def main():
 global size, rows
 size = 500 #obszar gry
 rows = 20 #siarka gry

 window = pygame.dispaly.set.mode((size, size))
            #jezęli true to gra działa
flag = True
clock = pygame.time.clock()

while flag:

    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      flag = False

    pygame.time.delay(50)
    clock.tick(10)

draw_window(window)

main() 

