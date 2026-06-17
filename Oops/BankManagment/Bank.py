import json
import random
import string
import os
from pathlib import Path


class Bank:
    # Resolves absolute path to guarantee data drops in the exact same directory as the script
    current_dir = Path(__file__).parent.resolve()
    database = current_dir / 'data.json'
    data = []

    @classmethod
    def load_database(cls):
        try:
            if cls.database.exists() and cls.database.stat().st_size > 0:
                with open(cls.database, 'r') as fs:
                    cls.data = json.load(fs)
            else:
                cls.data = []
                with open(cls.database, 'w') as fs:
                    json.dump(cls.data, fs)
        except Exception as err:
            print(f"Error loading database: {err}")
            cls.data = []

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)
            fs.flush()
            os.fsync(fs.fileno())  # Forces system to write cache directly to disk storage

    @classmethod
    def __accountGenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id_list = alpha + num + spchar
        random.shuffle(id_list)
        return "".join(id_list)

    @classmethod
    def __is_email_taken(cls, email):
        return any(user['email'].lower() == email.lower() for user in cls.data)

    def createAccount(self):
        print("\n--- Create Account ---")
        name = input("Enter your name: ").strip()
        
        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("Invalid input! Age must be a numerical value.")
            return

        email = input("Enter your email: ").strip()
        
        # Validation: Email must contain '@'
        if "@" not in email:
            print("Error: Invalid email format! The '@' symbol is required.")
            return
            
        if Bank.__is_email_taken(email):
            print("Error: An account with this email is already registered!")
            return

        pin_input = input("Enter your 4-digit PIN: ").strip()
        # PIN layout safety check
        if not (pin_input.isdigit() and len(pin_input) == 4):
            print("Error: PIN must be exactly 4 digits.")
            return
        pin = int(pin_input)

        if age < 18:
            print("Sorry, you must be 18 or older to open an account.")
            return

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": Bank.__accountGenerate(),
            "balance": 0
        }

        Bank.data.append(info)
        Bank.__update()
        
        print("\nAccount created successfully!")
        for key, value in info.items():
            print(f"{key.capitalize()} : {value}")
        print("\nPlease note down your account number for future access.")

    def _find_user(self):
        """Helper method to find matching user and minimize code repetition"""
        accnumber = input("Please enter your account number: ").strip()
        try:
            pin = int(input("Please enter your PIN: "))
        except ValueError:
            print("Invalid PIN format.")
            return None
        
        for user in Bank.data:
            if user['accountNo'] == accnumber and user['pin'] == pin:
                return user
        print("Error: Account not found or incorrect PIN.")
        return None

    def depositMoney(self):
        print("\n--- Deposit Money ---")
        user = self._find_user()
        if not user:
            return

        try:
            amount = int(input("Enter the amount to deposit: "))
        except ValueError:
            print("Invalid amount value.")
            return

        if amount <= 0 or amount > 10000:
            print("Error: You can only deposit an amount between 1 and 10,000.")
        else:
            user['balance'] += amount
            Bank.__update()
            print(f"Amount deposited successfully! New Balance: {user['balance']}")

    def withdrawMoney(self):
        print("\n--- Withdraw Money ---")
        user = self._find_user()
        if not user:
            return

        try:
            amount = int(input("Enter the amount to withdraw: "))
        except ValueError:
            print("Invalid amount value.")
            return

        if amount <= 0:
            print("Amount must be greater than 0.")
        elif user['balance'] < amount:
            print(f"Transaction Declined: Insufficient funds. Current Balance: {user['balance']}.")
        else:
            user['balance'] -= amount
            Bank.__update()
            print(f"Amount withdrawn successfully! Remaining Balance: {user['balance']}")

    def showDetails(self):
        print("\n--- Account Details ---")
        user = self._find_user()
        if not user:
            return
        
        print("\nYour account profile details:")
        for key, value in user.items():
            print(f"{key.capitalize()}: {value}")

    def updateDetails(self):
        print("\n--- Update Account ---")
        user = self._find_user()
        if not user:
            return

        print("Leave a field blank and press Enter to keep current values.")
        new_name = input(f"New Name [{user['name']}]: ").strip()
        new_email = input(f"New Email [{user['email']}]: ").strip()
        new_pin_str = input(f"New 4-digit PIN [{user['pin']}]: ").strip()

        if new_name:
            user['name'] = new_name

        if new_email and new_email.lower() != user['email'].lower():
            if "@" not in new_email:
                print("Error: Updated email requires an '@' symbol. Email change aborted.")
            elif Bank.__is_email_taken(new_email):
                print("Error: This email is already associated with another account.")
            else:
                user['email'] = new_email

        if new_pin_str:
            if new_pin_str.isdigit() and len(new_pin_str) == 4:
                user['pin'] = int(new_pin_str)
            else:
                print("Error: Invalid PIN structure. PIN change aborted.")

        Bank.__update()
        print("Details processed and updated successfully.")

    def userDelete(self):
        print("\n--- Delete Account ---")
        user = self._find_user()
        if not user:
            return

        check = input("Are you sure you want to permanently close this account? (y/n): ").strip().lower()
        if check == 'y':
            Bank.data.remove(user)
            Bank.__update()
            print("Account has been permanently deleted.")
        else:
            print("Account deletion process canceled.")


def main():
    Bank.load_database()
    bank_system = Bank()
    
    while True:
        print("\n========= BANK SYSTEM =========")
        print("1. Create an Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Show Details")
        print("5. Update Details")
        print("6. Delete Account")
        print("7. Exit")
        
        try:
            choice = int(input("Select an option (1-7): "))
        except ValueError:
            print("Please input a valid choice number.")
            continue

        if choice == 1: bank_system.createAccount()
        elif choice == 2: bank_system.depositMoney()
        elif choice == 3: bank_system.withdrawMoney()
        elif choice == 4: bank_system.showDetails()
        elif choice == 5: bank_system.updateDetails()
        elif choice == 6: bank_system.userDelete()
        elif choice == 7: 
            print("Thank you for using our bank application. Goodbye!")
            break
        else: 
            print("Invalid range selection! Please enter a choice between 1 and 7.")


if __name__ == "__main__":
    main()