class Order:
    orderCounter = 0

    def __init__(self, obj_computer):
        Order.orderCounter += 1
        self._id_order = Order.orderCounter
        self._obj_computer = obj_computer

    def __add__computer(self, obj_computer):
        # this will be our list
        self._obj_computer.append(obj_computer)

    def __str__(self):
        # this will contain all variables of type computer
        computers_str = ''
        for computer in self._obj_computer:
            # we are calling the all calls from the method __str__() and adding to our computers_str
            computers_str += computer.__str__()

        return f'''
            Order: {self._id_order}
            Computer: {computers_str}
        '''

