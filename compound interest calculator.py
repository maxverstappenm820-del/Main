#python compound interest calculator

prinsiple = 0
rate = 0
time = 0

while prinsiple <= 0:
    prinsiple = float(input("Enter the prinsiple amount: "))
    if prinsiple <= 0:
        print("Prinsiple amount must be greater than 0. Please try again.")

while rate <= 0:
    rate = float(input("Enter the interest rate (in percentage): "))
    if rate <= 0:
        print("Interest rate must be greater than 0. Please try again.")

while time <= 0:
    time = float(input("Enter the time period (in years): "))
    if time <= 0:
        print("Time period must be greater than 0. Please try again.")

# Calculate compound interest
total_amount = prinsiple * pow((1 + rate / 100), time)

print(f"Balance after {time} years is: ${total_amount:.2f}")
