from keyboard import Keyboard
from monitor import Monitor
from mouse import Mouse
from computer import Computer
from order import Order

keybo1 = Keyboard(entry_type='USB', brand='hp')
keybo2 = Keyboard(entry_type='Bluetooth', brand='Samsung')

monitor1 = Monitor(brand='AOC', size='20')
monitor2 = Monitor(brand='hp', size='16')

mouse1 = Mouse(entry_type='USB', brand='hp')
mouse2 = Mouse(entry_type='USB', brand='Samsung')


comp1 = Computer(name='hp', obj_mouse=mouse1, obj_monitor=monitor1, obj_keyboard=keybo1)
comp2 = Computer(name='Lenovo', obj_mouse=mouse2, obj_monitor=monitor2, obj_keyboard=keybo2)

# creating the list
computers = [comp1, comp2]
# creating the first order
order1 = Order(obj_list_computer=computers)
print(order1)
