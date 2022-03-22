"""
It is a boolean condition, if there is a false situation or error in this case,
it displays an Assertion error
This does not replace the try and catch, this is more to stop the program or avoid them during an execution
these errors are unrecoverable
"""

# Example 1
## check if the division is between zero
def division(a,b):
    # we ensure that b is not a zero value to continue
    assert b != 0, 'Division between zero' # false show this 'Division between zero'
    # true print this
    print(f'Result of the division a and b :{a/b}')


# example 2
## calculation get the average of a list
def get_average(ratings):
    assert len(ratings) != 0, 'This list is empty'
    print(f'f The average is: {sum(ratings)/len(ratings)}')

# example 3
## simulation shopping cart. Detect if the discount is less that the available
def apply_discount(products, discount):
    price_with_discount = products['price'] * (1.0 - discount)
    print(f'New price of the product : {price_with_discount}')

    """
    if price is greater or equal than the price with discount 
    or if price with discount greater or equal that price 
    """
    assert 0<=price_with_discount <= products ['price'], f'Invalid discount {price_with_discount}'
    ## so practically price_with_discount should be in a range of 0 to price, it will be valid
    print('Valid discount')


if __name__ == '__main__':
    # test of out division
   # division(10,2)
    """
    Result of the division a and b :5.0
    """

    #division(10, 0)
    """
    Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/tips and tricks Logic/1_assertions.py", line 21, in <module>
    division(10, 0)
  File "/home/lite/PycharmProject/LabGeometric/venv/tips and tricks Logic/1_assertions.py", line 12, in division
    assert b != 0, 'Division between zero'
AssertionError: Division between zero
    """

#--_________________________________________________________________________________________________

# example 2 test
    #ratings = [10,8,6]
    #get_average(ratings)
    """
    f The average is: 8.0
    """
    #ratingsEmpty = []
    #get_average(ratingsEmpty)
    """
    Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/tips and tricks Logic/1_assertions.py", line 50, in <module>
    get_average(ratingsEmpty)
  File "/home/lite/PycharmProject/LabGeometric/venv/tips and tricks Logic/1_assertions.py", line 20, in get_average
    assert len(ratings) != 0, 'This list is empty'
AssertionError: This list is empty
    """

#--_________________________________________________________________________________________________

# example 2 test
    products = {'name': 'tshirt', 'price': 1500}
    #apply_discount(products, 0.10)
    """
    New price of the product : 1350.0
    Valid discount
    """
    ## but if we add more than 1.0 or more than 100% it is the same
    apply_discount(products, 1.2)
    """
    Traceback (most recent call last):
  File "/home/lite/PycharmProject/LabGeometric/venv/tips and tricks Logic/1_assertions.py", line 84, in <module>
    apply_discount(products, 1.2)
  File "/home/lite/PycharmProject/LabGeometric/venv/tips and tricks Logic/1_assertions.py", line 33, in apply_discount
    assert 0<=price_with_discount <= products ['price'], f'Invalid discount {price_with_discount}'
AssertionError: Invalid discount -299.99999999999994
    """

