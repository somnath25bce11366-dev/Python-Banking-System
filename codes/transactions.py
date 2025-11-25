from file_handler import load_data, update_balance

def check_balance(acc_num):
    """Prints the current balance."""
    users = load_data()
    balance = users[acc_num]['balance']
    print(f"\nYour Current Balance is: ${balance:.2f}")

def deposit(acc_num):
    """Adds money to the account."""
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Amount must be positive.")
            return

        users = load_data()
        new_balance = users[acc_num]['balance'] + amount
        update_balance(acc_num, new_balance)
        print(f"Success! New Balance: ${new_balance:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter a number.")

def withdraw(acc_num):
    """Deducts money if funds are sufficient."""
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be positive.")
            return

        users = load_data()
        current_balance = users[acc_num]['balance']

        if amount > current_balance:
            print("Insufficient Funds!")
        else:
            new_balance = current_balance - amount
            update_balance(acc_num, new_balance)
            print(f"Withdrawal Successful! Remaining Balance: ${new_balance:.2f}")

    except ValueError:
        print("Invalid input. Please enter a number.")