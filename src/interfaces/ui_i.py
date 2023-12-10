import abc


class UI(abc.ABC):
    @abc.abstractmethod
    def update(self):
        """Update"""

    @abc.abstractmethod
    def draw(self):
        """Draw self"""

    @abc.abstractmethod
    def close(self):
        """Close"""
