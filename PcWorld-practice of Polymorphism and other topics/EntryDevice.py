class EntryDevice:

    def __init__(self, entry_type, brand):
        # (_) -> encapsulation
        self._entry_type = entry_type
        self._brand = brand

    # @property
    # def entry_type(self):
    #     return self._entry_type
    #
    # @property
    # def brand(self):
    #     return self._brand

    """"
    We have created another 'python packaged' with the name of 'PcWorld-practice'
    automatically there is file called '__init__.py' -> it's for compatibility with 
    other version, but currently it is not necessary with the new versions of python 
      
    """