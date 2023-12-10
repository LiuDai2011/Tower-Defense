import dataclasses


@dataclasses.dataclass
class Coord:
    x: float
    y: float

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float):
        return Coord(self.x * other, self.y * other)
