# scope of variables -> alcance

var_global = 'Global variable'
var_global_original = 'Global variable start'
def printThis():
    global var_global_original # this is to modify

    print(f'Global variable from the function { var_global}')
    var_local = 'Local variable'
    print(f'Global variable from the function {var_local} ')

    #modify a global variable
   # print(f'Global variable original {var_global_original}')
    var_global_original = 'Global variable start ends'
    print(f'Global variable original finish {var_global_original}')
printThis()
"""
Global variable from the function Global variable
Global variable from the function Local variable 
Global variable original finish Global variable start ends
Global variable out of the function Global variable
"""

print(f'Global variable out of the function {var_global}')
"""
Global variable out of the function Global variable
"""

# print(f'Local variable in of the function {var_local}')
"""
Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/functions/scope_of_a_variable.py", line 21, in <module>
    print(f'Local variable in of the function {var_local}')
NameError: name 'var_local' is not defined

"""