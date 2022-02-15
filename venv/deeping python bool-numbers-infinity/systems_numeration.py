# deepening numbering system

# Decimal
a = 10
print(f'Decimal: {a}')

# Binary
# will have the same result bus in the system it is in binary (b)
a = 0b1010
print(f'Binary: {a}')

# Octal
a = 0o12
print(f'Octal: {a}')

# Hexadecimal
a = 0xA
print(f'Hexadecimal: {a}')


# convert a number including the base
# decimal base
a = int('23', 10)
print(f'Decimal base:  {a}')
# binary base
a = int('10111', 2)
print(f'Binary base:  {a}')
# base Octal
a = int('27', 8)
print(f'Octal base:  {a}')
#Hexadeecimal base
a = int('17', 16)
print(f'Hexadecimal base:  {a}')

'''
Decimal: 10
Binary: 10
Octal: 10
Hexadecimal: 10
Decimal base:  23
Binary base:  23
Octal base:  23
Hexadecimal base:  23
'''

# float type
print('Float type'.center(50,'-'))
a = 3.0
print(f'a: {a}')

a = 3.0
print(f'using .2f or .3f or .... a: {a:.2f}')

# Constructor float can get int and str
a = float(10)
print(f'using .2f or .3f or .... and using float() strg a: {a:.2f}')
a = float('10')
print(f'using .2f or .3f or .... and using float() int a: {a:.2f}')

# Exponential notation (positive or negative values)
a = 3e5
print(f'Exponential notation positive 3e5 -> a: {a}')
a = 3e-5
print(f'Exponential notation negative 3e-5 -> a: {a}')

# Any calculation involving a float is promoted to a float.
print('Any calculation involving a float is promoted to a float. 4 + 5.0 ')
a = 4 + 5.0
print(a)
print(f'type : {type(a)}')

'''
--------------------Float type--------------------
a: 3.0
using .2f or .3f or .... a: 3.00
using .2f or .3f or .... and using float() strg a: 10.00
using .2f or .3f or .... and using float() int a: 10.00
Exponential notation positive 3e5 -> a: 300000.0
Exponential notation negative 3e-5 -> a: 3e-05
Any calculation involving a float is promoted to a float. 4 + 5.0 
9.0
type : <class 'float'>
'''