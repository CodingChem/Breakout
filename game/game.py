from typing import Self
import pygame


class Game:
    """The Game object is responsible to run our game instance"""
    def __init__(
            self,
            screen_width: int = 400,
            screen_height: int = 800,
        ) -> Self:
        self.screen_size = (screen_width, screen_height)
        self.player = Player()
        self.ball = Ball()
        self.bricks = BrickList()


    def start_game(self) -> None:
        raise NotImplemented


    def _initialize_game(self) -> None:
        pass


    def _update(self) -> None:
        pass


    def _draw(self) -> None:
        pass


    def _loop(self) -> None:
        pass