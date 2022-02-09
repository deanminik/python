from EntryDevice import EntryDevice


class Mouse(EntryDevice):
    mouseCounter = 0

    def __init__(self, entry_type, brand):
        Mouse.mouseCounter += 1
        self._id_mouse = Mouse.mouseCounter
        super().__init__(entry_type, brand)

    def __str__(self):
        return f'Id: {self._id_mouse}, Entry type: {self._entry_type}, Brand: {self._brand}'
        # we can access to entry_type and brand even thought there are private due
        # we are calling them by the inheritance


# testing
mouse1 = Mouse(entry_type='USB', brand='hp')
mouse2 = Mouse(entry_type='USB', brand='Samsung')
mouse3 = Mouse(entry_type='USB', brand='LG')
print(mouse1)
print(mouse2)
print(mouse3)
