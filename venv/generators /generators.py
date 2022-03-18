# Generators
# It is a special function, returns a sequence of values
# suspend the executions of the function (Yield) -> produce, in spanish
# with this reserved word, we avoid to use return


# IMPORTANT : the best case to use a generator is when we don't know the size of a list
#   Look the generator_expression.py
#   also apart, the generators use tuples instead list
def generator():
    yield  1
    print('The yield 1 was consumed')
    yield  2
    print('The yield 2 was consumed')
    print('The yield 3 will be consumed')
    yield  3


# we are going to consume depending on the demand
gen = generator()

# with every call we consume a value
print(next(gen))
"""
1
"""
print(next(gen))
"""
2
"""
print(next(gen))
"""
3
"""
# if try to consume more values than three we will get an error
# print(next(gen))
"""
Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/generators /generators.py", line 27, in <module>
    print(next(gen))
StopIteration
"""

# consuming the values of generator with a loop
for value in generator():
    print(f'The value is : {value}')

"""
The value is : 1
The yield 1 was consumed
The value is : 2
The yield 2 was consumed
The yield 3 will be consumed
The value is : 3
"""