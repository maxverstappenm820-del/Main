# python Banking program

def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")


def deposit():

    amount = input("Enter the amount to deposit: ")
    while True:
        try:
            amount = float(amount)
            if amount <= 0:
                print("Please enter a positive amount.")
                amount = input("Enter the amount to deposit: ")
                return 0 
                continue
            else:
                return amount
            
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            amount = input("Enter the amount to deposit: ")
    global balance
    balance += amount


def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        return 0
        print("Insufficient funds.")
    elif amount <= 0:
        print("Please enter a positive amount.")
        return 0
    else:
        balance -= amount

def main():
    balance = 0
is_running = True

while is_running:
    print("----------Welcome to the Banking Program!---------")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance(balance)
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw(balance)
    elif choice == "4":
        is_running = False
        print("Thank you for using the Banking Program. Goodbye!")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
print("-------------------------------------------------")

if __name__ == "__main__":
    main()
