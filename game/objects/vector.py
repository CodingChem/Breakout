from typing import Self


class Vector:
    """A Vector class representing a 2D vecor in space"""
    def __init__(
            self,
            x: int,
            y: int,
        ) -> None:
        """Initialized with a position (x,y)"""
        self._x = x
        self._y = y


    def get_tuple(self):
        """Returns a tuple of the vector coordinates"""
        return (self._x, self._y)


    def __add__(
            self,
            other: Self
    ) -> Self:
        """Adds one Vector to another Vector"""
        return Vector(self._x + other._x, self._y + other._y)


    def reflect_horizontal(self) -> None:
        """Reverses the horizontal component of the vector"""
        self._x = -self._x


    def reflect_vertical(self) -> None:
        """Reverses the vertical component of the vector"""
        self._y = -self._y