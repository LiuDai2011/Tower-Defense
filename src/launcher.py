import sys
import pygame
from src.ui.window import Window
from src.test.test_element import TestElement


class Launcher:
    def __init__(self):
        self.window = Window()

    def launch(self):
        pygame.init()
        self.window.title('Tower Defense')
        self.window.pages[0].elements.append(TestElement())

        def loop():
            pass

        self.window.mainloop(loop)
        self.window.close()
        sys.exit(0)
