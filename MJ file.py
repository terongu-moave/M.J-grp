class BankAccount:
    def __init__(self):
        self.account_name = "Moave_Terongu"
        self.account_number = 1051528774
        self.balance = 100000

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into Account {self.account_number}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from Account {self.account_number}. Current balance: {self.balance}")
        else:
            print(f"Insufficient funds in Account {self.account_number}. Current balance: {self.balance}")

    def get_balance(self):
        print(self.balance)


account1 = BankAccount()
account1.deposit(100)
account1.withdraw(50)
account1.withdraw(100)

account2 = BankAccount()
account2.deposit(200)
account2.withdraw(300)
