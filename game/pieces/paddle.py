from pygame import SurfaceType, Rect, K_LEFT, K_RIGHT
from pygame.key import get_pressed as get_key_pressed
from pygame.draw import rect as draw_rect


class Paddle:
    def __init__(
            self,
            screen: SurfaceType,
            x: int,
            y: int,
            width: int = 80,
            height: int = 10,
            color: tuple[int,int,int] = (255,255,255)
    ) -> None:
        """Initialize the paddle class

        Args:
            screen (pygame.SurfaceType): The surface object to be rendered,
            x (int): The initial x-coordinate of the paddle
            y (int): The initial y-coordinate of the paddle
            width (int): The width of the paddle. Defaults to 80
            height (int): The height of the paddle. Defaults to 10
            color (tuple[int,int,int]): The color of the paddle
        """
        self.rect = Rect(x, y, width, height)
        self.color = color
        self.screen = screen


    def draw(
            self,
    ) -> None:
        """Draw the paddle on the surface object"""
        draw_rect(self.screen, self.color, self.rect)


    def update(
            self,
            speed: int
    ) -> None:
        """Updates the position of the paddle given the direction of user input

        Args:
            speed (int): The speed at witch the paddle moves
        """
        keys = get_key_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-speed,0)
        elif keys[K_RIGHT] and self.rect.right < self.screen.get_width():
            self.rect.move_ip(speed, 0)