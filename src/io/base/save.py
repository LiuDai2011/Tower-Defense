from typing.io import IO
from src.io.base.base import IOBase


class SaveBase(IOBase):
    def open(self, path, mode='w'):
        self.file = open(path, mode)

    def close(self):
        self.file.close()

    def save(self, _type, _value):
        pass

    def __init__(self):
        self.file: IO | None = None
