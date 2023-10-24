from typing import Callable
from .movingobject import MovingObject


class Ball(MovingObject):
    def __init__(
            self,
            draw_function: Callable,
            radius: int,
            color: tuple[int, int, int],
            position: tuple[int, int],
            velocity: tuple[int, int] = (0,0),
        ) -> None:
        super().__init__(color, draw_function, position, velocity)
        self.radius = radius