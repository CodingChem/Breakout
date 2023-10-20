from .vector import Vector2D


class Rectangle:
    def __init__(
            self,
            position: Vector2D,
            size: {
                'width' : int,
                'height': int
            }
    ):
        """"""
        self.position = position
        self.width = size['width']
        self.height = size['height']