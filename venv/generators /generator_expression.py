# Generator expression
# this is an anonymous generator

multiplication = (value * value for value in range(4))
                   # 0*0=0 -> 1*1 = 1 -> 2*2=4 -> 3*3=9
print(multiplication)
"""
<generator object <genexpr> at 0x7f8550add120>
"""
print(next(multiplication))
print(next(multiplication))
print(next(multiplication))
print(next(multiplication))

"""
0
1
4
9
"""

# Generator expression in a function
import math
sum = sum(value * value for value in range(4))
print(f'Result of the sum : {sum}')
"""
Result of the sum : 14
"""

# example using a list o another iterator
mylist = ['Juan','Perez']
generator = (value for value in mylist)
print(next(generator))
print(next(generator))
"""
Juan
Perez
"""
# modify elements from a list
# create a string from a generator, created from a list
thislist = ['karla','Gomez']
counter = 0
def increment():
    global counter
    counter += 1
    return counter
# -> yield of or generator and for loop
generator_v = (f'{increment()}. {name}' for name in thislist)
thislist = list(generator_v)
print(thislist)
"""
['1. karla', '2. Gomez']
"""
chain = ', '.join(thislist)
print(f' The chain generated from the list:  {chain}')
"""
The chain generated from the list:  1. karla, 2. Gomez
"""


