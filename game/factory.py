import pygame
from typing import Self
from objects.rectangle import Rectangle
from objects.circle import Circle

class GameEngineProvider:
    instance = None
    def __init__(
            self: Self,
            screen_size: tuple[int,int] = None
    ) -> Self:
        if not GameEngine.instance == None:
            return GameEngine.instance
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)


    def get_screen(self):
        return self.screen


    def get_draw_function(self, shape):
        screen = self.screen
        match shape:
            case "circle":
                def draw(
                    circle: Circle
                    ) -> None:
                    pygame.draw.circle(screen, circle.color, circle.position(), circle.radius)
                return draw
            case "rectangle":
                def draw(
                    rectangle: Rectangle
                ) -> None: