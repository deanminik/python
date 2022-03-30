# new style to give format in python

name = 'Juan'
mi_cadena = 'Hello, {}'. format(name)
print(mi_cadena)
"""
Hello, Juan
"""

#itenger to hexa
error = 500
cadena_hex = 'error en la hexadecimal: {e1:x}'.format(e1=error)
print(cadena_hex)

"""
error en la hexadecimal: 1f4
"""