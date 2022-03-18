class Person:
    person_counter = 0 # class attribute

    # our constructor
    def __init__(self, name, lastname):
        self.name = name # instance attribute
        self.lastname = lastname # instance attribute

# show the attribute of an object
person_1 = Person(name='marco', lastname='fdz')
print(f'This is the instance attributes: {person_1.__dict__}')
"""
This is the instance attributes: {'name': 'marco', 'lastname': 'fdz'}
"""

# create attribute at the time
print(person_1.person_counter)
"""
0
"""
person_1.person_counter = 10  # person_counter this is different to the class attribute up there
# it is impossible to modify directly with the object, just with the class
print(person_1.__dict__)
"""
{'name': 'marco', 'lastname': 'fdz', 'person_counter': 10}
"""

# to access to the class variable we need to use the class
print(Person.person_counter)
"""
0
"""

# object 2
person_2 = Person('roy', 'gomez')
print(person_2.__dict__)
"""
{'name': 'roy', 'lastname': 'gomez'}
"""

# associate a class attribute at the time
Person.counter_2 = 20
print(Person.counter_2)
"""
20
"""
"""
now we can access to this attribute using person1 or 2
"""
