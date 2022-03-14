# it is a collections of the UNIQUES elements
# also it is mutable
# but the elements should be unmutable for example we cannot contain list because they are mutable

# only : string, int float et

group = {'juan',10,10.3}
print(group)

# empty set
group = set()
print(group)

# add new element
group.add('roy')
print(group)

# create a set from an iterable
group = set([4,5,6,8,9])
print(group)

# add another set
group2 = {100,200,300,300}
group.update(group2)
print(group)
"""
{4, 5, 6, 100, 8, 9, 200, 300}
"""
## there is no duplication of 300

# operations of sets elements
black_hair = {'juan','karla','ana','marco'}
blonde_hair = {'roy','victor','luis'}
brown_eyes = {'karla', 'luis'}
under_30 = {'juan','karla','marco'}
# -> union
# recover all elements with brown eyes and blonde hair
print(brown_eyes.union(blonde_hair))
"""
{'karla', 'luis', 'roy', 'victor'} # we got luis just once 
"""

# intersection -> recover the elements that they are in both sets
# brown eyes and blonde hair
print(brown_eyes.intersection(blonde_hair))
"""
{'luis'}

only luis is located in both sets 
"""

# difference -> just take the elements from just one set
print(black_hair.difference(under_30))
"""
{'ana'}

ana appears just once in both sets 
"""
# symmetric -> only returns the elements that exist in just one set

print(black_hair.symmetric_difference(under_30))
"""
{'ana'}
"""

# ask if a set is inside another one
print(under_30.issubset(black_hair))
"""
True

it is true because black hair is located before the under 30
"""


# ask if a set contains another set
print(under_30.issuperset(black_hair))
"""
False
we do not have completed the set in under 30, there are more elements in the first one 
"""

# if the black hair do not have blonde hair
print(black_hair.isdisjoint(blonde_hair))
"""
True
there is not relation between them 
"""