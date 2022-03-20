"""
https://docs.python.org/3/library/dataclasses.html
Data class is ise to generate automatically the method init and repr
"""
from dataclasses import dataclass
from typing import ClassVar

@dataclass(frozen=True)# this will be an immutable object
class Address:
    street: str
    number: int = 0


@dataclass(frozen=True)
class Person:
    name: str
    lastname: str
    address: Address
    person_counter: ClassVar[int] = 0 # this will be our class variable -> ClassVar

    def __post_init__(self):
        if not self.name:
            raise ValueError(f'Value of name empty: {self.name}')

address1 = Address('cartago',1)
person1 = Person('Dean','fdz', None)
print(person1)
# this generates automatically the repr method
"""
Person(name='Dean', lastname='fdz')
"""
# class variable
print(f'class variable: {Person.person_counter}')
"""
class variable: 0
"""

# instance variables
print(f'Instance variable : {person1.__dict__}')
"""
Instance variable : {'name': 'Dean', 'lastname': 'fdz'}
"""

# if we create a variable with empty values -> this will not a problem
#empty_person = Person('','')
#print(f'empty person: {empty_person}')
"""
empty person: Person(name='', lastname='')
"""
# we need to add a condition to prevent empty values
"""
Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/data classes/data_classes.py", line 37, in <module>
    empty_person = Person('','')
  File "<string>", line 5, in __init__
  File "/home/lite/PycharmProject/LabGeometric/venv/data classes/data_classes.py", line 16, in __post_init__
    raise ValueError(f'Value of name empty: {self.name}')
ValueError: Value of name empty: 
"""

# check equality values between objects
person2 = Person('Dean','fdz', Address('San JOse', 30))
print(f'The same objects? : {person1 == person2}')
"""
The same objects? : True
"""
# add the class to a collection -> dictionaries
ourCollection = {person1, person2}
"""
Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/data classes/data_classes.py", line 60, in <module>
    ourCollection = {person1, person2}
TypeError: unhashable type: 'Person'
"""
#to add this correctly add frozen in the dataclasses decorator
print(ourCollection)
"""
{Person(name='Dean', lastname='fdz')}
"""
# adding address -> create an address class
"""
{Person(name='Dean', lastname='fdz', address=None), Person(name='Dean', lastname='fdz', address=Address(street='San JOse', number=30))}
"""