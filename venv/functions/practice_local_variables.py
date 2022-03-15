counter = 0

def show_counter():
    print(counter)

def modify_counter(c):
    global counter
    counter = c

modify_counter(5)
show_counter()
"""
5
"""