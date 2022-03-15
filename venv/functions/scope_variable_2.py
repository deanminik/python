# more of scope variables
def function_extern():
    variable_local_extern = 'Global variable extern'

    def function_nest():
        variable_local_nets = 'Local variable nested'
        nonlocal variable_local_extern
        variable_local_extern = 'new value local extern'

    function_nest()

    print(f'Local value extern {variable_local_extern}')


function_extern()
"""
Local value extern new value local extern
"""
