def cal(a,b, option='sum'):
    def sum(a,b):
        return a+b

    def rest(a,b):
        return a-b

    if option == 'sum':
        print(sum(a,b))
    elif option == 'rest':
        print(rest(a,b))


#cal(10,30)

"""
40
-20
"""

cal(10,30, option='rest')
"""
-20
"""