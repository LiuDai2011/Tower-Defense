import abc


class IListener(abc.ABC):
    @abc.abstractmethod
    def listen(self):
        """Listen To The Event"""

    @abc.abstractmethod
    def event_type(self) -> int:
        """Return A Event Type"""
