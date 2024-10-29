class BankAccount:
    all_accounts = []
    def __init__(self, int_rate = 0.01, balance = 0.0):
        self.int_rate = int_rate
        self.balance = balance  
        self.balance = balance 
        BankAccount.all_accounts.append(self) 
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            self.balance -= 5 # penalty for insufficient funds
            print("Insufficient Funds")
        return self     
    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self
                
account1 = BankAccount(balance=100.00)
account1.display_account_info().deposit(700).deposit(800).deposit(900).withdraw(50).yield_interest()

account2 = BankAccount(balance=100.00)
account2.withdraw(50).withdraw(50).withdraw(60).withdraw(70)
account2.display_account_info()

account1.display_account_info().yield_interest()

