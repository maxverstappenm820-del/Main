opreator = input("enter the operator:(+ - * /) ")
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))

if opreator == "+":
    result = num1 + num2
    print("the result is: ", round(result, 2))
elif opreator == "-":
    result = num1 - num2
    print("the result is: ",round (result, 2))
elif opreator == "*":
    result = num1 * num2
    print("the result is: ",round(result, 2))
elif opreator == "/":
    if num2 != 0:
        result = num1 / num2
        print("the result is: ", round(result, 2))
    else:
        result = print("Error: Division by zero is not allowed.")

else:    print(f"{opreator} is not a valid operator. Please enter one of the following: +, -, *, /.")