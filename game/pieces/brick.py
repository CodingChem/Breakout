from pygame import SurfaceType, Rect
from pygame.draw import rect as draw_rect
from random import randint
from .color import Color

class Brick(Rect):
    def __init__(
            self,
            x: int,
            y: int,
            width: int = 60,
            height: int = 20,
            color: Color | None = None
    ) -> None:
        """Initializes the Brick class

        Args:
            x (int): initial x-coordinate of the brick
            y (int): initial y-coordinate of the brick
            width (int): The width of the brick. Defaults to 60
            height (int): The height of the brick. Defaults to 20
            color (tuple[int,int,int], optional): _description_. Defaults to (random.randint(0,255), random.randint(0,255), random.randint(0,255)).
        """
        super().__init__(x, y, width, height)
        if color is None:
            self.color = Color(None, randint(0,255), randint(0,255), randint(0,255))
        else:
            self.color = color

    def draw(self, screen: SurfaceType) -> None:
        """Draw the brick on the screen
        """
        draw_rect(screen, self.color.to_tuple(), self)
