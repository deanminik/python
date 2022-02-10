# file = open('test.txt', 'r')
# file2 = open('text-spanish.txt', 'r')
#print(file.read())
#print(file2.read())
#print(file2.read(5)) # five characters
#print(file2.readline())

# this is to see the path of the file
import os
path = os.path.join(os.path.expanduser('~'), 'desktop', 'calling-from-desktop.txt')
print (path)
# for some reason desktop appears with lowercase, so change the d -> D


file_from_desktop = open('/home/lite/Desktop/calling-from-desktop.txt','r')
print(file_from_desktop.read())