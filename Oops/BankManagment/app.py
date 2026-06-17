import json
import random
import string
import os
from pathlib import Path
import streamlit as st


class Bank:
    current_dir = Path(__file__).parent.resolve()
    database = current_dir / 'data.json'

    @classmethod
    def load_database(cls):
        try:
            # Initialize session state tracking list if it doesn't exist
            if 'bank_data' not in st.session_state:
                if cls.database.exists() and cls.database.stat().st_size > 0:
                    with open(cls.database, 'r') as fs:
                        st.session_state['bank_data'] = json.load(fs)
                else:
                    st.session_state['bank_data'] = []
                    with open(cls.database, 'w') as fs:
                        json.dump([], fs)
        except Exception as err:
            st.error(f"Error loading database: {err}")
            st.session_state['bank_data'] = []

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(st.session_state['bank_data'], fs, indent=4)
            fs.flush()
            os.fsync(fs.fileno())

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
        return any(user['email'].lower() == email.lower() for user in st.session_state['bank_data'])

    def createAccount(self, name, age, email, pin_input):
        if "@" not in email:
            return {"status": "error", "message": "Invalid email format! The '@' symbol is required."}
            
        if Bank.__is_email_taken(email):
            return {"status": "error", "message": "An account with this email is already registered!"}

        if not (pin_input.isdigit() and len(pin_input) == 4):
            return {"status": "error", "message": "PIN must be exactly 4 digits."}

        if age < 18:
            return {"status": "error", "message": "You must be 18 or older to open an account."}

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin_input),
            "accountNo": Bank.__accountGenerate(),
            "balance": 0
        }

        st.session_state['bank_data'].append(info)
        Bank.__update()
        return {"status": "success", "data": info}

    def _find_user(self, accnumber, pin_input):
        if not pin_input.isdigit():
            return None
        
        pin = int(pin_input)
        
        # Always reload safely directly from file system to match live changes
        try:
            if self.database.exists() and self.database.stat().st_size > 0:
                with open(self.database, 'r') as fs:
                    st.session_state['bank_data'] = json.load(fs)
        except Exception:
            pass

        for user in st.session_state['bank_data']:
            if user['accountNo'].strip() == accnumber.strip() and user['pin'] == pin:
                return user
        return None

    def depositMoney(self, user, amount):
        if amount <= 0 or amount > 10000:
            return {"status": "error", "message": "You can only deposit an amount between 1 and 10,000."}
        
        user['balance'] += amount
        Bank.__update()
        return {"status": "success", "message": f"Successfully deposited! New Balance: {user['balance']}"}

    def withdrawMoney(self, user, amount):
        if amount <= 0:
            return {"status": "error", "message": "Amount must be greater than 0."}
        if user['balance'] < amount:
            return {"status": "error", "message": f"Insufficient funds. Current Balance: {user['balance']}"}
        
        user['balance'] -= amount
        Bank.__update()
        return {"status": "success", "message": f"Successfully withdrawn! Remaining Balance: {user['balance']}"}

    def updateDetails(self, user, new_name, new_email, new_pin_str):
        if new_name:
            user['name'] = new_name

        if new_email and new_email.lower() != user['email'].lower():
            if "@" not in new_email:
                return {"status": "error", "message": "Updated email requires an '@' symbol."}
            if Bank.__is_email_taken(new_email):
                return {"status": "error", "message": "This email is already associated with another account."}
            user['email'] = new_email

        if new_pin_str:
            if new_pin_str.isdigit() and len(new_pin_str) == 4:
                user['pin'] = int(new_pin_str)
            else:
                return {"status": "error", "message": "Invalid PIN layout. Must be exactly 4 digits."}

        Bank.__update()
        return {"status": "success", "message": "Details processed and updated successfully."}

    def userDelete(self, user):
        st.session_state['bank_data'].remove(user)
        Bank.__update()
        return {"status": "success", "message": "Account has been permanently deleted."}


# --- STREAMLIT UI LAYOUT ---

st.set_page_config(page_title="Secure Bank App", page_icon="🏦", layout="centered")
st.title("🏦 Secure Digital Banking System")

# Safe continuous execution load hook
Bank.load_database()
bank = Bank()

st.sidebar.header("Navigation Menu")
menu = st.sidebar.radio(
    "Choose an Action:",
    ["Create Account", "Deposit Money", "Withdraw Money", "Show Details", "Update Details", "Delete Account"]
)

