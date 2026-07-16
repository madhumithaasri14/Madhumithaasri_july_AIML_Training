# Part A — Spot the Bug

def add_item(item, cart=[]):
    cart.append(item)
    return cart


print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

# Output:
# ['apple']
# ['apple', 'banana']
# ['bread', 'milk']
# ['apple', 'banana', 'eggs']

# Explanation:
# The default list (cart=[]) is created only once
# Calls without a cart argument share the same list
# Passing cart=["bread"] creates a separate list

# Part B — Fix It

def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

# Part C — Build the Cart

def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })


def update_price(price_tuple, new_price):
    # Tuples are immutable, so changing an element raises TypeError.
    price_tuple[0] = new_price


def calculate_total(cart):
    total = 0
    for item in cart["items"]:
        total += item["price"] * item["qty"]
    total -= total * (cart["discount"] / 100)
    return total


cart1 = create_cart("Alice", 10)
add_to_cart(cart1, "Apple", 50, 2)
add_to_cart(cart1, "Milk", 30, 1)

cart2 = create_cart("Bob", 5)
add_to_cart(cart2, "Bread", 40, 2)

print(cart1)
print("Alice Total:", calculate_total(cart1))

print(cart2)
print("Bob Total:", calculate_total(cart2))

price = (100,)
try:
    update_price(price, 120)
except TypeError as e:
    print("Error:", e)
# Discussion Points

# 1. Why is discount=0 safe but cart=[] dangerous?
# discount=0 is safe because integers are immutable.
# cart=[] is dangerous because lists are mutable and shared between function calls.

# 2. What is the difference between rebinding and mutating?
# Rebinding creates a new object reference.
# Mutating changes the existing object's contents.

# 3. Which of these are mutable? — list, tuple, dict, set, str, int
# Mutable: list, dict, set
# Immutable: tuple, str, int

# 4. When you pass a list into a function and modify it, do changes reflect outside? Why?
# Yes. Lists are mutable, so modifying the list inside the function also changes the original list.
