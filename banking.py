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
    def show_transactions(self):
        print("\n-------Transaction History--------")
        if len (self.transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)  

name=input("Enter your name: ")
acc=bank(name, 1000000)


while True:
    print("\n choose an options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Transactions")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice =='1':
        amount=float(input("Enter the amount to deposit: "))
        acc.deposit(amount)
    elif choice =='2':
        a=int(input("enter a pin"))
        if a==pin:
            amount=float(input("Enter the amount to withdraw: "))
            acc.withdraw(amount)
        else:
            print("Incorrect pin. Withdrawal failed.")
            break
    elif choice =='3':
        acc.show_transactions()     
    elif choice =='4':      
        print("Thank you for banking with us. Goodbye!")        
        break
    else:        
        print("Invalid choice. Please enter a number between 1 and 4.")        