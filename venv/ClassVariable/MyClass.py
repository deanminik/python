class MyClass:

    variable_class = 'this is the value of the variable class' #thic will share with every class

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    #creating a static method
    @staticmethod # remember, a decorator allows to affect the next method to associate the class by itself and not with the objects
    def static_method():
        print(MyClass.variable_class)
    #creating a class method
    @classmethod
    def class_method(cls): #we receive this parameter cls = class from classmethod
        print(cls.variable_class)

    def instance_method(self):
        #now we can access to the static method
        self.class_method()
        self.static_method()
        print(self.variable_class)
        print(self.instance_variable)


MyClass.class_method()
myObject1 = MyClass('variable_instance')
myObject1.class_method()
myObject1.instance_method()



#MyClass.class_method()
#MyClass.static_method()
"""
print(MyClass.variable_class)
myclass = MyClass('Value variable instance')
print(myclass.instance_variable)
print(myclass.variable_class)

myclass2 = MyClass('Value variable instance from second object')
print(myclass2.instance_variable)
print(myclass2.variable_class)

#this is a dynamic variable
MyClass.variable_class2 = 'Value variable class 2'
print(MyClass.variable_class2)
"""
