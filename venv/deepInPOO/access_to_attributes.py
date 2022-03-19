# accesses to attribute:

# public
# protected -> to hidde data from an object in python
# private

# these concepts are not the same from other languages specially protected and private

class MyClass:
    def __init__(self, public, protected, private):
        self.public = public
        self._protected = protected # only be able to access to this variable from the class
        self.__private = private # we won't modify this variable outside the class
        # this is just for good practice, because you can void these rules


object1 = MyClass('Public value','Protected value','Private value')

# access to a public attribute
print(object1.public)
#  -> modify the public value
object1.public = 'Public value modified '
print(object1.public)
"""
Public value
Public value modified 
"""
#*************************************************************************************
# access to a protected attribute
print(object1._protected) # displays a warning about this is protected. You can use it but it is not recommended
"""
Protected value
"""
object1._protected = 'Protected value modified'
print(object1._protected)
"""
Protected value modified
"""

# access to a private value
# print(object1.__private)
"""
Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/deepInPOO/access_to_attributes.py", line 41, in <module>
    print(object1.__private)
AttributeError: 'MyClass' object has no attribute '__private'
"""

"""
python automatically hides the private attribute 
"""

# but there is a way to access
print(object1._MyClass__private)
"""
Private value
"""

object1._MyClass__private = 'New private value'
print(object1._MyClass__private)
"""
New private value
"""
# this is not recommended





