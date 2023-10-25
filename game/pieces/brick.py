from pygame import SurfaceType, Rect
from pygame.draw import rect as draw_rect
from random import randint

class Brick:
    def __init__(
            self,
            screen: SurfaceType,
            x: int,
            y: int,
            width: int = 60,
            height: int = 20,
            color: tuple[int,int,int] = (randint(0,255), randint(0,255), randint(0,255))
    ) -> None:
        """Initializes the Brick class

        Args:
            screen (pygame.SurfaceType): The surface object to draw the brick on.
            x (int): initial x-coordinate of the brick
            y (int): initial y-coordinate of the brick
            width (int): The width of the brick. Defaults to 60
            height (int): The height of the brick. Defaults to 20
            color (tuple[int,int,int], optional): _description_. Defaults to (random.randint(0,255), random.randint(0,255), random.randint(0,255)).
        """
        self.rect = Rect(x, y, width, height)
        self.color = color
        self.screen = screen


    def draw(self) -> None:
        """Draw the brick on the screen
        """
        draw_rect(self.screen, self.color, self.rect)
