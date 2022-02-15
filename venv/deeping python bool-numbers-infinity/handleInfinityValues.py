# Using infinity values
import math
from decimal import Decimal

positive_infinity = float('inf')
print(f'Positive Infinity:{positive_infinity} ')
print(f'Is it infinity: {math.isinf(positive_infinity)}')
'''
Positive Infinity:inf 
Is it infinity: True
'''

positive_infinity = float('2.0')
print(f'Positive Infinity:{positive_infinity} ')
print(f'Is it infinity: {math.isinf(positive_infinity)}')
'''
Positive Infinity:2.0 
Is it infinity: False
'''

negative_infinity = float('-inf')
print(f'Positive Infinity:{negative_infinity} ')
print(f'Is it  infinity: {math.isinf(negative_infinity)}')

'''
Positive Infinity:-inf 
Is it  infinity: True
'''
# Module math
positive_infinity = math.inf
print(f'Positive Infinity using math:{positive_infinity} ')
print(f'Is it infinity: {math.isinf(positive_infinity)}')
'''
Positive Infinity using math:inf 
Is it infinity: True
'''

negative_infinity = -math.inf
print(f'Negative Infinity using math:{negative_infinity} ')
print(f'Is it infinity: {math.isinf(negative_infinity)}')
'''
Negative Infinity using math:-inf 
Is it infinity: True
'''

# Module decimal
positive_infinity = Decimal('Infinity')
print(f'Positive Infinity using decimal:{positive_infinity} ')
print(f'Is it infinity: {math.isinf(positive_infinity)}')

negative_infinity = Decimal('-Infinity')
print(f'Negative Infinity using decimal :{negative_infinity} ')
print(f'Is it infinity: {math.isinf(negative_infinity)}')

'''
Positive Infinity using decimal:Infinity 
Is it infinity: True
Negative Infinity using decimal :-Infinity 
Is it infinity: True

'''