class FigureGeometric:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    # get section
    @property
    def height(self): return self._height

    # set section
    @height.setter
    def height(self, height): self._height = height

    @property
    def width(self): return self._width

    @width.setter
    def width(self, width): self._width = width

    def __str__(self): return f' Figure Geometric: width -> {self._width}, height -> {self._height}'
