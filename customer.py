class Customer:
    def __init__(self, name):
        self._name = name
        self._orders = []
        self._coffees = []

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set([order.coffee for order in self._orders]))

    def add_order(self, order):
        self._orders.append(order)
        if order.coffee not in self._coffees:
            self._coffees.append(order.coffee)

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self.add_order(order)
        coffee.add_order(order)
        return order

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be between 1-15 characters")
        self._name = value