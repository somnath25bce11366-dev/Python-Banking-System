import auth
import transactions

def main_menu(acc_num):
    """The menu users see AFTER logging in."""
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Logout")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            transactions.check_balance(acc_num)
        elif choice == '2':
            transactions.deposit(acc_num)
        elif choice == '3':
            transactions.withdraw(acc_num)
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid option. Try again.")

def start_app():
    """The starting screen of the application."""
    print("Welcome to the Python Banking System")
    
    while True:
        print("\n1. Login")
        print("2. Create New Account")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            acc_num = auth.login()
            if acc_num:
                main_menu(acc_num)
        elif choice == '2':
            auth.signup()
        elif choice == '3':
            print("Thank you for using our bank. Goodbye!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    start_app()