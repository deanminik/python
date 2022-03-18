# List comprehensions
# here we use list instead tuples

numbers = range(10)
taking_pairs_list = []

# Create a new list with the number pair multiplied by itself
for number in numbers:
    if number % 2 == 0:
        # taking_pairs_list.append(number)
        taking_pairs_list.append(number*number)

print(f'Pair list: {taking_pairs_list}')
"""
Pair list: [0, 2, 4, 6, 8]
"""
"""
Pair list: [0, 4, 16, 36, 64]
"""

# start with list comprehension
# [expression for var in collection if condition]
# the condition if, is optional
taking_pairs_list_v2 = [number*number for number in numbers if number % 2 == 0]
print(taking_pairs_list_v2)
"""
[0, 4, 16, 36, 64]
"""

# Another example but wih 2 conditions
# we add the element to the list if the number is true twice
# condition: the number should be divisible between 2 and 6
pairs = [number for number in range(50) if number % 2 == 0 if number % 6 == 0]
print(pairs)
"""
[0, 6, 12, 18, 24, 30, 36, 42, 48]
"""

# adding if else, this is without a list comprehension
list_pairs_v3 = []
list_impairs = []
for number in range(10): # 0-9
    if number % 2 == 0:
        list_pairs_v3.append(number)
    else:
        list_impairs.append(number)


print(f'Pair list: {list_pairs_v3}')
print(f'Impair list: {list_impairs}')
"""
Pair list: [0, 2, 4, 6, 8]
Impair list: [1, 3, 5, 7, 9]
"""

# the same example but with list comprehension
list_pairs_v4 = []
list_impairs_v4= []
 # -> expression                 condition                                            loop
[list_pairs_v4.append(number) if number % 2 == 0 else list_impairs_v4.append(number) for number in range(10)]

print(f'Pair list: {list_pairs_v4}')
print(f'Impair list: {list_impairs_v4}')
"""
Pair list: [0, 2, 4, 6, 8]
Impair list: [1, 3, 5, 7, 9]
"""

# another example is to take a list of list and convert in just one list
list_of_list = [[1,2,3],[4,5,6],[7,8,9,10]]
# convert the list of list in just one list
# so create a list comprehension
simple_list = [sublist for sublist in list_of_list ]
print(simple_list)
"""
[[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
# but we need to iterate every sublist
"""
simple_list = [value
               for sublist in list_of_list
                    for value in sublist]
print(simple_list)
"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

# create a pair of list, using the result of previous example  without list comprehension
pair_list = []
for sublist in list_of_list:
    for value in sublist:
        if value % 2 == 0:
            pair_list.append(value)

print(pair_list)
"""
[2, 4, 6, 8, 10]
"""

# now using list comprehension
pair_list = []
pair_list = [value for sublist in list_of_list for value in sublist if value % 2 == 0]
print(pair_list)
"""
[2, 4, 6, 8, 10]
"""
