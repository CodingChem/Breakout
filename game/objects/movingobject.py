from typing import Callable
from .drawableshape import DrawableShape
from .vector import Vector

class MovingObject(DrawableShape):
    """A base class for a moving object"""
    def __init__(
            self,
            color: tuple[int,int,int],
            draw_function: Callable[[DrawableShape],None],
            position: tuple[int,int],
            velocity: tuple[int,int] = (0,0)
        ) -> None:
        """Initialize object with color, draw_function, position(x,y) and velocity(x,y)"""
        super().__init__(color, position, draw_function)
        self.velocity = Vector(velocity[0], velocity[1])


    def update(self) -> None:
        """Updates the position of the object with the velocity"""
        self.position = self.position + self.velocity


    @classmethod
    def __subclasshook__(cls, C):
        if cls is MovingObject:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented