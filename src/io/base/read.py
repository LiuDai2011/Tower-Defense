from typing.io import IO
from src.io.base.base import IOBase


class ReadBase(IOBase):
    def open(self, path, mode='r'):
        self.file = open(path, mode)

    def close(self):
        self.file.close()

    def read(self, _type, _value):
        pass

    def __init__(self):
        self.file: IO | None = None
