from abc import ABCMeta, abstractmethod
from typing import Callable, Self
from .vector import Vector

class DrawableShape(metaclass=ABCMeta):
    """A base class for drawable shapes"""
    def __init__(
            self,
            color: tuple[int,int,int],
            position: tuple[int,int],
            draw_function: Callable[[Self], None]
        ) -> None:
        """Initialize with a color, position and drawfunction"""
        self.color = color
        self.position = Vector(*position)
        self.draw_function = draw_function


    def draw(self):
        """Draw the object using the provided draw function"""
        self.draw_function(self)