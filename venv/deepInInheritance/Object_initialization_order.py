# Object initialization order

class Father:
    def __init__(self):
        print('Initialization of the father class')

    def method(self):
        print('Father method')

father1 = Father() # when you run without print this show the next message
"""
Initialization of the father class
"""
father1.method()
"""
Father method
"""

class Child(Father):
    pass # to avoid the initialization method __init__ of Child and use father class
child1 = Child()
"""
Initialization of the father class
"""

class Chil_2(Father):
    def __init__(self):
        print('Initialization of child')



child2 = Chil_2()
"""
Initialization of child
"""

class Chil_3(Father):
    def __init__(self):
        # In an option may we can call the method init from father class too using super()
        super().__init__()
        print('Initialization of child')
        # overwrite the method from the father class
    def method(self):
        print('Overwritten the father class')

child3 = Chil_3()
"""
Initialization of the father class
Initialization of child
"""
child3.method()
"""
Overwritten the father class
"""