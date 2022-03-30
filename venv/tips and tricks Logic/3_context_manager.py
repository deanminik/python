"""
remember: with -> provide all resources, and we do not need to close them
"""

from contextlib import contextmanager


with open('3_test_content_manager.txt', 'w') as file:
    file.write('Hello from python')

# this is the same without (with):
"""
file = open('3_test_content_manager.txt','w')
try:
    file.write('Hello from python version 2')
finally:
    file.close()
"""

# this is not the same and it is not a good practice
"""
file = open('3_test_content_manager.txt','w')
file.write('hello without (with)')
file.close()
"""

# Handle context manager with classes
# 1. adding protocol with the functions (__enter__) and (__exit__)
# 2. Using the library contextlib

# Option 1
class HandleFiles:
    def __init__(self, name):
        self.name = name
        print(f'The parameter name is : 3_test_content_manager.txt')

    def __enter__(self):
        self.file = open(self.name, 'w')
        print('enter method')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit method')
        if self.file:
            self.file.close()
            print('closing...')

# using contextmanager
@contextmanager
# this method is a generator, this gets the resource
# after, suspend temporally the execution of yield
# and when this finish, this go back to the execution and close the resource
def handleFilesGenerator(name):
    try:
        file = open(name, 'w')
        yield file

    finally: # to close our resource
        file.close()

# add an identifier
class Identifier():
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
        # when we go out of a block of withs , for example start at the beginning.
        # this will decrement

    def print_this(self,text):
        print('  '*self.level + text)

# the same exerciser identifier with context-lib
class Identifier_with_contextlib():
    def __init__(self):
        self.level = 0

    # In this case we do not need enter end exit method like the previous one
    # In this case we are going to use the contextmanager
    @contextmanager
    def identifier(self):
        try:
            self.level += 1
            # end to stop the execution of the block when the yield finishes
            yield self
        finally:
            self.level -=1
     # so now we just have one method
    def print_this(self,text):
        print('  '*self.level + text)

if __name__ == '__main__':
    # implementing the protocol of context manager
    with HandleFiles('3_test_content_manager.txt') as file:
        file.write('Test from handle class')

    # test with the library of context-lib
    with handleFilesGenerator('3_test_content_manager.txt') as file:
        file.write('3_test_content_manager.txt')
        file.write('\nbye')

    with Identifier() as identifier:
        identifier.print_this('first level')
        with identifier:
            identifier.print_this('second level')
            identifier.print_this('second level continues')
            with identifier:
                identifier.print_this('third level')
        with identifier:
            identifier.print_this('ends level')


    # Identifier_with_contextlib():
    print()
    obj = Identifier_with_contextlib()
    with obj.identifier():
        obj.print_this('first level')
        obj.print_this('first level continue...')
        with obj.identifier():
            obj.print_this('second level')
            obj.print_this('second level continue...')
            with obj.identifier():
                obj.print_this('third level')
                obj.print_this('third level continue...')
        with obj.identifier():
            obj.print_this('finish of the first level ')



"""
enter method
exit method
closing...
"""

"""

   first level
    second level
    second level continues
      third level
    ends level
"""


"""
  first level
  first level continue...
    second level
    second level continue...
      third level
      third level continue...
    finish of the first level 
"""