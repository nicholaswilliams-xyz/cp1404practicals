"""
Shop calculator:

Display total price of n items. Discount if total price > minimum price for discount
"""

num_of_items = int(input("Total number of items: "))
discount = float(0.1)
total_price = 0

while num_of_items < 0:
    print("Invalid number of items")
    num_of_items = int(input("Total number of items: "))

for i in range(1, num_of_items+1):
    item_price = int(input(f"Price of item {i}: $"))
    total_price += item_price

if total_price > 100:
    discounted_total_price = total_price - total_price * discount
    print(f"Total price for {i} items is ${discounted_total_price}")

else:
    print(f"Total price for {i} items is ${total_price}")
