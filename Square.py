from FigureGeometric import FigureGeometric
from Color import Color


class Square(FigureGeometric, Color): # the order is important
    def __init__(self, side, color):
        #super().__init__(side)
        FigureGeometric.__init__(self, side, side)
        Color.__init__(self, color)

    def calculator_are(self):
        return self.height * self.width

    def __str__(self):
        return f'{FigureGeometric.__str__(self)} {Color.__str__()}'