#concession stand program

menu = {
    "pizza": 5.00,
    "hot dog": 2.50,
    "hamburger": 3.00,
    "nachos": 4.00,
    "soda": 1.50,
    "popcorn": 3.50,
    "lemonade": 2.00,
    "candy": 1.00,
}
total=0
cart=[]
print("Welcome to the concession stand!")
print("------Here is our menu:------")
for item, price in menu.items():
    print(f"{item.title():10}: ${price:.2f}")
print("-----------------------------")

while True:
    food=input("What would you like to order? (Type 'done' to finish): ").lower()
    if food == "done":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        print(f"{food.title()} added to your cart.")
    elif food == "":
        print("Please enter an item from the menu.")
    else:
        print("Sorry, we don't have that item. Please choose from the menu.")
print("-------your order-------")
for food  in cart:
    total += menu.get(food)
print(f"your cart: {', '.join(cart)}")
print()
print(f"Your total is: ${total:.2f}")
print("Thank you for your order!")


