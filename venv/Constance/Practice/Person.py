class Person:
    person_counter = 0 # this will be share with every object
    @classmethod
    def generate_netx_value(cls):  # REMEMBER: with this (cls) we access to our class variables
        cls.person_counter += 1
        return cls.person_counter

    def __init__(self, name, age):
        #Person.person_counter += 1
        self.id_person = Person.generate_netx_value()
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