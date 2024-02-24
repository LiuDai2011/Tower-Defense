import pygame.draw

from src.ui.element import Element
from src.content import Content


class TestElement(Element):
    def draw(self):
        pygame.draw.rect(Content.get_launcher().window.screen, (0, 0, 255), (100, 100, 100, 100))
