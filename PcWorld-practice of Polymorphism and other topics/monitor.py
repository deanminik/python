class Monitor:
    monitorCounter = 0

    def __init__(self, brand, size):
        Monitor.monitorCounter += 1
        self._id_monitor = Monitor.monitorCounter
        self._brand = brand
        self._size = size

    def __str__(self):
        return f'Id: {self._id_monitor}, Brand: {self._brand}, Size: {self._size}'


if __name__ == '__main__':
    monitor1 = Monitor(brand='AOC', size='20')
    monitor2 = Monitor(brand='hp', size='16')
    monitor3 = Monitor(brand='Apple', size='18')
    print(monitor1)
    print(monitor2)
    print(monitor3)

