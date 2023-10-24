from typing import Callable

from .drawableshape import DrawableShape
from .movingobject import MovingObject
from .vector import Vector


class Rectangle(MovingObject):
    def __init__(
            self,
            draw_rect: Callable[[DrawableShape], None],
            position: tuple[int,int],
            size: tuple[int,int],
            color: tuple[int,int,int]
        ) -> None:
        super().__init__(color, draw_rect, position, (0,0))
        self.size = size
        self.velocity = Vector(0,0)


    def move(self, speed: int) -> None:
        self.velocity = Vector(speed,0)