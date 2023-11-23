import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Checkboxy w Pygame")

# Kolory
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

# Klasa reprezentująca checkbox
class Checkbox:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.checked = False

    def draw(self):
        pygame.draw.rect(screen, gray if not self.checked else white, self.rect, 0)
        pygame.draw.rect(screen, black, self.rect, 1)

        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, black)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def toggle(self):
        self.checked = not self.checked


# Utwórz checkboxy
checkbox1 = Checkbox(50, 50, 200, 50, "Checkbox 1")
checkbox2 = Checkbox(50, 120, 200, 50, "Checkbox 2")
checkbox3 = Checkbox(50, 190, 200, 50, "Checkbox 3")

checkboxes = [checkbox1, checkbox2, checkbox3]

# Główna pętla gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Kliknięcie lewego przycisku myszy
                for checkbox in checkboxes:
                    if checkbox.rect.collidepoint(event.pos):
                        checkbox.toggle()
                        if checkbox.checked:
                            # Jeśli kliknięto checkbox, wyłącz pozostałe
                            for other_checkbox in checkboxes:
                                if other_checkbox != checkbox:
                                    other_checkbox.checked = False

    # Wypełnij tło
    screen.fill(white)

    # Narysuj checkboxy
    for checkbox in checkboxes:
        checkbox.draw()

    # Zaktualizuj okno
    pygame.display.flip()
