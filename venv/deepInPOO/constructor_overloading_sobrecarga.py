# In python there is not an overloading of constructors
# because we do not work directly with a constructor in python when we create classes
# the think we do is to work with the method __init__ however this not the only way to create objects

#*********************
# simulation of constructor overloading
# other ways to create object in python
class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    #more options -> constructor overloading
    @classmethod
    def create_empty_person(cls): # static method
        return cls(None, None) # in this case we add None because our method is about empty parameters

    @classmethod
    def create_person_with_values(cls, name, lastname): # static method
        return cls(name, lastname)


    def __str__(self):
        return f'Name: {self.name}, lastname: {self.lastname}'


person1 = Person('JUan','fdz')
print(person1)
"""
Name: JUan, lastname: fdz
"""
person_empty = Person.create_empty_person()
print(person_empty )
"""
Name: None, lastname: None
"""

person_with_values = Person.create_person_with_values('roy','hdz')
print(person_with_values)
"""
Name: roy, lastname: hdz
"""