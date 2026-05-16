# Q1. Define a parent class called Animal with:
#     __init__ accepting name and sound
#     A method speak(self) that returns "{name} says {sound}"
#
#     Create two child classes: Dog and Cat
#     Each should use super().__init__() passing the right sound automatically
#     (Dog always says "Woof", Cat always says "Meow")
#     So creating a Dog only needs a name: Dog("Rex")
#     Test speak() on both

# Q2. Using the User parent class below, create two child classes:
#     AdminUser — role defaults to "admin", adds a method:
#       manage_users(self) → returns "{username} is managing users."
#     CustomerUser — role defaults to "customer", adds a method:
#       place_order(self, product) → returns "{username} ordered {product}."
#     Both should use super().__init__() correctly
#     Test all methods including the inherited login() on both
#
#     class User:
#         def __init__(self, username, email, role="viewer"):
#             self.username = username
#             self.email = email
#             self.role = role
#             self.is_active = True
#
#         def login(self):
#             return f"{self.username} logged in."

# Q3. Override a method:
#     Using your AdminUser from Q2, override login() so it returns:
#     "{username} logged in with ADMIN privileges."
#     Regular User login stays unchanged
#     Test login() on both a User and AdminUser to show the difference

# Q4. Use super() in an overridden method:
#     Add a login() to CustomerUser that calls super().login()
#     and appends " Welcome to the shop!" to the result
#     Expected: "ali logged in. Welcome to the shop!"

# Q5. Build a small product system using inheritance:
#     Parent class: Product
#       __init__: name, price, category="General"
#       method: display(self) — prints name, price, category
#       method: apply_discount(self, percent) — returns discounted price
#
#     Child class: DigitalProduct(Product)
#       __init__: name, price, file_format (e.g "PDF", "MP4")
#       category should automatically be set to "Digital" via super()
#       Add method: download(self) → "{name} is downloading as {file_format}"
#       Override display() to also print file_format after calling super().display()
#
#     Child class: PhysicalProduct(Product)
#       __init__: name, price, weight_kg
#       category should automatically be set to "Physical" via super()
#       Add method: ship(self) → "Shipping {name} — {weight_kg}kg"
#       Override display() to also print weight after calling super().display()
#
#     Create one of each, call display(), apply_discount(), and their unique methods