class Product: # Again this class is inheritance of object
    product_counter = 0 # variable class

    def __init__(self, name, price):
        Product.product_counter += 1
        self._id_product = Product.product_counter  #This symbol (_) before the word means, that the variable is private.
        self._name = name
        self._price = price

    @property
    def price(self):
        return self._price

    def __str__(self):
        return f'Id Product: {self._id_product}, Name:{self._name}, Price: {self._price}'
        #To don't spend more time, using get and set because the variables are private, we are forcing to
        # call it, but it is a bad practice

#This conditional means if (__name__ = class Product) has the same name of (__main__ = Product.py) to run this conditional
#So this part will be able only here in this class
if __name__ == '__main__':
    product1 = Product('T-shirt', 100.00)
    print(product1)
    product2 = Product('jeans', 150.00)
    print(product2)




