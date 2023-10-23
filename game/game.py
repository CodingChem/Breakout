from sys import exit
import pygame
from typing import Self
from objects.board import Board 
from objects.vector import Vector2D

class Game:
    """This class handles the interactions between our Board class and pygame"""
    def __init__(
            self,
            screen_size: tuple[int, int],
    ) -> Self:
        self.screen_size = screen_size
        self.screen = None
        self.board = None
    

    def initialize_screen(self) -> None:
        self.screen = pygame.display.set_mode(self.screen_size)


    def initialize_board(self) -> None:
        self.board = Board(self.screen_size, self.draw_circle, self.draw_rectangle)


    def draw_circle(
            self,
            pos: Vector2D,
            size: {'radius': int}
            ) -> None:
        pygame.draw.circle(self.screen,(255,255,255),(pos.x, pos.y),size['radius'])


    def draw_rectangle(
            self,
            pos: Vector2D,
            size: {
                'width': int,
                'height': int
                }
            ) -> None:
        pygame.draw.rect(self.screen, (255,255,255),pygame.rect(pos.x,pos.y,pos.x+size['width'], pos.y + size['height']))


    def loop(self) -> None:
        while True:
            self.handle_events()
            self.update()
            self.draw()

    
    def handle_events(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_RIGHT:
                            pass
                        case pygame.K_LEFT:
                            pass


    def update(self) -> None:
        self.board.update()


    def draw(self) -> None:
        self.screen.fill((0,0,0))
        self.board.draw()
        pygame.display.update()


if __name__ == '__main__':
    game = Game((400,600))
    game.initialize_screen()
    game.initialize_board()
    game.loop()