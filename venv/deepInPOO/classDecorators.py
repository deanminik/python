# Class decorators
"""
it is pretty similar to functions decorators, we can modify in a programming way our class
"""
import inspect


def decorator_repr(cls):
    print('Execution of class decorator')
    print(f'We get the class object: {cls.__name__} ')

    # we check our attributes with (vars)
    attributes = vars(cls)
    # Iterate every attribute
    #for name, attribute in attributes.items():
    #    print(name, attribute)

    #check if init method has been overwritten
    if '__init__' not in attributes:
        raise TypeError(f'{cls.__name__} this has not overwritten the method __init__')

    # the signature includes the parameter of the method init
    signature_init = inspect.signature(cls.__init__)
    print(f'Signature of the method init: {signature_init} ')

    # recover the parameters, exec self
    init_parameters = list(signature_init.parameters)[1:] # this is to avoid self parameter end start after that
    print(f'Init parameters: {init_parameters}')

    # check if every parameter has a property method associated
    for parameter in init_parameters:
        is_method_property = isinstance(attributes.get(parameter), property)
        if not is_method_property:
            raise TypeError(f'No exist a method property for this parameter: {parameter}')

    # create the repr dynamically
    def repr_method(self):
        """
        we are going to simulate dynamically the __repr__ method
        def __repr__(self):
            return f'Person(name={self._name}, lastname={self._lastname})'
        """
        #***********************************************************************************************
        # we get the name of the class dynamically
        class_name = self.__class__.__name__
        print(f'name of the class: {class_name}')
        # we get the names of the properties and its values dynamically
        # Generator expression, create name_attribute=value_attribute
        argument_generator = (f'{name}={getattr(self,name)!r}' for name in init_parameters)
        # arguments list
        arg_list = list(argument_generator)
        print(f'List of the generator: {arg_list}')
        # create a string from now on arguments list
        arguments = ','.join(arg_list)
        print(f'Arguments of the repr method: {arguments}')
        # we created the shape of __repr__ method, without its name
        result_repr_method = f'{class_name}({arguments})'
        return result_repr_method



    # add dynamically the repr method to our class
    setattr(cls,'__repr__',repr_method)

    return cls


@decorator_repr
class Person:
    def __init__(self, name, lastname):
        print('2. Execution of init method')
        self._name = name
        self._lastname = lastname

    @property
    def name(self): # always name of the parameter
        return self._name

    @property
    def lastname(self):
        return self._lastname
    #pass



person1 = Person('juan','hdz')
# see the code inside the class decorator

"""
Execution of class decorator
We get the class object: Person 
2. Execution of init method
"""

"""
__module__ __main__
__init__ <function Person.__init__ at 0x7f099223eee0>
name <property object at 0x7f09922afc70>
lastname <property object at 0x7f09922aff90>
__dict__ <attribute '__dict__' of 'Person' objects>
__weakref__ <attribute '__weakref__' of 'Person' objects>
__doc__ None
Execution of init method

Process finished with exit code 0

"""

# if we comment the class and just add pass we get this
"""
Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/deepInPOO/classDecorators.py", line 23, in <module>
    class Person:
  File "/home/lite/PycharmProject/LabGeometric/venv/deepInPOO/classDecorators.py", line 17, in decorator_repr
    raise TypeError(f'{cls.__name__} this has not overwritten the method __init__')
TypeError: Person this has not overwritten the method __init__
"""

# the signature includes the parameter of the method init -> we were inspecting the method
"""
Signature of the method init: (self, name, lastname) 
"""

# recovering only parameters after self
"""
Init parameters: ['name', 'lastname']
"""

# check if a parameter has a method property
# also commenting a lastname method to test it
"""
Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/deepInPOO/classDecorators.py", line 40, in <module>
    class Person:
  File "/home/lite/PycharmProject/LabGeometric/venv/deepInPOO/classDecorators.py", line 34, in decorator_repr
    raise TypeError(f'No exist a method property for this parameter: {parameter}')
TypeError: No exist a method property for this parameter: lastname
"""


# create the repr dynamically.
# add dynamically the repr method to our class
print(person1)
"""
Result to execute the repr method
"""

# we get the name of the class dynamically
"""
name of the class: Person
"""

# this is the information of the repr method dynamically
"""
List of the generator: ["name='juan'", "lastname='hdz'"]
"""
#converting that list in a string
"""
Arguments of the repr method: name='juan',lastname='hdz'
"""
# we created the shape of __repr__ method, without its name
"""
Person(name='juan',lastname='hdz')
"""

#*********************************************************************************
# check is this class has the property name and lastname
print(dir(Person))
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
 'lastname', 'name']

"""

# has overwritten the repr method?
code_repr = inspect.getsource(person1.__repr__)
print(code_repr)

"""
   def repr_method(self):
        """
        we are going to simulate dynamically the __repr__ method
        def __repr__(self):
            return f'Person(name={self._name}, lastname={self._lastname})'
        """
        #***********************************************************************************************
        # we get the name of the class dynamically
        class_name = self.__class__.__name__
        print(f'name of the class: {class_name}')
        # we get the names of the properties and its values dynamically
        # Generator expression, create name_attribute=value_attribute
        argument_generator = (f'{name}={getattr(self,name)!r}' for name in init_parameters)
        # arguments list
        arg_list = list(argument_generator)
        print(f'List of the generator: {arg_list}')
        # create a string from now on arguments list
        arguments = ','.join(arg_list)
        print(f'Arguments of the repr method: {arguments}')
        # we created the shape of __repr__ method, without its name
        result_repr_method = f'{class_name}({arguments})'
        return result_repr_method


Process finished with exit code 0

"""