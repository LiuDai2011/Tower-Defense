from src.interfaces.listener_i import IListener
from src.interfaces.ui_i import UI
from src.types.event import Event
from src.ui.element import Element


class Page(UI):
    def update(self, event: Event):
        for e in self.elements:
            e.update(event)

    def draw(self):
        for e in self.elements:
            e.draw()

    def close(self):
        for e in self.elements:
            e.close()

    @property
    def listeners(self) -> list[IListener]:
        raise ValueError('Don\'t find .listeners')

    @listeners.setter
    def listeners(self, value):
        raise ValueError('Don\'t find .listeners')

    def __init__(self):
        self.elements: list[Element] = []
