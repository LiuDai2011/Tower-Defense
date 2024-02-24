import pygame
from pygame import Surface

from src.enums.events import Events
from src.interfaces.listener_i import IListener
from src.interfaces.ui_i import UI
from src.ui.page import Page


class Window(UI):
    screen: Surface = None

    def __init__(self):
        self.size = (800, 600)
        Window.screen = pygame.display.set_mode(self.size)

        self.pages: list[Page] = [Page()]
        self.now_page = 0

        self._listeners = []

    def update(self, event):
        self.pages[self.now_page].update(event)

    def draw(self):
        self.pages[self.now_page].draw()

    def close(self):
        for e in self.pages:
            e.close()
        pygame.quit()

    def mainloop(self, func=lambda: None):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.update(Events.update)
            self.draw()
            func()
            pygame.display.flip()

    @staticmethod
    def title(title: str = ''):
        pygame.display.set_caption(title)

    @property
    def listeners(self) -> list[IListener]:
        return self._listeners

    @listeners.setter
    def listeners(self, value):
        self._listeners = value
