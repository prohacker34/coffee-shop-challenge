class Coffee:
    def __init__(self, name):
        self._name = name
        self._orders = []
        self._customers = []

    def orders(self):
        return self._orders

    def customers(self):
        return list(set([order.customer for order in self._orders]))

    def add_order(self, order):
        self._orders.append(order)
        if order.customer not in self._customers:
            self._customers.append(order.customer)

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value