 # Coffee Shop#
 This project has customers,coffees and orders.


## Key Features
- **Customer Management**: Track customer orders and favorite coffees
- **Coffee Analytics**: Calculate average price and order counts per coffee
- **Order System**: Link customers to coffees with price tracking
- **Data Validation**: Enforce business rules (e.g., valid prices, name lengths)
## project structure
coffee1/
│
├── coffee-shop-challenge
│ ├── customer.py # Customer class implementation
│ ├── coffee.py # Coffee class implementation
│ └── order.py # Order class implementation
│ └── debug.py
├── tests/ # Testing files
│ ├── test_models.py # Pytest unit tests
│
│
├── README.md # This file
└── requirements.txt # Dependencies

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:prohacker34/coffee-shop-challenge.git
   cd coffee-shop-challenge

## usage
# Initialization Example
coffee1 = Coffee("latte")      # Coffee instance
customer1 = Customer("john")   #customer instance
order1 = Order(customer1, coffee1, 20) #order instance

# Linking
 1. customers and orders
 customer1.add_order(order1)
 2. coffee and orders
 coffee1.add_order(order1)



# Check results
  1. find average
  print("Coffee1 average price:", coffee1.average_price())
  2. find total
  print("Coffee2 number of orders:", coffee2.num_orders())
  3. find customers coffee
  print("Customer1 coffees:", [c.name for c in customer1.coffees()])
  4. find coffee for each customer
  print("Coffee1 customers:", [c.name for c in coffee1.customers()])

