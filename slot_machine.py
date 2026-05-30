# python slot machine program

import random

print("Welcome to the Slot Machine!")

def spin_row():
    symbols = ['🍋', '🍒', '🍉', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(' | '.join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        symbol = row[0]
        if symbol == '🍋':
            return bet * 2
        elif symbol == '🍒':
            return bet * 3
        elif symbol == '🍉':
            return bet * 4
        elif symbol == '🔔':
            return bet * 5
        elif symbol == '⭐':
            return bet * 10
    return 0

def main():
    balance=100

    print("Welcome to the Slot Machine!")
    print("Symbols🍋, 🍒, 🍉, 🔔, ⭐")

    while balance > 0:
        print(f"Current Balance: ${balance}")
        input("Press Enter to spin...")
        bet = input("Enter your bet amount: ")
        if not bet.isdigit():
            print("Invalid input. Please enter a numeric value.")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient balance. Please enter a valid bet.")
            continue
        if bet <= 0:
            print("Bet must be greater than zero.")
            continue
        balance -= bet

        row = spin_row()

        print("Spinning...")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"Congratulations! You won ${payout}!")
            balance += payout
        else:
            print("Sorry, you lost. Try again!")
            balance -= bet
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing! Goodbye!")
            break
        print("\n")
    print("Game Over!")
    print(f"Final Balance: ${balance}")

if __name__ == "__main__":
    main()