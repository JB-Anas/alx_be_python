# main-0.py
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
