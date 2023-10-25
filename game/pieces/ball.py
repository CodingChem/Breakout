from pygame import SurfaceType, Rect
from pygame.draw import circle as draw_circle
from .paddle import Paddle
from .brick import Brick


class Ball:
    def __init__(
            self,
            screen: SurfaceType,
            paddle: Paddle,
            dx: int = 0,
            dy: int = 0,
            color: tuple[int,int,int] = (255,255,255),
            radius: int = 10
        ) -> None:
        """Initialize the ball class

        Args:
            screen (pygame.SurfaceType): The surface to draw the ball on
            x (int): initial x-coordinate of the ball
            y (int): initial y-coordinate of the ball
            dx (int): initial x-component of velocity
            dy (int): initial y-component of velocity
            color (int, optional): color of ball. Defaults to white
            radius (int, optional): Radius of ball. Defaults to 10.
        """
        self.rect = Rect(paddle.rect.top + radius * 2, paddle.rect.centerx - radius, radius * 2, radius * 2)
        self.paddle = paddle
        self.dx = dx
        self.dy = dy
        self.screen = screen
        self.color = color


    def on_paddle(
            self,
    ) -> None:
        """Places the ball on the paddle

        Args:
            paddle (Paddle): The paddle object
        """
        self.rect.update(
            self.paddle.rect.centerx - self.rect.width / 2,
            self.paddle.rect.top - self.rect.height,
            self.rect.width,
            self.rect.height
        )
        self.dx, self.dy = 0, 0


    def draw(self) -> None:
        """Draws the ball on the screen
        """
        draw_circle(self.screen, self.color, self.rect.center, self.rect.width/2)


    def update(
            self,
            speed: int,
        ) -> None:
        """Moves the ball according to its velocity(dx,dy)

        Args:
            speed: the speed multiplier given to the ball object
        """
        if self.is_on_paddle():
            self.on_paddle()
        else:
            self.rect.move_ip(self.dx * speed, self.dy * speed)


    def bounce(
            self,
            bricks: list[Brick]
    ) -> None | Brick:
        """Bounce the ball of walls, the paddle and bricks.

        Args:
            paddle (Paddle): The Paddle
            bricks (list[Brick]): A list of bricks

        Returns:
            Brick or None: The brick that was hit, or None if no brick was hit.
        """
        if self.rect.left < 0 or self.rect.right > self.screen.get_width():
            self.dx *= -1
        elif self.rect.top < 0 or self.rect.colliderect(self.paddle.rect):
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