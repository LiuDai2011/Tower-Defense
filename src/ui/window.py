import pygame
from src.interfaces.ui_i import UI


class Window(UI):
    def __init__(self):
        self.size = (600, 480)
        self.screen = pygame.display.set_mode(self.size)

    def update(self):
        pass

    def draw(self):
        pass

    def close(self):
        pass

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.update()
