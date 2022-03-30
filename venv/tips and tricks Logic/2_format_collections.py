"""
this applies to any kind of collections, list, set, dict and etc
Give a consistent list

"""

# Definition of a list in just one list
myList=['roy','marcos','ana']

# format
myList_v2 = [
    'juan',
    'lupe',
    'rita'
]

# give format with possible errors
myList_v3 = [
    'one',
    'two'
    'pedro'
]

print(myList)
print()
print(myList_v2)
print()
print(myList_v3)
"""
['roy', 'marcos', 'ana']

['juan', 'lupe', 'rita']

['one', 'twopedro']
"""
# the last one was joined with (two) because missed the (,)

# our format avoid missing the comma for example
myList_v4 = [
    'one',
    'two',
    'three',
    'four',
]
"""
In the last element we added a comma, to avoid errors like missing (,) Our eye can identify better the mistake
with this way of structure   
"""
print(myList_v4)
"""
['one', 'two', 'three', 'four']
"""