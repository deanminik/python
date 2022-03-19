# Inheritance simple
"""
We are going to simulate a list. We won't go to use the type list. We are going
to create our own class and our child class will order our class
"""

# father class
class SimpleList:
    def __init__(self, elements):
        self._elements = list(elements)

    def addElement(self, element):
        self._elements.append(element)

    # type method built-in from list
    def __getitem__(self, item_index):
        return self._elements[item_index]

    def sorting(self):
        self._elements.sort()

    # built-in for list too
    def __len__(self):
        return len(self._elements) # how many elements are

    def __repr__(self): # representation for developer
        return f'{self.__class__.__name__} ({self._elements!r})' # !r -> call the attribute repr of the list that we defined


simpleList = SimpleList([5,3,6,8])
print(simpleList)
"""
SimpleList ([5, 3, 6, 8])
"""

class OrderList(SimpleList):
    def __init__(self, elements=[]): # with this, we do not call automatically the father class with its method __init__
        super().__init__(elements) #Now we are calling the method manually from father class
        # we order the elements when it is initialized
        self.sorting()

    def addElement(self, element):
        super().addElement(element) # this super is not calling the father class directly. It is calling,
        # the nex class of our MRO -> Method resolution order (see the end of this file to understand)
        # always order the element
        self.sorting()


orderList = OrderList([4,3,6,9,-1])
print(orderList)
"""
OrderList ([-1, 3, 4, 6, 9])
"""
# adding a new element
orderList.addElement(-14)
print(orderList)
"""
OrderList ([-14, -1, 3, 4, 6, 9])
"""

# len of our list
print(len(orderList))
"""
6
"""

# class to only add integer numbers (enteros)
class IntegerList(SimpleList):
    def __init__(self, elements=[]):
        for element in elements:
            self._validate(element)
        # if this an integer we add the element to our list
        super().__init__(elements)

    def _validate(self, element):
        # if this an integer we add the element to our list
        if not isinstance(element, int):
            raise ValueError(f'f This is not a integer value: {element}')

    # overwrite the addmethod from a class father
    def addElement(self, element):
        self._validate(element)
        # when it is validated we add to our list
        super().addElement(element)


# Integer list
# integerList = IntegerList(['hello',1,2,3])
"""
Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/deepInInheritance/ExampleOfInheritance.py", line 87, in <module>
    integerList = IntegerList(['hello',1,2,3])
  File "/home/lite/PycharmProject/LabGeometric/venv/deepInInheritance/ExampleOfInheritance.py", line 70, in __init__
    self._validate(element)
  File "/home/lite/PycharmProject/LabGeometric/venv/deepInInheritance/ExampleOfInheritance.py", line 77, in _validate
    raise ValueError(f'f This is not a integer value: {element}')
ValueError: f This is not a integer value: hello
"""

integerList = IntegerList([0,1,2,3,-15])
print(integerList)
"""
IntegerList ([0, 1, 2, 3, -15])
"""

# ****************************************************************************************************************
# multiple inheritance
# we are going to create a class to mix the children classes (order and integer)
class OrderAndIntegerList(IntegerList, OrderList):
    pass # we do not add any implementation for example __init__ because we are going to use our children classes

# order and integer
order_integer_list = OrderAndIntegerList([4,5,-1,10,14,-4])
print(order_integer_list)
"""
OrderAndIntegerList ([-4, -1, 4, 5, 10, 14])
"""
# adding a new element
order_integer_list.addElement(-20)
print(order_integer_list)
"""
OrderAndIntegerList ([-20, -4, -1, 4, 5, 10, 14])
"""


# order_integer_list.addElement('hello')
# print(order_integer_list)
"""
Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/deepInInheritance/multipleInheritance.py", line 123, in <module>
    order_integer_list.addElement('hello')
  File "/home/lite/PycharmProject/LabGeometric/venv/deepInInheritance/multipleInheritance.py", line 81, in addElement
    self._validate(element)
  File "/home/lite/PycharmProject/LabGeometric/venv/deepInInheritance/multipleInheritance.py", line 77, in _validate
    raise ValueError(f'f This is not a integer value: {element}')
ValueError: f This is not a integer value: hello

Process finished with exit code 1

"""

# Know the father class and its order
print(OrderAndIntegerList.__base__)
"""
<class '__main__.IntegerList'>
"""
print(OrderAndIntegerList.__bases__)
"""
(<class '__main__.IntegerList'>, <class '__main__.OrderList'>)
"""
#    Applying the concept of MRO -> Method Resolution Order
print(OrderAndIntegerList.__mro__)
"""
(<class '__main__.OrderAndIntegerList'>, <class '__main__.IntegerList'>, <class '__main__.OrderList'>, <class '__main__.SimpleList'>, <class 'object'>)
"""