#shopping cart program
print("Welcome to the shopping cart program!")
cart = []
prices = []
total=0

while True:
    item = input("Enter the item name (or 'done' to finish): ").lower()
    if item.lower() == 'done':
        break
    if item == "":
        print("Item name cannot be empty. Please try again.")
        continue
    if item in cart:
        print(f"{item} is already in the cart. Please enter a different item.")
        continue
    
    price = input(f"Enter the price of {item}:$ ")
    if price == "":
        print("Price cannot be empty. Please try again.")

        continue
    price = float(price)
    if price < 0:
        print("Price cannot be negative. Please try again.")
        continue
    
    if not isinstance(price, (int, float)):
        print("Price must be a number. Please try again.")
        continue

    cart.append(item)
    prices.append(price)
total += price
print("------Your Cart------")

for  item in cart:
    print(item, end=", ")

print()

total = sum(prices)

print(f"Total price: ${total:.2f}$")
