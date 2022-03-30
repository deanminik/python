"""
use for convention
also are temporal
(_)
"""

for _ in range(3):
    print('hello...')
"""
hello...
hello...
hello...
"""

# duple
values = ('Juan','Perez', 31)
name, _ ,age = values
print(name)
print(age)
print(f'variable without importance: {_}')
"""
Juan
31
variable without importance: Perez
"""

# list
_ = list()
_.append(1)
_.append(2)

print(_)
"""
[1, 2]

"""

# useful for temporal process