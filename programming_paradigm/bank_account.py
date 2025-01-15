# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize account balance (default to 0 if not provided)
        self.account_balance = initial_balance

    def deposit(self, amount):
        # Deposit the specified amount to the account balance
        self.account_balance += amount

    def withdraw(self, amount):
        # Withdraw the specified amount if sufficient funds are available
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # Display the current account balance in a user-friendly format
        print(f"Current Balance: ${self.account_balance:.2f}")


import sys
from bank_account import BankAccount

def main():
    # Create a BankAccount instance with an initial balance of 100
    account = BankAccount(100)  # Example starting balance
    
    if len(sys.argv) < 2:
        # Provide usage instructions if not enough arguments are provided
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and amount
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        # Call the deposit method and print confirmation
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        # Call the withdraw method and check if withdrawal is successful
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        # Display the current balance
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
