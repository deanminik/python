"""
It is not the same meaning of constance from other languages. In python, it just a convention
So it just to define the value to a variable, and it won’t be able to modify the value just in terms but with
python it is possible to modify the value.

There is a recommendation to use the variables in a different module
"""
#1- To use the convention, it is a required to write with uppercase the variable
MY_CONSTANCE = 'The value of my constance'

class Mathematics:
    PI = '3.1416' #REMEMBER: This is a variable of class because it is outside the any method
    #And it is associated with the class and not with the objects
    #We can access to this variable from another module just calling the class. It is not necessary
    #to build an object to access to this variable PI

