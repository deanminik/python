from handlingResources import HandlingResources

with HandlingResources('/home/lite/Desktop/calling-from-desktop.txt') as file:
    print(file.read())


"""
---------------we get the resource----------------
Hello from desktop dean with a txt file

--------------we closed the resource--------------

Process finished with exit code 0

"""

