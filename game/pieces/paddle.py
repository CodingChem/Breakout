from typing import Self
from pygame import K_LEFT, K_RIGHT
from pygame.key import get_pressed as get_key_pressed

from .vector import Vector
from .brick import Brick

class Paddle(Brick):
    def set_velocity(
            self: Self,
            dx: int
    ):
        self.velocity = Vector(dx, 0)