# 1. CREATE ACCOUNT
if menu == "Create Account":
    st.subheader("🆕 Open a New Bank Account")
    with st.form("create_acc_form", clear_on_submit=True):
        name = st.text_input("Full Name").strip()
        age = st.number_input("Age", min_value=0, max_value=120, value=18)
        email = st.text_input("Email Address").strip()
        pin = st.text_input("Set 4-Digit PIN", type="password", max_chars=4).strip()
        
        submitted = st.form_submit_button("Submit Application")
        if submitted:
            if not name or not email or not pin:
                st.warning("All input fields are mandatory!")
            else:
                response = bank.createAccount(name, age, email, pin)
                if response["status"] == "error":
                    st.error(response["message"])
                else:
                    st.success("Account successfully created!")
                    st.json(response["data"])
                    st.info("Please store your generated Account Number safely.")

# 2. DEPOSIT MONEY
elif menu == "Deposit Money":
    st.subheader("💵 Safe Deposit Portal")
    acc = st.text_input("Enter Account Number").strip()
    pin = st.text_input("Enter 4-Digit PIN", type="password", max_chars=4).strip()
    amount = st.number_input("Deposit Amount ($)", min_value=0, step=100)
    
    if st.button("Authorize Deposit"):
        user = bank._find_user(acc, pin)
        if not user:
            st.error("Invalid Account Number or incorrect PIN match.")
        else:
            response = bank.depositMoney(user, amount)
            if response["status"] == "error":
                st.error(response["message"])
            else:
                st.success(response["message"])

# 3. WITHDRAW MONEY
elif menu == "Withdraw Money":
    st.subheader("🏧 ATM Withdrawal System")
    acc = st.text_input("Enter Account Number").strip()
    pin = st.text_input("Enter 4-Digit PIN", type="password", max_chars=4).strip()
    amount = st.number_input("Withdraw Amount ($)", min_value=0, step=100)
    
    if st.button("Process Cashout"):
        user = bank._find_user(acc, pin)
        if not user:
            st.error("Invalid Account Number or incorrect PIN match.")
        else:
            response = bank.withdrawMoney(user, amount)
            if response["status"] == "error":
                st.error(response["message"])
            else:
                st.success(response["message"])

# 4. SHOW DETAILS
elif menu == "Show Details":
    st.subheader("📋 Account Information Overview")
    acc = st.text_input("Enter Account Number").strip()
    pin = st.text_input("Enter 4-Digit PIN", type="password", max_chars=4).strip()
    
    if st.button("Fetch Dashboard Records"):
        user = bank._find_user(acc, pin)
        if not user:
            st.error("Invalid Account Number or incorrect PIN match.")
        else:
            st.success("Access Granted!")
            col1, col2 = st.columns(2)
            col1.metric("Account Holder", user["name"])
            col1.metric("Registered Email", user["email"])
            col2.metric("Available Balance", f"${user['balance']}")
            col2.metric("Age", user["age"])

# 5. UPDATE DETAILS
elif menu == "Update Details":
    st.subheader("⚙️ Modify Account Attributes")
    acc = st.text_input("Enter Account Number").strip()
    pin = st.text_input("Enter Current 4-Digit PIN", type="password", max_chars=4).strip()
    
    user = None
    if acc and pin:
        user = bank._find_user(acc, pin)
        
    if user:
        st.info("Fill options you want to change. Leave options blank to persist old attributes.")
        new_name = st.text_input(f"New Name (Current: {user['name']})").strip()
        new_email = st.text_input(f"New Email (Current: {user['email']})").strip()
        new_pin = st.text_input(f"New PIN (Current: ****)", type="password", max_chars=4).strip()
        
        if st.button("Apply Profile Changes"):
            response = bank.updateDetails(user, new_name, new_email, new_pin)
            if response["status"] == "error":
                st.error(response["message"])
            else:
                st.success(response["message"])
    elif acc or pin:
        st.caption("Please input a valid combinations of account credentials above to open updating options panel.")

# 6. DELETE ACCOUNT
elif menu == "Delete Account":
    st.subheader("⚠️ Permanent Termination Suite")
    acc = st.text_input("Enter Account Number").strip()
    pin = st.text_input("Enter 4-Digit PIN", type="password", max_chars=4).strip()
    
    confirm = st.checkbox("I confirm that I want to close this account permanently.")
    
    if st.button("Execute Termination Protocol"):
        if not confirm:
            st.warning("You must click the confirmation checkbox first.")
        else:
            user = bank._find_user(acc, pin)
            if not user:
                st.error("Authentication check failed. Invalid Credentials.")
            else:
                response = bank.userDelete(user)
                st.success(response["message"])