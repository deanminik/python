# bool
# numeric type false = 0

value = 0
result = bool(value)
print(f'Value: {value}, result:{result}')
'''
Value: 0, result:False
'''

value = 5
result = bool(value)
print(f'Value: {value}, result:{result}')
'''
Value: 5, result:True
'''

# working with string is the same
value = ''
result = bool(value)
print(f'Value: {value}, result:{result}')
'''
Value: , result:False
'''

value = 'h'
result = bool(value)
print(f'Value: {value}, result:{result}')
'''
Value: h, result:True
'''

# collections list with booleans
value = []
result = bool(value)
print(f'Value: {value}, result:{result}')
'''
Value: [], result:False
'''

value = [1,2,3]
result = bool(value)
print(f'Value: {value}, result:{result}')
'''
Value: [1, 2, 3], result:True
'''

# dictionary
value = {}
result = bool(value)
print(f'Value: {value}, result:{result}')
'''
Value: {}, result:False
'''

value = {1,2,3}
result = bool(value)
print(f'Value: {value}, result:{result}')
'''
Value: {1, 2, 3}, result:True
'''

if bool(''): # is it an empty string? yes -> false | no ->true this conditions is like this boo('')
    print('return true')
else:
    print('return false')

if '': # is it an empty string? yes -> false | no ->true this conditions is like this boo('')
    print('return true')
else:
    print('return false')
'''
return false
return false
'''

if bool('r'): # is it an empty string? yes -> false | no ->true this conditions is like this boo('')
    print('return true')
else:
    print('return false')

if 'd': # is it an empty string? yes -> false | no ->true this conditions is like this boo('')
    print('return true')
else:
    print('return false')

'''
return true
return true
'''
value = '1'
while bool(value):  # while '': or while value:
    print(' while -> true')
    break # to work just one time
else:
    print(' while -> false')

'''
 while -> true
'''
