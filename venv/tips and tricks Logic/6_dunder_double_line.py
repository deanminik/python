# dunder = Double underscore
# like this : if __name__ == '__main__':
# those are method overwritten

class Father:
    def __init__(self):
        # use double score at the beginning and end
        # this won't use name mangling
        self.__dunder_variable__ = 10


if __name__ == '__main__':
    father = Father()
    #print(dir(father))
    print(father.__dunder_variable__)
    """
    10
    """