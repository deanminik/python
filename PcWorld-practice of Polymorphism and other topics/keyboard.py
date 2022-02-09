from EntryDevice import EntryDevice


class Keyboard(EntryDevice):
    keyboardCounter = 0

    def __init__(self, entry_type, brand):
        Keyboard.keyboardCounter += 1
        self._id_keyboard = Keyboard.keyboardCounter
        super().__init__(entry_type, brand)


