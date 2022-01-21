class Person:
    person_counter = 0 # this will be share with every object

    def __init__(self, name, age):
        Person.person_counter += 1
        self.id_person = Person.person_counter
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person [{self.id_person} {self.name} {self.age}]'


person1 = Person(name='Juan', age=28)
print(person1)
person2 = Person(name='Pedro', age=29)
print(person2)

#print
"""
Person [1 Juan 28]
Person [2 Pedro 29]
"""