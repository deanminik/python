# during this course we used the method __srt__ to overwrite the method and show the message
# but there are two ways more to represent object(string) in python

# Representation of objects (str, repr, format)
#print(dir(object))
"""
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
 '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
"""

class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    # repr -> more focused to developers that final users
    # The purpose is just to represent the code
    def __repr__(self):
        return f'{self.__class__.__name__}(name = {self.name}, lastname = {self.lastname})'

    # str -> more for final users
    # the implementation by default call the repr method
    def __str__(self):
        return f'{self.__class__.__name__}: {self.name} {self.lastname}'

    # format -> its implementation by default is str method
    # also it is called using f''
    # more extend or detailed
    def __format__(self, format_spec):
        return f'{self.__class__.__name__}: With name{self.name} and also lastname {self.lastname}'

person1 = Person('Luis','Monge')
# repr
print(f'Representation of the object person1: {person1!r}')   # !r -> this to ensure the call of __repr__ and not __str__
"""
Representation of the object person1: Person(name = Luis, lastname = Monge)
"""

# str
print(person1) # this call the str method by default
"""
Person: Luis Monge
"""

# format
print(f'{person1}') # with f string we do not need to use __format__
"""
Person: With nameLuis and also lastname Monge
"""
