"""
We indicate to a developer to do not use these methods or attributes as
a part of the public interface

only use this inside the class
"""

#from _4_part_2 import *
from _4_part_2 import public_function
from _4_part_2 import _protected_function

class MyClase:
    def __init__(self):
        self.public_variable = 10
        self._protected_variable = 11


if __name__ == '__main__':
    obj = MyClase()
    print(obj.public_variable)
    print(obj._protected_variable)

    """
    10
    11
    we can access to a _protected_variable but it is protected and it is a bad practice 
    """

    #imported model
    public_function()
    """
    Public function in use
    """
    _protected_function()
    """
    Traceback (most recent call last):
     File "/home/lite/PycharmProject/LabGeometric/venv/tips and tricks Logic/4_nomenclature_attributes_methods.py", line 32, in <module>
    _protected_function()
    NameError: name '_protected_function' is not defined
    """

    """
    Also, it is not a recommendation to import with *
    the better way is just call part by part like this:
    
    from _4_part_2 import public_function
    from _4_part_2 import _protected_function
    """
    """
    Public function in use
    Protected function
    """