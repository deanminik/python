print(dir(__builtins__)) # those are classes and method that we have available in python
"""
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 
'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 
'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 
'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 
'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError',
'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 
'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 
'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 
'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 
'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', 
'__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 
'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 
'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 
'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 
'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 
'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

"""

help(zip)
"""
class zip(object)
 |  zip(*iterables) --> A zip object yielding tuples until an input is exhausted.
 |  
 |     >>> list(zip('abcdefg', range(3), range(4)))
 |     [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
 |  
 |  The zip object yields n-length tuples, where n is the number of iterables
 |  passed as positional arguments to zip().  The i-th element in every tuple
 |  comes from the i-th iterable argument to zip().  This continues until the
 |  shortest argument is exhausted.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.


Process finished with exit code 0

"""

# so we can build iterables to build tuples

numbers = [1,2,3]
letters = ['a','b','c']
mix = zip(numbers, letters)
print(mix)
"""
so we have an object type zip 
<zip object at 0x7f6120aa12c0>
"""
print(list(mix))
"""
[(1, 'a'), (2, 'b'), (3, 'c')]
"""
print(f' this is a tuple{tuple(zip(numbers, letters))}')
"""
 this is a tuple((1, 'a'), (2, 'b'), (3, 'c'))
"""

# iterable with many elements at the same time
for numbers, letters in zip(numbers, letters):
    print(f'Numbers: {numbers}, Letters: {letters}')

"""
Numbers: 1, Letters: a
Numbers: 2, Letters: b
Numbers: 3, Letters: c
"""

"""
newList = []
for numbers, letters in zip(numbers, letters):
    newList.append(f'{numbers}-{letters}')
print(newList)
"""
"""

['1-a', '2-b', '3-c']
"""

# unzip
unmix = [(1,'a'),(2,'b'),(3,'c')]
un_numbers, un_letters = zip(*unmix)
print(f'Number {un_numbers} and letters {un_letters}')
"""
Number (1, 2, 3) and letters ('a', 'b', 'c') 
"""

# create a dictionary from list

mykeys = ['Name', 'Las name', 'Age']
values = ['Michael', 'Fernández', 18]
mydictionary = dict(zip(mykeys, values))
print(mydictionary)
"""
{'Name': 'Michael', 'Las name': 'Fernández', ' Age': 18}
"""

# update a element from our dictionary
thiskey = ['Age']
new_age = [45]
mydictionary.update(zip(thiskey, new_age))
print(mydictionary)
"""
{'Name': 'Michael', 'Las name': 'Fernández', 'Age': 45}
"""