from typing import Callable

from .drawableshape import DrawableShape
from .ball import Ball
from .rectangle import Rectangle


class Player:
    speed = 5
    def __init__(
            self,
            draw_circle: Callable[[Ball], None],
            draw_rect: Callable[[DrawableShape], None],
            screen_size: tuple[int, int],
            lives: int = 3
        ) -> None:
        self.lives = lives
        self.paddle = Rectangle(draw_rect,(int(screen_size[0]/2),screen_size[1] - 50), (50, 50),(255,255,255))
        self.ball = Ball(draw_circle,5,(255,255,255),(0,0),(1,1))


    def update(self) -> None:
        self.ball.update()
        self.paddle.update()


    def draw(self) -> None:
        self.paddle.draw()
        self.ball.draw()


    def move_left(self) -> None:
        self.paddle.move(-self.speed)


    def move_right(self) -> None:
        self.paddle.move(self.speed)


    def stop_moving(self) -> None:
        self.paddle.move(0)