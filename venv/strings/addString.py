
tupla_str = ('Hello','welcome','to','Amazing','course')
message = ' '.join(tupla_str)
print(f'Message: {message}')

"""
Message: Hello welcome to Amazing course
"""

list_str = ['Hello','welcome','to','Amazing','course']
message = '/'.join(list_str)
print(f'Message: {message}')

"""
Message: Hello/welcome/to/Amazing/course
"""

str = 'hello'
message = '.'.join(str)
print(f'Message: {message}')

"""
Message: h.e.l.l.o
"""

dictionary = {'name':'Juan', 'lastname':'fdz','age':'18'}
keys = '-'.join(dictionary.keys())
values = '-'.join(dictionary.values())
print(f'Keys: {keys} type: {type(keys)}')
print(f'Values: {values} type: {type(values)}')

"""
Keys: name-lastname-age type: <class 'str'>
Values: Juan-fdz-18 type: <class 'str'>
"""