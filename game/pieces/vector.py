from math import sqrt
from typing import Self


class Vector:
    def __init__(
            self: Self,
            x: int,
            y: int
        ) -> None:
        self.x, self.y = x, y


    def __add__(
            self: Self,
            other: Self
    ) -> Self:
        return Vector(self.x + other.x, self.y + other.y)


    def flip_horizontal_component(
            self: Self,
    ) -> None:
        self.x *= -1


    def flip_vertical_component(
            self: Self,
    ) -> None:
        self.y *= -1


    def magnitude(self: Self):
        return sqrt(self.x ** 2 + self.y ** 2)


    def normalize(self: Self):
        magnitude = self.magnitude()
        self.x /= magnitude
        self.y /= magnitude