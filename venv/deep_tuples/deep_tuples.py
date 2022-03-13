# A tuple is immutable

# variables
a, b = 'hello', 'bye'
print(a, b)

# swap (exchange)
a, b = b, a
print(a, b)

"""
hello bye
bye hello
"""

# return multiple values in a function
def minmax(elements):
    return min(elements), max(elements)

min, max = minmax([1,10,15,20,45])
print(f'min value {min}, max value {max}')
"""
min value 1, max value 45
"""

# sum of a tuple
result = sum((1,10,15,20,45))
print(result)
"""
91
"""

# the sum of every argument
def mysum(*args):
    return sum(args)

result = mysum(1,10,15,20,45)
print(result)
"""
91
"""