# useful to unpack (*) the content of a variable

numbers = [1,2,3]
print(numbers)
print(*numbers)
"""
[1, 2, 3]
1 2 3
"""
print(*numbers, sep='-')
"""
1-2-3
"""
# use elements using unpacking
def sum(a, b, c):
    print(f'result of the sum of those elements: {a+b+c}')
sum(*numbers)
"""
result of the sum of those elements: 6
"""

# extract some elements of the list
##the_list = [1,2,3,4,5,6]
# or
the_list = list(range(1,7))

# a, b, c, d = the_list
# we go an error
"""
    a, b, c, d = the_list
ValueError: too many values to unpack (expected 4)
"""
a, *b, c, d = the_list
print(a, b, c, d)
"""
1 [2, 3, 4] 5 6

"""

# join list
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [list1, list2]
print(list3) # this will be an array
"""
[[1, 2, 3], [4, 5, 6]]
"""
list3 = [*list1, *list2]
print(list3)
"""
[1, 2, 3, 4, 5, 6]
"""

# join dictionaries
dic1 = {'a':1, 'b':2, 'c':3}
dic2 = {'d':4, 'e':5, 'f':6}
dic3 = {**dic1, **dic2}
print(dic3)
"""
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
"""

# * -> unpacking list
# ** -> unpacking dictionaries


# built a list from a string
str_list = [*'holamundo']
print(str_list)
"""
['h', 'o', 'l', 'a', 'm', 'u', 'n', 'd', 'o']
"""
# or, without space
print(*str_list, sep='')
"""
holamundo
"""