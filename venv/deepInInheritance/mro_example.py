class Class1:
    def __init__(self):
        print('Class1.__init__')

    def method(self):
        print('class 1 method')


class Class2(Class1):
    def __init__(self):
        print('Class2.__init__')

    def method(self):
        print('class 2 method')
        super().method()


class Class3(Class1):
    def __init__(self):
        print('Class3.__init__')

    def method(self):
        print('class 3 method')
        super().method()



class Class4(Class2,Class3):
    def method(self):
      print('class 4 method')
      super().method()

class4 = Class4()
"""
Class2.__init__
"""
print(Class4.__bases__)
"""
(<class '__main__.Class2'>, <class '__main__.Class3'>)
"""
# implementing MRO -> Method Resolution Order
print(Class4.__mro__)
"""
(<class '__main__.Class4'>, <class '__main__.Class2'>, <class '__main__.Class3'>, <class '__main__.Class1'>, <class 'object'>)
"""
# with that we could see the all classes involve in this class 4 with the order from left to right

# which method is executed (class 2 or class 3 ?)
print(class4.method())
"""
class 4 method
"""
## using pass
"""
class 2 method
"""
# also, if we comment the method in the class 2
"""
class 3 method
"""
# if we comment in class 3 too
"""
class 1 method
"""

# so it was the same order as the Method Resolution Order presentation

# if we comment the last one wi get this error
"""
Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/deepInInheritance/mro_example.py", line 47, in <module>
    print(class4.method())
AttributeError: 'Class4' object has no attribute 'method'
"""

# you can change the order of 2 to 3 just changing in class 4 the position of the father classes (Class3,Class2)
"""
(<class '__main__.Class4'>, <class '__main__.Class3'>, <class '__main__.Class2'>, <class '__main__.Class1'>, <class 'object'>)
"""

# adding super to all methods
"""
class 4 method
class 2 method
class 3 method
class 1 method
"""
