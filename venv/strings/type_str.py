from my_clase import MyClass

 # help(MyClass)

""" print out->
class MyClass(builtins.object)
 |  This is an example of the document of our class
 |  
 |  Methods defined here:
 |  
 |  __init__(self)
 |      Method -> begin of our class
 |  
 |  my_method(self, param1, param2)
 |      :param param1:
 |      :param param2:
 |      :return:
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
"""

# print(MyClass.__doc__) # but this only shows the documentation of the class part not the documentation of the methods parts

"""
    This is an example of the document of our class
"""

# to see the documentation de init method try this

# print(MyClass.__init__.__doc__) # to see the documentation de init method try this

"""
        Method -> begin of our class
"""

print(MyClass.my_method.__doc__)

"""
        :param this is the parameter 1 -> param1:
        :param this is the parameter 2 -> param2:
        :return:
        
"""