from EntryDevice import EntryDevice


class Keyboard(EntryDevice):
    keyboardCounter = 0

    def __init__(self, entry_type, brand):
        Keyboard.keyboardCounter += 1
        self._id_keyboard = Keyboard.keyboardCounter
        super().__init__(entry_type, brand)

    def __str__(self):
        return f'Id: {self._id_keyboard}, Entry type: {self._entry_type}, Brand: {self._brand}'


if __name__ == '__main__':
    keybo1 = Keyboard(entry_type='USB', brand='hp')
    keybo2 = Keyboard(entry_type='Bluetooth', brand='Samsung')
    keybo3 = Keyboard(entry_type='USB', brand='Lenovo')
    print(keybo1)
    print(keybo2)
    print(keybo3)

"""
Id: 1, Entry type: USB, Brand: hp
Id: 2, Entry type: Bluetooth, Brand: Samsung
Id: 3, Entry type: USB, Brand: Lenovo
"""