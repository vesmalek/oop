# Q1. Define a class called User with a class attribute
#     platform = "MyApp"
#     Create two instances and print the platform from both
#     Then print the type of one instance

class User:
    platform = "MyApp"

    def set_details(self, username, email, role):
        self.username = username.strip().lower()
        self.email = email.strip().lower()
        self.role = role.strip().lower()
    
    def display(self):
        print(f"{self.username} | {self.email} | {self.role}")

    def is_admin(self):
        return self.role == 'admin'


user1 = User()
user2 = User()
print()
print("Question 01:")
print(f"user1 platform: {user1.platform}")
print(f"user2 platform: {user2.platform}")
print(f"user1 type: {type(user1).__name__}")

# Q2. Add a method called set_details(self, username, email, role)
#     to the User class that sets those as instance attributes
#     Create two users with different details and call display()
#     which should print: "username | email | role"

user1.set_details('gakpo', 'gakpo@lfc.com', 'Winger')
user2.set_details('curtis', 'curtis@lfc.com', 'Admin')

print()
print("Question 02:")
user1.display()
user2.display()

# Q3. Add a method called is_admin(self) to User that returns
#     True if the role is "admin", False otherwise
#     Test it on both users from Q2

print()
print("Question 03:")
print(f"Is user1 an admin? {user1.is_admin()}")
print(f"Is user2 an admin? {user2.is_admin()}")

# Q4. Define a class called Order with:
#     - A class attribute status = "pending"
#     - A method set_details(self, product_name, quantity, price_per_unit)
#     - A method get_total(self) that returns quantity * price_per_unit
#     - A method summarize(self) that prints all details including total
#     Create two orders and call summarize() on both

class Order:
    status = "pending"

    def set_details(self, product_name, quantity, price_per_unit):
        self.product_name = product_name.strip().lower()
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def get_total(self):
        return self.quantity * self.price_per_unit
    
    def summarize(self):
        print(f"Product name: {self.product_name}, Quantity: {self.quantity}, Price Per unit: {self.price_per_unit}. The total is {self.get_total()}")

order1 = Order()
order1.set_details('tomato', 5, 1.25)
order2 = Order()
order2.set_details('oranges', 2, 6.75)

print()
print("Question 04:")
order1.summarize()
order2.summarize()

# Q5. Define a class called ShopCart with:
#     - A method set_customer(self, name) that sets the customer name
#     - A method add_item(self, product_name, price) that stores each
#       item as a dict and collects them in a list attribute called items
#     - A method get_total(self) that returns the sum of all item prices
#     - A method receipt(self) that prints the customer name, each item
#       with its price, and the total at the bottom
#
#     Create a cart, set a customer, add 3 items, then call receipt()

class ShopCart:
    items = []
    sum = 0
    def set_customer(self, name):
        self.customer_name = name
    
    def add_item(self, product_name, price):
        item = {'product': product_name, 'price' : price}
        self.items.append(item)

    def get_total(self):
        for item in self.items:
            self.sum += item['price']
        return self.sum
    
    def receipt(self):
        print(f"Customer: {self.customer_name}")
        for item in self.items:
            print(f"{item.get('product')} - ${item.get('price')}")
        total = self.get_total()
        print(f"Total: {total}")

print()
print("Question 05:")
cart = ShopCart()
cart.set_customer('Hashim')
cart.add_item('shirt', 19)
cart.add_item('shoes', 105)
cart.add_item('bag', 50)

cart.receipt()