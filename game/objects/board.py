from typing import Self
from objects.vector import Vector2D
from objects.player import Player

class Board:

    def __init__(self, size, draw_circle, draw_rect):
        self.size = size
        self.bricks = self.create_bricks()
        self.player = Player()
        self.balls = []


    def update(self) -> None:
        self.player.update()
        for ball in self.balls:
            ball.update()


    def draw(self) -> None:
        self.draw_circle(Vector2D(100,100),{'radius': 20})