# Shopping Cart Analyzer

# List of items in cart
cart_items = ["Laptop", "Mouse", "Keyboard", "Mouse"]

# Tuple of products with prices
products = (
    ("Laptop", 50000),
    ("Mouse", 500),
    ("Keyboard", 1500),
    ("Monitor", 12000)
)

total = 0
prices_list = []

# Calculate total and store prices
for item in cart_items:
    for product in products:
        if item == product[0]:
            total += product[1]
            prices_list.append(product[1])

# Finding max and min priced items
max_price = max(prices_list)
min_price = min(prices_list)

# Finding corresponding item names
max_item = ""
min_item = ""

for product in products:
    if product[1] == max_price:
        max_item = product[0]
    if product[1] == min_price:
        min_item = product[0]

# Output
print("Cart Items:", cart_items)
print("Total Bill:", total)
print("Most Expensive Item:", max_item, "-", max_price)
print("Cheapest Item:", min_item, "-", min_price)
