class HandlingResources:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("we get the resource".center(50,'-'))
        self.name = open(self.name, 'r')
        return self.name

    def __exit__(self, Exception_type, Exception_value, traceback_list_errors):
        # this will call when we finish in the method with from another file
        print('we closed the resource'.center(50,'-'))
        if self.name: # if this file is headed to an object
            self.name.close()
            # if we feel that maybe this resource ir open, we can add
            # this conditional to ask if this is closed
