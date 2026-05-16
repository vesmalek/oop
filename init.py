# Q1. Rewrite the User class from the Classes tutorial using __init__
#     It should accept username, email, and role (default "viewer")
#     Add a display() method that prints all three
#     Create two users — one with role, one without — and call display()

class User:
    def __init__(self, username, email, role="viewer"):
        self.username = username.strip().lower()
        self.email = email.strip().lower()
        self.role = role.strip().lower()
        self.platform = "MyApp"        
    
    def display(self):
        print(f"{self.username} | {self.email} | {self.role}")

    def is_admin(self):
        return self.role == 'admin'

user1 = User('izzy', 'izzy@studios.com')
user2 = User('azraq', 'azraq@studios.com', 'architect')

print()
print("Question 01:")
user1.display()
user2.display()

# Q2. Define a class called Product with __init__ accepting:
#     name, price, and category (default "General")
#     Inside __init__ also set in_stock = True automatically (not a parameter)
#     Add a method restock(self) that sets in_stock to True and prints a message
#     Add a method sell_out(self) that sets in_stock to False and prints a message
#     Test both methods on one product

class Product:
    def __init__(self, name, price, category="General"):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = True

    def restock(self):
        self.in_stock = True
        print(f"{self.name} is now in stock!")

    def sell_out(self):
        self.in_stock = False
        print(f"Sorry, {self.name} is now out of stock :)")

print()
print("Question 02:")
product1 = Product('avocadoes', 5.99, 'Grocery')
product1.restock()
product1.sell_out()

# Q3. Define a class called Order with __init__ accepting:
#     product_name, quantity, price_per_unit
#     Compute and store total inside __init__ (not passed in)
#     Also set status = "pending" automatically
#     Add a method confirm(self) that changes status to "confirmed"
#     Add a method display(self) that prints all details including total and status
#     Create an order, display it, confirm it, display it again

class Order:
    def __init__(self, product_name, quantity, price_per_unit):
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.total = quantity * price_per_unit
        self.status = "pending ⏳"

    def confirm(self):
        self.status = "confirmed ✅"

    def display(self):
        print('-' * 25)
        print("Order Summary:")
        print('-' * 25)
        print(f"Order Status: {self.status}")
        print(f"Product: {self.product_name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price Per Unit: {self.price_per_unit}")
        print('-' * 12)
        print(f"TOTAL: {self.total}")
        print('-' * 12)
        
print()
print("Question 03:")
my_order = Order('Books', 3, 12.5)
my_order.display()

print()
my_order.confirm()
my_order.display()

# Q4. Define a class called BankAccount with __init__ accepting:
#     owner and an opening balance (default 0)
#     Add a method deposit(self, amount) that adds to balance and prints new balance
#     Add a method withdraw(self, amount) that:
#       - deducts from balance if funds are sufficient
#       - prints "Insufficient funds" if not
#     Add a method get_balance(self) that returns the current balance
#     Test it with deposits and withdrawals including one that should fail

class BankAccount:
    def __init__(self, owner, opening_balance=0):
        self.owner = owner
        self.balance = opening_balance
        print(f"Account opened successfully. Account: {self.owner} - Balance: ${self.balance:,}")

    def deposit(self, amount):
        self.balance += amount
        print(f"You have successfully deposited ${amount:,}. Current balance is ${self.balance:,}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance
    
print()
print("Question 04:")
my_account = BankAccount('Ally', 13500)
my_account.deposit(2500)
my_account.withdraw(6500)
print(f"Account: {my_account.owner} - Balance: ${my_account.get_balance():,}")
my_account.withdraw(15000)
print(f"Account: {my_account.owner} - Balance: ${my_account.get_balance():,}")

# Q5. Define a class called ShopCart using __init__:
#     Accept customer_name in __init__
#     Initialize an empty items list in __init__ (not a parameter)
#     Add method add_item(self, product_name, price)
#       that appends a dict to items
#     Add method get_total(self) that returns sum of all item prices
#     Add method receipt(self) that prints customer name,
#       each item with price, and total
#     Create a cart, add 3 items, print the receipt

class ShopCart:
    def __init__(self):
        self.items = []

    def add_item(self, product_name, price):
        item = {'product': product_name, 'price': price}
        self.items.append(item)

    def get_total(self):
        return sum(item['price'] for item in self.items)
    
    def receipt(self):
        print('-' * 25)
        print("Receipt")
        print('-' * 25)
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item['product']} - ${item['price']:,}")
        print('-' * 25)
        print(f"TOTAL: ${self.get_total():,}")

my_cart = ShopCart()
my_cart.add_item('Pillow', 10.99)
my_cart.add_item('Rug', 40)
my_cart.add_item('Headphones', 1350)

print()
print("Question 05:")
my_cart.receipt()