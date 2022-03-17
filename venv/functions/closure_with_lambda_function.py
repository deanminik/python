# external function or main function
def operation(a,b):
    # 1. lambda function
    return lambda : a + b



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