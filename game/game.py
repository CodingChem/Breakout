# Base packages import
from typing import Self
from sys import exit
# External packages import
import pygame
# Internal packages import
from objects import Player, BrickList


class Game:
    """The Game object is responsible to run our game instance"""
    def __init__(
            self,
            screen_width: int = 400,
            screen_height: int = 800,
        ) -> None:
        pygame.init()
        self._screen_size = (screen_width, screen_height)
        self._screen = pygame.display.set_mode(self._screen_size)
        self._player = Player()
        self._bricks = BrickList()
        self._ball = None


    def start_game(self) -> None:
        #self._initialize_game()
        self._loop()


    def _initialize_game(self) -> None:
        raise NotImplementedError


    def _loop(self) -> None:
        while True:
            self._handle_events()
            self._update()
            self._draw()


    def _handle_events(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            pass
                        case pygame.K_RIGHT:
                            pass
                        case pygame.K_SPACE:
                            pass


    def _update(self) -> None:
        self._player.update()
        if self._ball:
            self._ball.update()


    def _draw(self) -> None:
        self._screen.fill((0,0,0))
        self._player.draw()
        self._bricks.draw()
        if self._ball:
            self._ball.draw()
        pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.start_game()