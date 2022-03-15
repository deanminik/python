# dictionaries save an order. The sets do not.

mydictionary = {'Name':'Dean', 'Lastname':'fdz','age':'28'}
print(mydictionary)

#the dictionaries are mutable but the key is unmutable

#mydictionary = {(1,2):'value1'}
#print(mydictionary)

# add a key with the value if this no exist
mydictionary['department'] = 'system'
print(mydictionary)
"""
{'Name': 'Dean', 'Lastname': 'fdz', 'age': '28', 'department': 'system'}
"""

# there are no values duplicated
mydictionary['Name'] = 'roberto'
print(mydictionary)
"""
{'Name': 'roberto', 'Lastname': 'fdz', 'age': '28', 'department': 'system'}
"""

# recover elements with the key
print(mydictionary['Name'])
"""
roberto
"""

# recover elements with the get method
print(mydictionary.get('Name','We did not find the key'))
"""
roberto
"""
print(mydictionary.get('Name__________','We did not find the key'))
"""
We did not find the key
"""

# recover elements with the set default
thisname = mydictionary.setdefault('Name','Value by default')
print(thisname)
"""
roberto
"""

thisname = mydictionary.setdefault('Name***','Value by default')
print(thisname)
"""
Value by default
"""

# recover elements with the pprint
from pprint import pprint as pp
help(pp)
"""
Help on function pprint in module pprint:

pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True)
    Pretty-print a Python object to a stream [default is sys.stdout].
"""

pp(mydictionary)
"""
{'Lastname': 'fdz',
 'Name': 'roberto',
 'Name***': 'Value by default',
 'age': '28',
 'department': 'system'}
"""