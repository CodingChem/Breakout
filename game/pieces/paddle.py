from pygame import K_LEFT, K_RIGHT
from pygame.key import get_pressed as get_key_pressed
from .brick import Brick

class Paddle(Brick):
    def update(
            self,
            speed: int,
            border_width: int
    ) -> None:
        """Updates the position of the paddle given the direction of user input

        Args:
            speed (int): The speed at witch the paddle moves
        """
        keys = get_key_pressed()
        if keys[K_LEFT] and self.left > 0:
            self.move_ip(-speed,0)
        elif keys[K_RIGHT] and self.right < border_width:
            self.move_ip(speed, 0)