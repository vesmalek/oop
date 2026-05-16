# Q1. Add __str__ and __repr__ to this class:
#     __str__ should return: "Shirt — $29.99"
#     __repr__ should return: "Product(name='Shirt', price=29.99, category='Clothing')"
#
#     class Product:
#         def __init__(self, name, price, category):
#             self.name = name
#             self.price = price
#             self.category = category

# Q2. Add __str__ and __len__ to this ShopCart class:
#     __str__ should return: "ismail's cart — 3 item(s)"
#     __len__ should return the number of items in the cart
#
#     class ShopCart:
#         def __init__(self, customer):
#             self.customer = customer
#             self.items = []
#
#         def add_item(self, name, price):
#             self.items.append({"name": name, "price": price})

# Q3. Add __str__ and __repr__ to the User class:
#     __str__: "ismail (admin)" 
#     __repr__: "User(username='ismail', email='ismail@mail.com', role='admin')"
#     Then create a list of 3 users and print the list — observe which method is used

# Q4. This question connects to Django:
#     Define a class called BlogPost that mimics a Django model
#     __init__ accepts: title, author, status (default "draft")
#     __str__ returns the title — because in Django admin you want to see the title
#     __repr__ returns full details for debugging
#     Add a method publish(self) that changes status to "published"
#     Create two posts, print them, publish one, print again

# Q5. Combine inheritance with dunder methods:
#     Parent class: Vehicle
#       __init__: make, model, year
#       __str__: "{year} {make} {model}"
#       __repr__: "Vehicle(make='{make}', model='{model}', year={year})"
#
#     Child class: Car(Vehicle)
#       __init__: make, model, year, num_doors=4
#       Use super().__init__() for the Vehicle part
#       Override __str__ to return: "{year} {make} {model} ({num_doors} doors)"
#       Add method: honk(self) → "Beep beep!"
#
#     Create a Vehicle and a Car, print both, call repr() on both
#     Show that Car's __str__ overrides Vehicle's