import abc


class IOBase(abc.ABC):
    @abc.abstractmethod
    def open(self, path):
        """Open"""

    @abc.abstractmethod
    def close(self):
        """Close"""
