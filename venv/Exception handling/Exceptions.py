# example 1
print('Example 1')
# 10/0

"""
Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/Exception handling/Exceptions.py", line 1, in <module>
    10/0
ZeroDivisionError: division by zero
"""

try:
    10/0
except Exception as e:
    print(f'''
     We found the next error saved here (e)
     {e}
''')

"""
  We found the next error saved here (e)
     division by zero

"""

print('Example 2')

# example 2
result = None # none means that there is an assign value
a = 10
b = 0

try:
    result = a/b
except Exception as e:
# except ZeroDivisionError as e: this is more specific
    #print(f'There is an error:{e}')
    print(f'There is an error:{e}, {type(e)}')

print(f'Result {result}')


# example 3
# using else and finally
# print('Example 3')
# result2 = None
# try:
#     a = int(input('add the first number: '))
#     b = int(input('add the second number: '))
#     result2 = a/b
# except Exception as e:
#     print(f'There is an error : {e}, {type(e)}')
# else:
#     print('There is not exception :)') # this is when the code works correctly
# finally:
#     print('This (finally) executes whatever there is an error or not ')


# example 4
from customExceptions import CustomExceptions
print('Example 4')
result3 = None
# we are going to test if these number are the same
try:
    a = 5
    b = 5
    if a == b:
        raise CustomExceptions('They should not have the same value')
        # raise is used to display any kind of error. You can also be able to use for example
        # raise ValueError('this is an error due ...')
    result = a / b
except Exception as e:
    print(f'There is an error : {e}')


