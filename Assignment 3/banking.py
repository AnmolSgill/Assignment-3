from datetime import datetime
import unittest


#in progress
class User:
    def __init__(self, username, chequing_account=None, savings_account=None, line_of_credit_account=None, credit_card_account=None):
        self.username = username
        self.chequing_account = chequing_account
        self.savings_account = savings_account
        self.line_of_credit_account = line_of_credit_account
        self.credit_card_account = credit_card_account

    
    def create_savings_account(self, account_number, balance, min_balance):
        self.savings_account = Savings_Account(self, account_number, balance, min_balance=500.00)
        print(f"User {self.username} created a new Savings account.\nAccount no. {account_number} | Balance: ${balance} (Minimum balance ${min_balance}).\n")


    def create_chequing_account(self, account_number, balance, over_draft_fee=15.00):
        self.chequing_account = Chequing_Account(self, account_number, balance, over_draft_fee)
        print(f"User {self.username} created a new Chequing account.\nAccount no. {account_number} | Balance: ${balance}.\n")

    def create_credit_card_account():
        print()

    def create_line_of_credit_account():
        print()

    def deposit_savings(self, amount):
        self.savings_account.deposit(amount)

    def deposit_chequing(self, amount):
        self.chequing_account.deposit(amount)
    
    def withdraw_savings(self, amount):
        self.savings_account.withdraw(amount)

    def withdraw_chequing(self, amount):
        self.chequing_account.withdraw(amount)

    def display_chequing_account_details(self):
        self.chequing_account.display_account_details()
    
    def display_savings_account_details(self):
        self.savings_account.display_account_details()

    def e_transfer_from_chequing(self, amount, user):
        print(f"User {self.username} transferring ${amount} to User {user.username}")


    def e_transfer_from_savings(self, amount, user):
        print(f"User {self.username} transferring ${amount} to User {user.username} ")
        print()

    
# Complete
class Transaction: 
    def __init__(self, amount, transaction_type, account_number):
        self.date = datetime.now()
        self.amount = amount
        self.transaction_type = transaction_type
        self.account_number = account_number

    def __str__(self):
        return (f"{self.date} - Activity on account {self.account_number} for {self.transaction_type} in the amount of ${self.amount}")
    
#Complete
class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def new_transaction(self, transaction:Transaction):
        self.transactions.append(transaction)
        
    def __str__(self):
        return ", ".join([str(transaction) for transaction in self.transactions])     

# complete
class Bank_Account:
    def __init__(self, user: User, account_number, balance:float=0.0):
        self.user = user
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = TransactionHistory()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Account no.: {self.account_number} Deposited ${amount}.")
            print(f"New balance: ${self.balance}.\n")
            self.transaction_history.new_transaction(Transaction(amount, "deposit", self.account_number))
        else:
            print("Invalid deposit amount.\n")
    
    def display_account_details(self):
        print(f"Account no. {self.account_number} Summary:\nCurrent Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid amount or insufficient funds.\n")


# complete
class Savings_Account(Bank_Account):
    def __init__(self, user, account_number, balance:float=0.0, min_balance:float=500.00):
        super()._init__(user, account_number, balance)
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= self.min_balance:
            self.balance -= amount
            print(f"Account no.: {self.account_number} Withdrew ${amount}.")
            print(f"New balance: ${self.balance}")
            self.transaction_history.new_transaction(Transaction(amount, "withdrawal", self.account_number))
        else:
            print("Invalid withdrawl amount or insufficient funds for savings account minimum balance.\n")

#complete
class Chequing_Account(Bank_Account):
    def __init__(self, user, account_number, balance:float=0.0, over_draft_fee:float=15.00):
        super().__init__(user, account_number, balance)
        self.over_draft_fee = over_draft_fee

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= 0:
            self.balance -= amount 
            print(f"Account no.: {self.account_number} Withdrew ${amount}")
            print(f"New balance: ${self.balance}.\n")
            self.transaction_history.new_transaction(Transaction(amount, "withdrawal", self.account_number))
        elif amount <= 0:
            print("Invalid withdrawl amount.\n")
        else:
            self.balance -= self.over_draft_fee
            print(f"Insufficient funds. You have been charged a ${self.over_draft_fee} overdraft fee")
            print(f"Account no. {self.account_number} New balance: ${self.balance}.\n")
        
    

class Credit_Card_Account(Bank_Account):
    print()

class Line_of_Credit(Bank_Account):
    print()