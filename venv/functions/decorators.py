# Decorators
# With a decorator you can modify a function before returning the result, using another function.
# it is a function that gets a function and return another one
# it is used to extend functionalities

# 1- function decorator (a)
# 2- function to decorate (b)
# 3- function decorated (c)

def decorator_function_a(function_to_decorate_b_calling_show_message_function_or_another_function):
    def decorated_function_c():
        print('Before to execute the function')
        function_to_decorate_b_calling_show_message_function_or_another_function() # this return -> "show_message function"
        print('After of the execution of the function')

    return decorated_function_c
"""
with the decorator we are calling another function before to release the below function show_message(), also working 
with this function  show_message() because you can modify it 
"""
@decorator_function_a # we are calling another function before to release the below function show_message()
def show_message():
    print('show_message function')

show_message()
"""
Before to execute the function
show_message function
After of the execution of the function
"""

print('Another example using arguments'.center(50,'*'))
# ********************************************************************************************
# Decorators with parameters arg
def decorator_function_av2(function_to_decorate_b_calling_show_message_function_or_another_function):
    def decorated_function_c(*args, **kwargs):
        print('Before to execute the function')
        result = function_to_decorate_b_calling_show_message_function_or_another_function(*args, **kwargs)
        print('After of the execution of the function')
        return result

    return decorated_function_c

@decorator_function_av2
def sum(a, b):
    return a + b

result = sum(5, 6)
print(result)
"""
Before to execute the function
After of the execution of the function
11
"""
