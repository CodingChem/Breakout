from .brick import Brick


class Bricks(list):
    def __init__(self) -> None:
        self.reset_bricks()


    def reset_bricks(self) -> None:
        """Reset the bricks for a new game
        """
        for i in range(5):
            for j in range(12):
                self.append(Brick(j * 60 + 50, i * 20 + 50))