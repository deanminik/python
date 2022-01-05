from Rectangle import Rectangle
from Square import Square

print('Creation square object'.center(50, '-'))

square1 = Square(side=-5, color='blue')
print(f'Calculation area square: {square1.calculator_are()}')
print(square1)

print('Creation rectangle object'.center(50, '-'))
rectangle1 = Rectangle(3, 8, 'Green')
print(f'Calculation area rectangle : {rectangle1.cal_area()}')
print(rectangle1)
