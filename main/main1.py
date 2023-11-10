import pygame
import self

pygame.init()


class snake(object):
     body = []
     turns = {}

def __init__(self, color , pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1


def move(self):
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()

             keys = pygame.key.get_pressed()

             if keys[pygame.K_LEFT]:
                 self.dirnx = 1
                 self.dirny = 0
             self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_RIGHT]:
                 self.dirnx = -1
                 self.dirny = 0
     self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif keys[pygame.K_UP]:
                 self.dirnx = 0
                 self.dirny = -1
self.turns[self.head.pos [:]] = [self.dirnx, self.dirny]

        elif keys[pygame.K_DOWN]
                 self.dirnx = 0
                 self.dirny = 1
self.turns[self.head.pos [:]] = [self.dirnx, self.dirny]

def reset(self, pos):
        pass

 def add_cube(self):
        pass

 def draw(self, surface):
       pass

def draw_grid(w, rows, surface):
       size_between = w // rows

       x = 0
       y = 0
       for l in range(rows):
           x = x + size_between
           y = y + size_between
           pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
           pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

def draw_window(surface):
    surface.fill((0, 255, 0))
    draw_grid(size, rows, surface)
    pygame.display.update()



def main():
    global size, rows
    size = 800
    rows = 20
    window = pygame.display.set_mode((size, size))

    s = snake((0, 0, 0), (10, 10))

    flag = True
    Clock = pygame.time.Clock()

    while flag:

                pygame.time.delay(50)
                Clock.tick(10)
                draw_window( window)
main()
