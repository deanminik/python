from Product import Product
from Order import Order

product1 = Product('T-shirt', 100.00)
product2 = Product('jeans', 150.00)
product3 = Product('hat', 15.00)
product4 = Product('shoes', 15.00)

products1 = [product1, product2]
products2 = [product3, product4]

order1 = Order(products1)
order1.add_product(product4)
order1.add_product(product3)

print(order1)
print(f'Total of the order 1: {order1.calculate_total()}')
order2 = Order(products2)
print(order2)
print(f'Total of the order 1: {order2.calculate_total()}')