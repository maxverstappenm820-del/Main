#python weight conversion program
weight = float(input("Enter the weight: "))
unit = input("Enter the unit (kg, g, lb, oz): ").lower()

if unit == "kg":
    weight_in_grams = weight * 1000
    weight_in_pounds = weight * 2.20462
    weight_in_ounces = weight * 35.274
    print(f"{weight} kg is equal to {weight_in_grams} g, {weight_in_pounds} lb, and {weight_in_ounces} oz.")
elif unit == "g":
    weight_in_kilograms = weight / 1000
    weight_in_pounds = weight * 0.00220462
    weight_in_ounces = weight * 0.035274
    print(f"{weight} g is equal to {weight_in_kilograms} kg, {weight_in_pounds} lb, and {weight_in_ounces} oz.")
elif unit == "lb":
    weight_in_kilograms = weight / 2.20462
    weight_in_grams = weight * 453.592
    weight_in_ounces = weight * 16
    print(f"{weight} lb is equal to {weight_in_kilograms} kg, {weight_in_grams} g, and {weight_in_ounces} oz.")
elif unit == "oz":
    weight_in_kilograms = weight / 35.274
    weight_in_grams = weight * 28.3495
    weight_in_pounds = weight / 16
    print(f"{weight} oz is equal to {weight_in_kilograms} kg, {weight_in_grams} g, and {weight_in_pounds} lb.")
else:
    print(f"{unit} is not a valid unit. Please enter one of the following: kg, g, lb, oz.")