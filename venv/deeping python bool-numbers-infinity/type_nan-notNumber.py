import math
from decimal import Decimal

# NaN -> Not a number
# it is an undefined data number
a = float('NaN')
print(f'a: {a}')
print(f'Is it a not a number? (NaN): {math.isnan(a)}')
'''
a: nan
Is it a not a number? (NaN): True
'''
a = Decimal('NaN')
print(f'a: {a}')
print(f'Is it a not a number? (NaN) using Decimal: {math.isnan(a)}')

'''
a: NaN
Is it a not a number? (NaN) using Decimal: True
'''