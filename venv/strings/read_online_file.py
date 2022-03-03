# read online content
from urllib.request import urlopen

with urlopen('http://python.org/') as message:
    #content= message.read() # we got the bite
    content = message.read().decode('utf-8') # we convert the bite in unicode
    print(content)

with open('nuevo_archivo.txt','w', encoding='utf-8') as archivo:
    archivo.write(content) # save the content in a file
