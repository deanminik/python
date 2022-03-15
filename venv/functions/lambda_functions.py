# it is an anonymous function without names
# also are small functions
# and  those are witten in just one line


# normal function
def sum(a, b):
    return a + b

# lambda function
my_lambda_function = lambda a, b: a + b
print(my_lambda_function(10, 30))
"""
40
"""

# lambda function without arguments
my_lambda_function_2 = lambda: 'Function without arguments'
print(my_lambda_function_2())
"""
Function without arguments
"""

# lambda function with default arguments
my_lambda_function_3 = lambda a=2, b=3: a+b
print(my_lambda_function_3())
"""
5
"""

# lambda function with arguments variable *args and **kwargs ->(*tuples and **dictionaries)
my_lambda_function_4 = lambda *arg, **kwargs: len(arg) + len(kwargs)
print(my_lambda_function_4(1, 2, 3, a=5,b=6))
"""
5
"""

# mixing everything
my_lambda_function_5 = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(my_lambda_function_5(1,2,6, 5,6,7, e=8,f=8))
"""
14
"""