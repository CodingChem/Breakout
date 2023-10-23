from typing import Self

class Vector2D:
    """Represents a Vector in 2D"""
    def __init__(
            self,
            x = 0,
            y = 0
    ) -> Self:
        """Initialize with x & y coordinates, defaults to zero"""
        self.set(x,y)

    def set(
            self,
            x: int,
            y: int
    ) -> None:
        """Set new x & y values"""
        self.x = x
        self.y = y


    def __add__(
            self,
            other: Self
    ) -> Self:
        """Returns the sum of two vectors"""
        return Vector2D(
            x = self.x + other.x,
            y = self.y + other.y
        )
    

    def get_tuple(self) -> tuple[int,int]:
        return self.x, self.y


    def reflect_vertical(
            self,
    ) -> None:
        """Mirrors the vector across a vertical axis"""
        self.set(
            x = -self.x,
            y = self.y
        )
    

    def reflect_horizontal(
            self
    ) -> None:
        """Mirrors the vector across a horizontal axis"""
        self.set(
            x = self.x,
            y = -self.y
        )

