pin=1234
class bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ₹{amount}")
            print(f"Deposit successful. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transactions.append(f"Withdrew ₹{amount}")
                print(f"Withdrawal successful. New balance: {self.balance}")
            else:
                print("Insufficient funds. Withdrawal failed.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")