
def sum(a,b):
    return a+b

# add a function to a variable
my_function = sum

# verify the type of variable
print(type(my_function))
"""
<class 'function'>
"""

# call the function through of the variable
result = my_function(6,5)
print(result)
"""
11
"""

# function as an argument
def operation(a,b,sum_arg):
    print(f'Result sum {sum_arg(a,b)}')


operation(5,5, sum)
"""
Result sum 10
"""

# return a function from other function
def return_function():

    return sum

my_function_return = return_function()
print(f'Result of the function returned {my_function_return(7,7)}')
"""
Result of the function returned 14
"""