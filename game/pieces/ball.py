from typing import Self
from pygame import SurfaceType
from pygame.draw import circle as draw_circle
from .vector import Vector
from .paddle import Paddle
from .brick import Brick
from .color import Color


class Ball(Brick):
    def __init__(
            self,
            paddle: Paddle,
            dx: int = 0,
            dy: int = 0,
            color: Color = Color('white'),
            radius: int = 10
        ) -> None:
        """Initialize the ball class

        Args:
            x (int): initial x-coordinate of the ball
            y (int): initial y-coordinate of the ball
            dx (int): initial x-component of velocity
            dy (int): initial y-component of velocity
            color (int, optional): color of ball. Defaults to white
            radius (int, optional): Radius of ball. Defaults to 10.
        """
        super().__init__(paddle.centerx - radius, paddle.top + radius * 2, dx, dy, radius * 2, radius * 2, color)


    def place_on_paddle(
            self,
            paddle: Paddle
    ) -> None:
        """Places the ball on the paddle

        Args:
            paddle (Paddle): The paddle object
        """
        super().set_position(
            paddle.centerx - self.width / 2,
            paddle.top - self.height,
            self.width,
            self.height
        )
        self.velocity = Vector(0,0)


    def draw(
            self,
            screen: SurfaceType
        ) -> None:
        """Draws the ball on the screen
        """
        draw_circle(screen, self.color.to_tuple(), self.center, self.width/2)


    def bounce(
            self,
            screen_width: int,
            bricks: list[Brick],
            paddle: Paddle
    ) -> None | Brick:
        """Bounce the ball of walls, the paddle and bricks.

        Args:
            paddle (Paddle): The Paddle
            bricks (list[Brick]): A list of bricks

        Returns:
            Brick or None: The brick that was hit, or None if no brick was hit.
        """
        if self.left < 0 or self.right > screen_width:
            self.velocity.x *= -1
        elif self.top < 0 or self.colliderect(paddle):
            self.velocity.y *= -1
        else:
            hit_brick = self.collidelist(bricks)
            if hit_brick != -1:
                self.velocity.y *= -1
                return bricks[hit_brick]


    def is_on_paddle(self) -> bool:
        return self.velocity.x == 0 and self.velocity.y == 0


    def shoot(
            self: Self,
            paddle: Paddle
        ) -> None:
        self.velocity = paddle.velocity + Vector(0, -1)
        return