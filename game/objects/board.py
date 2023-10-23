from typing import Self
from objects.vector import Vector2D
from objects.player import Player
from objects.rectangle import Rectangle

class Board:

    def __init__(self, size):
        self.size = size
        self.bricks = self.create_bricks()
        self.player = Player()
        self.balls = []


    def update(self) -> None:
        self.player.update()
        for ball in self.balls:
            ball.update()


    def draw(self) -> None:
        pass


    def create_bricks(self) -> list[Rectangle, ...]:
        return []