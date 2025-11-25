import random
from file_handler import load_data, save_user

def login():
    """Asks for credentials and returns Account Number if valid."""
    users = load_data()
    
    print("\n--- LOGIN ---")
    acc_num = input("Enter Account Number: ")
    pin = input("Enter 4-digit PIN: ")

    if acc_num in users and users[acc_num]['pin'] == pin:
        print("Login Successful!")
        return acc_num
    else:
        print("Invalid Account Number or PIN.")
        return None

def signup():
    """Creates a new account."""
    users = load_data()
    
    print("\n--- SIGNUP ---")
    name = input("Enter your Name: ") # Just for display
    pin = input("Create a 4-digit PIN: ")
    
    # Generate a random 5-digit account number
    while True:
        acc_num = str(random.randint(10000, 99999))
        if acc_num not in users:
            break
            
    # Save new user with 0.0 balance
    save_user(acc_num, pin, 0.0)
    
    print(f"Account Created Successfully!")
    print(f"Your Account Number is: {acc_num}")
    print("PLEASE REMEMBER THIS NUMBER!")