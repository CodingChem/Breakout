# Base packages import
from typing import Self
# External packages import
import pygame
# Internal packages import


class Game:
    """The Game object is responsible to run our game instance"""
    def __init__(
            self,
            screen_width: int = 400,
            screen_height: int = 800,
        ) -> Self:
        self.screen_size = (screen_width, screen_height)
        self.player = Player()
        self.ball = None
        self.bricks = BrickList()


    def start_game(self) -> None:
        raise NotImplementedError


    def _handle_events(self) -> None:
        raise NotImplementedError


    def _initialize_game(self) -> None:
        raise NotImplementedError


    def _update(self) -> None:
        raise NotImplementedError


    def _draw(self) -> None:
        raise NotImplementedError


    def _loop(self) -> None:
        raise NotImplementedError


if __name__ == '__main__':
    game = Game()