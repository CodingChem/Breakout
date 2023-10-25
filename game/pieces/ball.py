from pygame import SurfaceType
from pygame.draw import circle as draw_circle
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
        super().__init__(paddle.rect.centerx - radius, paddle.rect.top + radius * 2, radius * 2, radius * 2, color)
        self.dx = dx
        self.dy = dy


    def place_on_paddle(
            self,
            paddle: Paddle
    ) -> None:
        """Places the ball on the paddle

        Args:
            paddle (Paddle): The paddle object
        """
        self.rect.update(
            paddle.rect.centerx - self.rect.width / 2,
            paddle.rect.top - self.rect.height,
            self.rect.width,
            self.rect.height
        )
        self.dx, self.dy = 0, 0


    def draw(
            self,
            screen: SurfaceType
        ) -> None:
        """Draws the ball on the screen
        """
        draw_circle(screen, self.color.to_tuple(), self.rect.center, self.rect.width/2)


    def update(
            self,
            speed: int,
        ) -> None:
        """Moves the ball according to its velocity(dx,dy)

        Args:
            speed: the speed multiplier given to the ball object
        """
        self.rect.move_ip(self.dx * speed, self.dy * speed)


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
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.dx *= -1
        elif self.rect.top < 0 or self.rect.colliderect(paddle.rect):
            self.dy *= -1
        else:
            hit_brick = self.rect.collidelist(bricks) #type: ignore
            if hit_brick != -1:
                self.dy *= -1
                return bricks[hit_brick]


    def is_on_paddle(self) -> bool:
        return self.dx == 0 and self.dy == 0


    def shoot(self) -> None:
        self.dy = -1
        return