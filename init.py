# Q1. Rewrite the User class from the Classes tutorial using __init__
#     It should accept username, email, and role (default "viewer")
#     Add a display() method that prints all three
#     Create two users — one with role, one without — and call display()

# Q2. Define a class called Product with __init__ accepting:
#     name, price, and category (default "General")
#     Inside __init__ also set in_stock = True automatically (not a parameter)
#     Add a method restock(self) that sets in_stock to True and prints a message
#     Add a method sell_out(self) that sets in_stock to False and prints a message
#     Test both methods on one product

# Q3. Define a class called Order with __init__ accepting:
#     product_name, quantity, price_per_unit
#     Compute and store total inside __init__ (not passed in)
#     Also set status = "pending" automatically
#     Add a method confirm(self) that changes status to "confirmed"
#     Add a method display(self) that prints all details including total and status
#     Create an order, display it, confirm it, display it again

# Q4. Define a class called BankAccount with __init__ accepting:
#     owner and an opening balance (default 0)
#     Add a method deposit(self, amount) that adds to balance and prints new balance
#     Add a method withdraw(self, amount) that:
#       - deducts from balance if funds are sufficient
#       - prints "Insufficient funds" if not
#     Add a method get_balance(self) that returns the current balance
#     Test it with deposits and withdrawals including one that should fail

# Q5. Define a class called ShopCart using __init__:
#     Accept customer_name in __init__
#     Initialize an empty items list in __init__ (not a parameter)
#     Add method add_item(self, product_name, price)
#       that appends a dict to items
#     Add method get_total(self) that returns sum of all item prices
#     Add method receipt(self) that prints customer name,
#       each item with price, and total
#     Create a cart, add 3 items, print the receipt