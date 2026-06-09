import json
import os
import sys
from datetime import datetime

class ATM:
    DATA_FILE = "atm_data.json"

    def __init__(self):
        self.load_data()
        self.current_user = None

    def load_data(self):
        """Load user data from a JSON file."""
        if os.path.exists(self.DATA_FILE):
            try:
                with open(self.DATA_FILE, 'r') as f:
                    self.users = json.load(f)
            except json.JSONDecodeError:
                self.users = self.get_default_users()
        else:
            self.users = self.get_default_users()
            self.save_data()

    def get_default_users(self):
        """Return a default set of users."""
        return {
            "123456": {"pin": "1234", "balance": 1000.0, "history": []},
            "654321": {"pin": "4321", "balance": 500.0, "history": []}
        }

    def save_data(self):
        """Save user data to a JSON file."""
        with open(self.DATA_FILE, 'w') as f:
            json.dump(self.users, f, indent=4)

    def log_transaction(self, account_num, description):
        """Add a transaction record with a timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.users[account_num]["history"].append(f"[{timestamp}] {description}")

    def authenticate(self):
        """Authenticate user by account number and PIN."""
        print("\n=== ATM Authentication ===")
        account_num = input("Enter Account Number: ").strip()
        if account_num not in self.users:
            print("Error: Account not found.")
            return False

        attempts = 3
        while attempts > 0:
            pin = input(f"Enter PIN ({attempts} attempts remaining): ").strip()
            if self.users[account_num]["pin"] == pin:
                self.current_user = account_num
                print(f"\nWelcome back, Account {account_num}!")
                return True
            else:
                attempts -= 1
                print("Error: Incorrect PIN.")
        
        print("Too many incorrect attempts. Access Denied.")
        return False

    def show_menu(self):
        print("\n" + "="*30)
        print("      ATM MAIN MENU")
        print("="*30)
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Transaction History")
        print("5. Change PIN")
        print("6. Logout & Exit")
        print("="*30)

    def check_balance(self):
        balance = self.users[self.current_user]["balance"]
        print(f"\nYour current balance is: ${balance:,.2f}")

    def withdraw_money(self):
        try:
            amount = float(input("\nEnter amount to withdraw: "))
            if amount <= 0:
                print("Error: Amount must be positive.")
                return
            
            balance = self.users[self.current_user]["balance"]
            if amount > balance:
                print("Error: Insufficient balance.")
            else:
                self.users[self.current_user]["balance"] -= amount
                self.log_transaction(self.current_user, f"Withdrew ${amount:,.2f}")
                self.save_data()
                print(f"Success! New balance: ${self.users[self.current_user]['balance']:,.2f}")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

    def deposit_money(self):
        try:
            amount = float(input("\nEnter amount to deposit: "))
            if amount <= 0:
                print("Error: Amount must be positive.")
                return
            
            self.users[self.current_user]["balance"] += amount
            self.log_transaction(self.current_user, f"Deposited ${amount:,.2f}")
            self.save_data()
            print(f"Success! New balance: ${self.users[self.current_user]['balance']:,.2f}")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

    def show_history(self):
        history = self.users[self.current_user]["history"]
        print("\n--- Transaction History ---")
        if not history:
            print("No transactions yet.")
        else:
            for record in history[-10:]: # Show last 10 transactions
                print(record)

    def change_pin(self):
        old_pin = input("Enter current PIN: ").strip()
        if old_pin != self.users[self.current_user]["pin"]:
            print("Error: Incorrect PIN.")
            return
        
        new_pin = input("Enter new 4-digit PIN: ").strip()
        if len(new_pin) == 4 and new_pin.isdigit():
            confirm_pin = input("Confirm new PIN: ").strip()
            if new_pin == confirm_pin:
                self.users[self.current_user]["pin"] = new_pin
                self.log_transaction(self.current_user, "PIN changed successfully")
                self.save_data()
                print("Success: PIN updated.")
            else:
                print("Error: PINs do not match.")
        else:
            print("Error: PIN must be 4 digits.")

    def run(self):
        if not self.authenticate():
            return

        while True:
            self.show_menu()
            choice = input("Select an option (1-6): ").strip()

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.withdraw_money()
            elif choice == '3':
                self.deposit_money()
            elif choice == '4':
                self.show_history()
            elif choice == '5':
                self.change_pin()
            elif choice == '6':
                print("\nThank you for using our ATM. Goodbye!")
                break
            else:
                print("Error: Invalid selection. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
