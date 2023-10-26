from sys import exit
import pygame
from pieces.ball import Ball
from pieces.paddle import Paddle
from pieces.brick import Brick

class Game:
    def __init__(
            self,
            width: int = 800,
            height: int = 600
        ) -> None:
        """Initialize the Game class

        Args:
            width (int, optional): Screen width. Defaults to 800.
            height (int, optional): Screen height. Defaults to 600.
        """
        pygame.init()
        self.font = pygame.font.Font(None,36)
        self.score = 0
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        self.paddle = Paddle( int(width / 2), height - 20)
        self.ball = Ball(self.paddle)

        self.lives = 3
        self.reset_bricks()

    def reset_bricks(self) -> None:
        """Reset the bricks for a new game
        """
        self.bricks = []
        for i in range(5):
            for j in range(12):
                self.bricks.append(Brick(j * 60 + 50, i * 20 + 50))


    # TODO
    def draw_text(
            self,
            text: str,
            pos: tuple[int,int]
    ):
        pass


    def run_game(self) -> None:
        """Main game loop."""
        while True:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()


    def draw(self) -> None:
        """Draws the screen with the objects and updates the display
        """
        self.screen.fill((0,0,0))
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        for brick in self.bricks:
            brick.draw(self.screen)
        pygame.display.flip()


    def handle_events(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()
                case pygame.KEYUP:
                    self.paddle.set_velocity(0)
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_SPACE:
                            if self.ball.is_on_paddle():
                                self.ball.shoot(self.paddle)
                        case pygame.K_LEFT:
                            self.paddle.set_velocity(-1)
                        case pygame.K_RIGHT:
                            self.paddle.set_velocity(1)


        if not self.bricks:
            self.ball.velocity.x = 0
            self.ball.velocity.y = 0
            self.draw_text("Winner!", (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2)))

        hit_brick = self.ball.bounce(self.screen.get_width(), self.bricks, self.paddle)
        if hit_brick is not None:
            self.bricks.remove(hit_brick)
            self.score += 1

        if self.ball.bottom > self.screen.get_height():
            self.lives -= 1
            if self.lives == 0:
                self.lives = 3
                self.reset_bricks()
            self.ball.place_on_paddle(self.paddle)


    def update(self):
        self.paddle.update(2)
        if self.ball.is_on_paddle():
            self.ball.place_on_paddle(self.paddle)
        else:
            self.ball.update(2)

if __name__ == '__main__':
    game = Game()
    game.run_game()