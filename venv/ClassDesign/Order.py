from Product import Product
class Order:
    orders_counter = 0

    def __init__(self, products):
        Order.orders_counter += 1
        self._id_order = Order.orders_counter
        self._products = list(products)

    def add_product(self, product):
        self._products.append(product) # adding a new product to our list

    def calculate_total(self):
        total = 0
        for product in self._products:
            total += product.price #price is the property get from Product module, because it is private
        return total

    def __str__(self):
        products_str = ''
        for product in self._products:
            products_str += product.__str__() + '|'

        return f'Order: {self._id_order}, \nProducts: {products_str}'

if __name__ == '__main__':
    product1 = Product('T-shirt', 100.00)
    product2 = Product('jeans', 150.00)

    #creating a list of products
    products1 = [product1, product2]
    #creating the first order with the list of products
    order1 = Order(products1)
    print(order1)
    order2 = Order(products1)
    print(order2)