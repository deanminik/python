# closure -> cierre
# this defines another one and also returns
# the local variables could be use it from external functions

# external function or main function
def operation(a, b):
    # intern function
    def sum():
        return a + b # here they are the variables coming from operation

    # return the function
    return sum # without parentheses because we aren't call it the method. We are return it the method


my_function_closure = operation(5,5)
print(my_function_closure)
"""
<function operation.<locals>.sum at 0x7fe776bc3c10>
"""
print(my_function_closure())
"""
10
"""

# this is another way to call it
print(operation(10,15)())
"""
if we leave without parentheses we just call the function operation, 
to return the function sum add  () 
"""
"""
25
"""