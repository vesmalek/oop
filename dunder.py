# Q1. Add __str__ and __repr__ to this class:
#     __str__ should return: "Shirt — $29.99"
#     __repr__ should return: "Product(name='Shirt', price=29.99, category='Clothing')"
#
#     class Product:
#         def __init__(self, name, price, category):
#             self.name = name
#             self.price = price
#             self.category = category

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} — ${self.price}"
    
    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, category='{self.category}')"

print()
print("Question 01:")    
my_product = Product('onions', 8.75, 'Grocery')
print(my_product)
print(repr(my_product))

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

class ShopCart:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"{self.customer}'s cart — {len(self.items)} item(s)"
    
print()
print("Question 02:")
my_cart = ShopCart('Ajmala')
my_cart.add_item('coconut', 2)
my_cart.add_item('apples', 5)
my_cart.add_item('spinach', 0.5)
my_cart.add_item('milk', 3)

print(my_cart)

# Q3. Add __str__ and __repr__ to the User class:
#     __str__: "ismail (admin)" 
#     __repr__: "User(username='ismail', email='ismail@mail.com', role='admin')"
#     Then create a list of 3 users and print the list — observe which method is used

class User:
    def __init__(self, username, email, role="viewer"):
        self.username = username
        self.email = email
        self.role = role
    
    def __str__(self):
        return f"{self.username} ({self.role})"
    
    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}', role='{self.role}')"
    
user1 = User('kali', 'kali@linux.com', 'developer')
user2 = User('superuser', 'superuser@linux.com')
user3 = User('admin', 'admin@linux.com', 'admin')

print()
print("Question 03:")
print(user1)
print(user2)
print(user3)

users = [user1, user2, user3]

print(users)

# Q4. This question connects to Django:
#     Define a class called BlogPost that mimics a Django model
#     __init__ accepts: title, author, status (default "draft")
#     __str__ returns the title — because in Django admin you want to see the title
#     __repr__ returns full details for debugging
#     Add a method publish(self) that changes status to "published"
#     Create two posts, print them, publish one, print again

class BlogPost:
    def __init__(self, title, author, status="draft"):
        self.title = title
        self.author = author
        self.status = status

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f"BlogPost(title='{self.title}', author='{self.author}', status='{self.status}')"
    
    def publish(self):
        self.status = "published"

post1 = BlogPost('How to make pancakes', 'Izzy')
post2 = BlogPost('Python tutorial for beginners', 'Imran')
print()
print("Question 04:")
print(post1)
print(repr(post1))
print(post2)
print(repr(post2))
post2.publish()
print(post2)
print(repr(post2))

# Q5. Combine inheritance with dunder methods:
#     Parent class: Vehicle
#       __init__: make, model, year
#       __str__: "{year} {make} {model}"
#       __repr__: "Vehicle(make='{make}', model='{model}', year={year})"

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    def __repr__(self):
        return f"Vehicle(make='{self.make}', model='{self.model}', year={self.year})"

#     Child class: Car(Vehicle)
#       __init__: make, model, year, num_doors=4
#       Use super().__init__() for the Vehicle part
#       Override __str__ to return: "{year} {make} {model} ({num_doors} doors)"
#       Add method: honk(self) → "Beep beep!"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors=4):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    
    def __str__(self):
        return super().__str__() + f" ({self.num_doors} doors)"
    
    def honk(self):
        print("Beep beep!")

#     Create a Vehicle and a Car, print both, call repr() on both

my_vehicle = Vehicle('Toyota', 'Rav4', 2006)
my_car = Car('Subaru', 'Forester', 2010)

print()
print("Question 05:")
print(my_vehicle)
print(my_car)
print(repr(my_vehicle))
print(repr(my_car))
#     Show that Car's __str__ overrides Vehicle's