class FigureGeometric:
    def __init__(self, width, height):
        if self._validate_value(width):
            self._width = width
        else:
            self._width = 0
            print(f'this is an error of the number')
        if self._validate_value(height):
            self._height = height
        else:
            self._height = 0
            print(f'this is an error of the number')
    # get section
    @property
    def height(self): return self._height

    # set section
    @height.setter
    def height(self, height): self._height = height

    @property
    def width(self): return self._width

    @width.setter
    def width(self, width):
        if self._validate_value(width):
            self._width = width
        else:
            print(f'outside of the range: {width}')


    def __str__(self): return f' Figure Geometric: width -> {self._width}, height -> {self._height}'

    # private method
    def _validate_value(self, value):
        return True if 0 < value < 10 else False

