from src import IListener, UI


class Element(UI):
    @property
    def listeners(self) -> list[IListener]:
        return self._listeners

    @listeners.setter
    def listeners(self, value):
        raise RuntimeError('Don\'t set the listeners!')

    def update(self, event):
        pass

    def draw(self):
        pass

    def close(self):
        pass

    def __init__(self):
        self._listeners = []
