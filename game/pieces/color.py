class Color:
    default_colors = {
        'black': {'red': 0  , 'green': 0  , 'blue': 0  },
        'white': {'red': 255, 'green': 255, 'blue': 255},
        'red'  : {'red': 255, 'green': 0  , 'blue': 0  },
        'green': {'red': 0  , 'green': 255, 'blue': 0  },
        'blue' : {'red': 0  , 'green': 0  , 'blue': 255}
    }
    def __init__(
            self,
            color: str | None = None,
            red: int = 0,
            green: int = 0,
            blue: int = 0
    ) -> None:
        """Initialize the color class with a color, either
        a string corresponding to a basic color or a RGB value.
        if no arguments are provided it defaults to black.

        Args:
            color (str | None, optional): a string of a basic color. Defaults to None.
            red (int, optional): the amount of red in the color: a number between 0 and 255. Defaults to 0.
            green (int, optional): the amount of green in the color:a number between 0 and 255. Defaults to 0.
            blue (int, optional): the amount of blue in the color:a number between 0 and 255. Defaults to 0.
        """
        if color in self.default_colors:
            self._red = self.default_colors[color]['red']
            self._green = self.default_colors[color]['green']
            self._blue = self.default_colors[color]['blue']
        elif color is None:
            self._red = red
            self._green = green
            self._blue = blue
        else:
            raise 


    def to_tuple(self) -> tuple[int,int,int]:
        """ Returns the RGB value of the color.

        Returns:
            tuple[int,int,int]: The RGB value as a tuple
        """
        return (self._red, self._green, self._blue)