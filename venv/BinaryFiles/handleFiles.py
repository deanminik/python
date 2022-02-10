try:
    file = open('test.txt','w') # we create this file
    file.write('Adding information to this file \n')
    file.write('Bye')
    # encoding='utf8' -> to work with accents in spanish
    # but in the new version is not necessary, it  works correctly
    file2 = open('text-spanish.txt', 'w', encoding='utf8')
    file2.write('Información admisión está \n')
    file2.write('Adios')
except Exception as e:
    print(e)
finally:
    file.close() # we won't be able to work with this file
    file2.close()
    print('files created')

