class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        # objet1 + objet2 -> objet1.__add__(objet2)
        # we are overwriting this method from object class
        # you can only  use 2 objects
        return f'{self.name} {other.name} '

    def __sub__(self, other):
        return self.age - other.age

person_1 = Person('Pedro',20)
person_2 = Person('Carlos',8)
print(person_1 + person_2)
print(person_1 - person_2)
