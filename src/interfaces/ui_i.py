import abc

from src.interfaces.listener_i import IListener
from src.types.event import Event


class UI(abc.ABC):
    @abc.abstractmethod
    def update(self, event: Event):
        """Update"""

    @abc.abstractmethod
    def draw(self):
        """Draw self"""

    @abc.abstractmethod
    def close(self):
        """Close"""

    @property
    @abc.abstractmethod
    def listeners(self) -> list[IListener]:
        """Get The Listeners"""

    @listeners.setter
    @abc.abstractmethod
    def listeners(self, value: list[IListener]):
        """Set The Listeners"""

    def add_listener(self, listener: IListener):
        self.listeners = self.listeners + [listener]
