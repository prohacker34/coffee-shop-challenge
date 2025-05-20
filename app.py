class Customer:
    def __init__(self,name):
        self._name=name
        self._orders=[]
        self._coffees=[]

    def orders(self):
        return self._orders

    def coffees(self):
        return [order.coffee for order in self._orders]

    def add_order(self,order):
        self._orders.append(order)

    def coffee(self):
        return self._coffees

    def loop_coffees(self):
        return [coffee.coff for coffee in self._coffees]
    def add_coffee(self,coffee):
        self._coffees.append(coffee)


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value <1 or value >15:
            raise TypeError("character must be between 1-15")
        self._name=value

class Coffee :
    def __init__(self,name):
        self._name=name
        self._orders=[]
        self._customers=[]

    def orders (self):
        return self._orders
    def customers(self):
        return [order.customer for order in self._orders]

    def add_order(self,order):
          self._orders.append(order)

    def customer (self):
        return self._customers
    def loop_customers(self):
        return[customer.custom for customer in self._coffees]
    def add_customer(self,customer):
          self._customers.append(customer)

    @property
    def name(self):
        return self._name





class Order:
    def __init__(self,customer,coffee,price):
        self.customer=customer
        self.coffee=coffee
        self._price=price



    @property
    def  price(self):
        return self._price




coffee1=Coffee("latte")
coffee2=Coffee("espresso")
coffee3=Coffee("latte")

customer1=Customer("john")
customer2=Customer("jane")
customer3=Customer("leo")


order1=Order("john","latte",20)
order2=Order("jane","espresso",20)
order3=Order("leo","latte",20)

customer1.add_order(order1.customer)
customer1.add_order(order1.coffee)
customer1.add_order(order1._price)
customer2.add_order(order2.customer)
customer2.add_order(order2.coffee)
customer2.add_order(order2._price)
customer3.add_order(order3.customer)
customer3.add_order(order3.coffee)
customer3.add_order(order3._price)

coffee1.add_order(order1.customer)
coffee1.add_order(order1.coffee)
coffee1.add_order(order1._price)
coffee2.add_order(order2.customer)
coffee2.add_order(order2.coffee)

coffee3.add_order(order3.customer)
coffee3.add_order(order3.coffee)
coffee3.add_order(order3._price)



customer1.add_coffee(coffee1._name)
customer2.add_coffee(coffee2._name)
customer3.add_coffee(coffee3._name)

coffee1.add_customer(customer1._name)



# print(coffee2.orders())

print(customer2.coffee())

print(coffee1.customer())

