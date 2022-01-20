class MyClass:

    variable_class = 'this is the value of the variable class' #thic will share with every class

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

print(MyClass.variable_class)
myclass = MyClass('Value variable instance')
print(myclass.instance_variable)
print(myclass.variable_class)

myclass2 = MyClass('Value variable instance from second object')
print(myclass2.instance_variable)
print(myclass2.variable_class)