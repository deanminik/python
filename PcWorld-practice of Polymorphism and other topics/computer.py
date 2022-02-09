from keyboard import Keyboard
from monitor import Monitor
from mouse import Mouse


class Computer:
    computerCounter = 0

    def __init__(self, name, obj_monitor, obj_keyboard, obj_mouse):
        Computer.computerCounter += 1
        self._id_computer = Computer.computerCounter
        self._obj_name = name
        self._obj_monitor = obj_monitor
        self._obj_keyboard = obj_keyboard
        self._obj_mouse = obj_mouse

    def __str__(self):
        return f'''
         Id: {self._id_computer}, Name: {self._obj_name}
         Monitor: {self._obj_monitor}
         Keyboard: {self._obj_keyboard}
         Mouse: {self._obj_mouse}
         '''


# creating object from other classes
if __name__ == '__main__':
    keybo1 = Keyboard(entry_type='USB', brand='hp')
    keybo2 = Keyboard(entry_type='Bluetooth', brand='Samsung')
    keybo3 = Keyboard(entry_type='USB', brand='Lenovo')
    monitor1 = Monitor(brand='AOC', size='20')
    monitor2 = Monitor(brand='hp', size='16')
    monitor3 = Monitor(brand='Apple', size='18')
    mouse1 = Mouse(entry_type='USB', brand='hp')
    mouse2 = Mouse(entry_type='USB', brand='Samsung')
    mouse3 = Mouse(entry_type='USB', brand='LG')

    comp1 = Computer(name='hp', obj_mouse=mouse1, obj_monitor=monitor1, obj_keyboard=keybo1)
    print(comp1)
    comp2 = Computer(name='Lenovo', obj_mouse=mouse2, obj_monitor=monitor2, obj_keyboard=keybo2)
    print(comp2)
"""
      Id: 1, Name: hp
         Monitor: Id: 1, Brand: AOC, Size: 20
         Keyboard: Id: 1, Entry type: USB, Brand: hp
         Mouse: Id: 1, Entry type: USB, Brand: hp
         
      Id: 2, Name: Lenovo
         Monitor: Id: 2, Brand: hp, Size: 16
         Keyboard: Id: 2, Entry type: Bluetooth, Brand: Samsung
         Mouse: Id: 2, Entry type: USB, Brand: Samsung   
         
"""