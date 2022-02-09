class Employee: #father class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'Employee: [Name: {self.name}, Salary: {self.salary}]'
