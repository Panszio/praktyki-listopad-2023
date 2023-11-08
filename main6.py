import random
import pygame


pygame.init()


class Cube:
    rows = 20

    def __init__(self, start, dirnx=1, dirny=0, color=(0, 0, 0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = size // rows
        rw = self.pos[0]
        cm = self.pos[1]
        pygame.draw.rect(surface, self.color, (rw * dis + 1, cm * dis + 1, dis - 2, dis - 2))

        if eyes:
            center = dis // 2
            radius = 3
            circle_middle = (rw * dis + center - radius, cm * dis + 8)
            circle_middle2 = (rw * dis + center + radius, cm * dis + 8)
            pygame.draw.circle(surface, (255, 255, 255), circle_middle, radius)
            pygame.draw.circle(surface, (255, 255, 255), circle_middle2, radius)

class Snake:
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.dirnx = -1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_RIGHT]:
            self.dirnx = 1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_UP]:
            self.dirnx = 0
            self.dirny = -1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_DOWN]:
            self.dirnx = 0
            self.dirny = 1
        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]


        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                 if c.dirnx == -1 and c.pos[0] <= 0:
                     c.pos = (c.rows - 1, c.pos[1])
                 elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                 elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                     c.pos = (c.pos[0], 0)
                 elif c.dirnx == -1 and c.pos[1] <= 0:
                     c.pos = (c.pos[0], c.rows -1)
                 else:
                     c.move(c.dirnx, c.dirny)




    def reset(self, pos):
        pass

    def add_cube(self):
        tail = self.body[-1]
        dx = tail.dirnx
        dy = tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))

            self.body[-1].dirnx = dx
            self.body[-1].dirny = dy

    def draw(self, surface):
        for c in self.body:
            c.draw(surface, c == self.body[0])


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
        s.draw(surface)
        apple.draw(surface)
        pygame.display.update()


def random_apple(snake):
    positions = snake.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            return x, y


def main():
    global size, rows, s, apple
    size = 500
    rows = 20
    window = pygame.display.set_mode((size, size))

    s = Snake((0, 0, 0), (10, 10))
    apple = Cube(random_apple(s), color=(255, 0, 0))

    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(10)
        clock.tick(10)
        s.move()
        if s.body[0].pos == apple.pos:
            s.add_cube()
            apple = Cube(random_apple(s), color=(255, 0, 0))

        draw_window(window)

main()
