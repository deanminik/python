# different to give format to a string

# old style_____________________________
name = 'Juan'
mi_cadena = 'Hello, %s' % name
print(mi_cadena)
"""
Hello, Juan
"""

# convert integer  to hexadecimals
error = 500
hexa_number = 'Hexadecimals : %x' % error
print(hexa_number)
"""
Hexadecimals : 1f4
"""

# with many values use a duple
cadena = 'Hello %s there is an error: %x ' % (name, error)
print(cadena)
"""
Hello Juan there is an error: 1f4  
"""
# dictionaries
cadena = 'hello %(name)s there is an error %(error)x, %(name)s ' % {'name':name, 'error':error}
print(cadena)
"""
hello Juan there is an error 1f4, Juan 
"""