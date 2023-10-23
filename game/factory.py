import pygame
from typing import Self

class GameEngine:
    instance = None
    def __init__(
            self: Self,
            screen_size: tuple[int,int] = None
    ) -> Self:
        if not GameEngine.instance == None:
            return GameEngine.instance
        pygame.init()    
        self.screen = pygame.display.set_mode(screen_size)

    def get_draw_function(kind)