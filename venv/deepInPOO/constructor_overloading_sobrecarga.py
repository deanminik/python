# In python there is not an overloading of constructors
# because we do not work directly with a constructor in python when we create classes
# the think we do is to work with the method __init__ however this not the only way to create objects

#*********************
# simulation of constructor overloading
# other ways to create object in python
class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    #more options -> constructor overloading
    @classmethod
    def create_empty_person(cls): # static method
        return cls(None, None) # in this case we add None because our method is about empty parameters

    @classmethod
    def create_person_with_values(cls, name, lastname): # static method
        return cls(name, lastname)


    def __str__(self):
        return f'Name: {self.name}, lastname: {self.lastname}'


person1 = Person('JUan','fdz')
print(person1)
"""
Name: JUan, lastname: fdz
"""
person_empty = Person.create_empty_person()
print(person_empty )
"""
Name: None, lastname: None
"""

person_with_values = Person.create_person_with_values('roy','hdz')
print(person_with_values)
"""
Name: roy, lastname: hdz
"""

# Practice
# convert of temperature
class TemperatureConverter:

      MAX_CELSIUS = 100
      MAX_FAHRENHEIT = 213
      # IMPORTANT: in python there is not constance so the community consider simulating with son practices
      # using uppercase with the class variable and underscore

      @classmethod
      def c_f(cls, celsius):
          if celsius > cls.MAX_CELSIUS:
              raise ValueError(f'Temperature C too height: {celsius}')
          return celsius * 9/5 + 32

      @classmethod
      def f_c(cls,fahrenheit):
          if fahrenheit > cls.MAX_FAHRENHEIT:
              raise ValueError(f'Temperature F too height: {fahrenheit}')
          return (fahrenheit-32) * 5/9


if __name__ == '__main__':
    result = TemperatureConverter.c_f(15)
    print(result)
    """
    59.0
    """
    result = TemperatureConverter.f_c(10)
    print(result)
    """
    -12.222222222222221
    """
    result = TemperatureConverter.c_f(150)
    print(result)
    """
    Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/deepInPOO/constructor_overloading_sobrecarga.py", line 77, in <module>
    result = TemperatureConverter.c_f(150)
  File "/home/lite/PycharmProject/LabGeometric/venv/deepInPOO/constructor_overloading_sobrecarga.py", line 56, in c_f
    raise ValueError(f'Temperature C too height: {celsius}')
ValueError: Temperature C too height: 150
    """

