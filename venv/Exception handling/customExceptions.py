class CustomExceptions(Exception):
    def __init__(self, my_message):
        # message came from the class Exception
        self.message = my_message

