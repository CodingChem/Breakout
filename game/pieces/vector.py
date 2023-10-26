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