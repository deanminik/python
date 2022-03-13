names1 = ['Juan','Karla','pedro']
names2 = 'Laura Maria Gonzalo Ernesto'.split()

# plus list

print(f'Addition list: {names1 + names2} ')

"""
Addition list: ['Juan', 'Karla', 'pedro', 'Laura', 'Maria', 'Gonzalo', 'Ernesto'] 
"""

# extend list
names1.extend(names2)
print(f'extend the list 1 with the 2 {names1}')

"""
extend the list 1 with the 2 ['Juan', 'Karla', 'pedro', 'Laura', 'Maria', 'Gonzalo', 'Ernesto']
"""

# find the index of a list

mylist = [1,2,3,4,5,6,7,8,98]
print(f'Index 4: {mylist.index(4)}')
"""
Index 4: 3
"""

# reverse
mylist.reverse()
print(mylist)

"""
[98, 8, 7, 6, 5, 4, 3, 2, 1]
"""

# sort list
mylist.sort()
print(mylist)
"""
[1, 2, 3, 4, 5, 6, 7, 8, 98]
"""

# get min and max of a list
print(min(mylist))
print(max(mylist))

"""
1
98
"""

# copy a list to another list
help(list.copy)
"""
Help on method_descriptor:

copy(self, /)
    Return a shallow copy of the list.
"""
"""
shallow means that is just a reference so it returns a new object in memory 
"""
copylist = mylist.copy()
print(copylist)
"""
[1, 2, 3, 4, 5, 6, 7, 8, 98]
"""
print(f'The same reference? : { mylist is copylist}')
"""
The same reference? : False
"""

print(f'They have the same content : { mylist == copylist}')
"""
They have the same content : True
"""

# other way to make a copy of the list

copylist = list(mylist)
print(copylist)
"""
[1, 2, 3, 4, 5, 6, 7, 8, 98]
"""

# multiplication of list

multiplicationList = 5*[[2, 5]]
print(multiplicationList)
"""
[[2, 5], [2, 5], [2, 5], [2, 5], [2, 5]]
"""
print(f'The same reference: {multiplicationList[0] is multiplicationList[1]}')
"""
The same reference: True
"""
"""
So every list inside the list multiplicationList is the same object so they have the same memory position 
"""

# Arrays (matrices)
myArray = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(myArray)
print(f'row 0, column 0: {myArray[0][0]}')
"""
row 0, column 0: 10
"""
print(f'row 2, column 3: {myArray[2][3]}')
"""
row 2, column 3: 90
"""

# modify an array
myArray[2][3] = 100
print(myArray)
"""
[[10, 20], [30, 40, 50], [60, 70, 80, 100]]
"""

# order an array
list_of_list = [[10,14,87,90,71], [1,4,7,9], [11,144,879,2,6,3]]
print(list_of_list)
list_of_list.sort(key=len) # count of the elements in every sublist
print(list_of_list)
"""
[[10, 14, 87, 90, 71], [1, 4, 7, 9], [11, 144, 879, 2, 6, 3]]
[[1, 4, 7, 9], [10, 14, 87, 90, 71], [11, 144, 879, 2, 6, 3]]
"""

# "built in" -> this is part of the language of python -> the function that we are going to use is "sorted"
help(sorted)
"""
Help on built-in function sorted in module builtins:

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
"""

names_1 = ['roy', 'pedro', 'karla', 'Juan']
print(names_1)
names_1 = sorted(names_1)
print(names_1)
"""
['roy', 'pedro', 'karla', 'Juan']
['Juan', 'karla', 'pedro', 'roy']
"""
# that was alphabetically
#this is alphabetically but from z to a
names_1 = sorted(names_1, reverse=True)
print(names_1)
"""
['roy', 'pedro', 'karla', 'Juan']
"""

# order using the "len" -> large of the every element
names_1 = sorted(names_1, key=len)
print(names_1)
"""
['roy', 'Juan', 'pedro', 'karla']
"""

names_1 = sorted(names_1, key=len, reverse=True)
print(names_1)
"""
['pedro', 'karla', 'Juan', 'roy']
"""