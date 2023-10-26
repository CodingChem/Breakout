from typing import Self


class Vector:
    def __init__(
            self: Self,
            x: int,
            y: int
        ) -> None:
        self.x, self.y = x, y