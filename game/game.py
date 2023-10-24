# Base packages import
from typing import Callable, Self
from sys import exit
# External packages import
import pygame
# Internal packages import
from objects.ball import Ball
from objects.rectangle import Rectangle
from objects.player import Player

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
        draw_circle, draw_rect = self._get_draw_functions()
        self._player = Player(draw_circle, draw_rect, (screen_width, screen_height), 3)


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
                            self._player.move_left()
                        case pygame.K_RIGHT:
                            self._player.move_right()
                        case pygame.K_SPACE:
                            pass
                case pygame.KEYUP:
                    self._player.stop_moving()


    def _get_draw_functions(self) -> tuple[Callable, Callable]:
        screen = self._screen
        def draw_circle(ball: Ball):
            pygame.draw.circle(screen,ball.color,ball.position.get_tuple(), ball.radius)
        def draw_rect(rectangle: Rectangle):
            x, y = rectangle.position.get_tuple()
            pygame.draw.rect(screen, rectangle.color, pygame.Rect(x,y,rectangle.size[0],rectangle.size[1]))
        return (draw_circle, draw_rect)


    def _update(self) -> None:
        self._player.update()


    def _draw(self) -> None:
        self._screen.fill((0,0,0))
        self._player.draw()
        #self._bricks.draw()

        pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.start_game()