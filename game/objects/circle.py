from .vector import Vector2D
from typing import Self

class Circle:
    def __init__(
            self,
            position: Vector2D,
            radius: int
    ) -> Self:
        self.position = position
        self.radius = radius