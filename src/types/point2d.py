import dataclasses


@dataclasses.dataclass
class Point2D:
    x: int
    y: int

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int):
        return Point2D(self.x * other, self.y * other)
