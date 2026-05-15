# Q1. Define a class called User with a class attribute
#     platform = "MyApp"
#     Create two instances and print the platform from both
#     Then print the type of one instance

# Q2. Add a method called set_details(self, username, email, role)
#     to the User class that sets those as instance attributes
#     Create two users with different details and call display()
#     which should print: "username | email | role"

# Q3. Add a method called is_admin(self) to User that returns
#     True if the role is "admin", False otherwise
#     Test it on both users from Q2

# Q4. Define a class called Order with:
#     - A class attribute status = "pending"
#     - A method set_details(self, product_name, quantity, price_per_unit)
#     - A method get_total(self) that returns quantity * price_per_unit
#     - A method summarize(self) that prints all details including total
#     Create two orders and call summarize() on both

# Q5. Define a class called ShopCart with:
#     - A method set_customer(self, name) that sets the customer name
#     - A method add_item(self, product_name, price) that stores each
#       item as a dict and collects them in a list attribute called items
#     - A method get_total(self) that returns the sum of all item prices
#     - A method receipt(self) that prints the customer name, each item
#       with its price, and the total at the bottom
#
#     Create a cart, set a customer, add 3 items, then call receipt()