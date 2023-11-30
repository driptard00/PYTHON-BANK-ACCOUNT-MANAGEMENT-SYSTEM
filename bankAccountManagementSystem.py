class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount:.2f} successful.")
        self.display_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount:.2f} successful.")
            self.display_balance()


# Function to perform bank account operations
def bank_management():
    account_holder = input("Enter the account holder's name: ")
    initial_balance = float(input("Enter the initial balance: $"))

    # Creating a bank account object
    account = BankAccount(account_holder, initial_balance)

    while True:
        print("\nBank Account Management System")
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            account.display_balance()
        elif choice == '2':
            amount = float(input("Enter the deposit amount: $"))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the withdrawal amount: $"))
            account.withdraw(amount)
        elif choice == '4':
            print("Exiting Bank Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Run the bank management system
bank_management()
