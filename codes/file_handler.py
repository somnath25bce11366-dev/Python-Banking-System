import os

# Path to the data file
DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/users.txt')

def load_data():
    """Reads users.txt and returns a dictionary of users."""
    users = {}
    if not os.path.exists(DATA_FILE):
        return users  # Return empty if file doesn't exist yet

    with open(DATA_FILE, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 3:
                acc_num, pin, balance = parts
                users[acc_num] = {
                    'pin': pin,
                    'balance': float(balance)
                }
    return users

def save_user(acc_num, pin, balance):
    """Appends a new user to the text file."""
    # First, load existing to make sure we don't overwrite (simple approach)
    with open(DATA_FILE, 'a') as f:
        f.write(f"{acc_num},{pin},{balance}\n")

def update_balance(acc_num, new_balance):
    """Updates the balance of a specific user."""
    users = load_data()
    users[acc_num]['balance'] = new_balance
    
    # Rewrite the whole file with updated data
    with open(DATA_FILE, 'w') as f:
        for acc, data in users.items():
            f.write(f"{acc},{data['pin']},{data['balance']}\n")