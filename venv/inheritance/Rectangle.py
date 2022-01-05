from Color import Color
from FigureGeometric import FigureGeometric


class Rectangle(FigureGeometric, Color):
    def __init__(self, width, height, color):  # we are going to call the properties from father's classes
        # Calling the init from the father class Figure
        FigureGeometric.__init__(self, width, height)
        Color.__init__(self, color)

    def cal_area(self):
        return self.height * self.width

    def __str__(self):
        return f'{FigureGeometric.__str__(self)} {Color.__str__(self)}'
