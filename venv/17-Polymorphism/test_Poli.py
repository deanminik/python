from Employee import Employee
from Manager import Manager

def print_details(thisObject):
    print(thisObject) # automatically calls the str method
    print(type(thisObject))# this is to now what is the class that we are using

empl_father = Employee('Juan', 5000) #father class
print_details(empl_father)

"""
Employee: [Name: Juan, Salary: 5000] 
<class 'Employee.Employee'>
"""
manager_children = Manager('Boss', 7000, 'System')
print_details(manager_children)

"""
Manager [Department: System] Employee: [Name: Boss, Salary: 7000]
<class 'Manager.Manager'>
"""
