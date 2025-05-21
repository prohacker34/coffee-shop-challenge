from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("customer must be a Customer object")
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be a Coffee object")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("price must be a positive number")

        self.customer = customer
        self.coffee = coffee
        self._price = price

    @property
    def price(self):
        return self._price


coffee1 = Coffee("latte")
coffee2 = Coffee("espresso")
coffee3 = Coffee("latte")
coffee4 = Coffee("special")

customer1 = Customer("john")
customer2 = Customer("jane")
customer3 = Customer("leo")


order1 = Order(customer1, coffee1, 20)
order2 = Order(customer2, coffee2, 20)
order3 = Order(customer3, coffee1, 2)
order4 = Order(Customer("julian"), coffee4, 3)


customer1.add_order(order1)
customer2.add_order(order2)
customer3.add_order(order3)

coffee1.add_order(order1)
coffee1.add_order(order3)
coffee2.add_order(order2)
coffee4.add_order(order4)


if __name__ == "__main__":
    print("Coffee1 orders:", len(coffee1.orders()))
    print("Customer1 coffees:", [c.name for c in customer1.coffees()])
    print("Customer2 coffees:", [c.name for c in customer2.coffees()])
    print("Coffee1 customers:", [c.name for c in coffee1.customers()])
    print("coffee2 customers:", [c.name for c in coffee2.customers()])
    print("Coffee2 number of orders:", coffee2.num_orders())
    print("Coffee1 average price:", coffee1.average_price())