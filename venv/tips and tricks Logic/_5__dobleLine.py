"""
it is not only a convention, python also understand this concept of double line
and works making some changes
"""

class Father:
    def __init__(self):
        self.public_variable = 1
        self._protected_variable = 2
        self.__private_variable = 3

    def get_variable_private(self):
        return self.__private_variable

    def __private_method_from_father_class(self):
        print('Accessing to a private method from the fatherclass ')


class Child(Father):
    def __init__(self):
        super().__init__()
        self.public_variable = 'overwrite with 1'
        self._protected_variable = 'overwrite with 2'
        self.__private_variable = 'overwrite with 3'

    def __private_method_from_child_class(self):
        print('Accessing to a private method from the subclass ')

#using a global variable
_Test__variable_global = 10

class Test:
    def get_variable(self):
        return __variable_global

if __name__ == '__main__':
    # print all attributes
    father = Father()
    print(dir(father))

    """
    ['_Father__private_variable', '__class__', '__delattr__', '__dict__', 
    '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
    '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
    '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
    '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
    '_protected_varible', 'public_variable']

    """
    #print(f'Private variable : {father.__private_variable}')
    """
    Traceback (most recent call last):
    File "/home/lite/PycharmProject/LabGeometric/venv/tips and tricks Logic/__5__dobleLine.py", line 27, in <module>
    print(f'Private variable : {father.__private_variable}')
    AttributeError: 'Father' object has no attribute '__private_variable'
    """
    print(f'Private variable Using (name mangling){father._Father__private_variable}')

    """
    Private variable Using (name mangling)3
    """
    """
    from here was without get def  
    """
    """
    using get 
    """
    # name manglin is transparent for the developer
    print(f'access using get : {father.get_variable_private()}')
    """
    access using get : 3
    """
    # child test
    chil = Child()
    print(f'Public access from child: {chil.public_variable}')
    """
    Public access from child: overwrite with 1
    """
    print(f'Protected and not recommended access from child: {chil._protected_variable}')
    """
    Public access from child: overwrite with 2
    """
   # print(f'Private and not recommended access from child: {chil.__private_variable}')
    """
    Traceback (most recent call last):
    File "/home/lite/PycharmProject/LabGeometric/venv/tips and tricks Logic/__5__dobleLine.py", line 70, in <module>
    print(f'Private and not recommended access from child: {chil.__private_variable}')
    AttributeError: 'Child' object has no attribute '__private_variable'
    """
    """
    we can not access in that way 
    """
    # Now using name mangling from the child class
    print(f'Private variable Using (name mangling) from child :{chil._Child__private_variable}')
    """
    Private variable Using (name mangling) from child overwrite with 3
    """
    ## methods with double __
    # father.__private_method_from_father_class()
    """
    Traceback (most recent call last):
    File "/home/lite/PycharmProject/LabGeometric/venv/tips and tricks Logic/__5__dobleLine.py", line 90, in <module>
    father.__private_method_from_child_class()
    AttributeError: 'Father' object has no attribute '__private_method_from_father_class'
    """
    father._Father__private_method_from_father_class()
    """
    Accessing to a private method from the fatherclass 
    """
    chil._Child__private_method_from_child_class()
    """
    Accessing to a private method from the subclass 
    """
    father._Father__private_method_from_father_class()
    """
    Accessing to a private method from the fatherclass 
    """
    # accessing to a global variable
    print(f'accessing to a global variable {_Test__variable_global}')
    """
    accessing to a global variable 10
    """
    # using nam mangling and class to access to a global variable
    test = Test()
    print(f'accessing to a global variable from a class: {test.get_variable()} ')
    """
    accessing to a global variable from a class: 10 
    """