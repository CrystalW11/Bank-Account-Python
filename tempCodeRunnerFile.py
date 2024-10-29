class BankAccount:
    all_accounts = []
    def __init__(self, int_rate = 0.01, balance = 0.0, deposits = 0.0):
        self.int_rate = int_rate
        self.balance = balance  
        self.deposits = 0.0 # deposit attribute to 0.0
        
        BankAccount.all_accounts.append(self) # your code here! (remember, instance attributes go here)
        # don't worry about user info here; weill involve the user class soon
        
    def deposit(self, amount):
        self.balance += amount
        self.deposits += amount #deposits updated
        return self

    def withdraw(self, amount):
                # we use the static method here to evaluate 
                # if we can with draw the funds without going negative
        if  self.withdraw(amount):
            self.balance -= amount
        else:
            self.balance -= 5 # penalty for insufficient funds
            print("Insufficient Funds")
        return self
        # static methods have no acess to any attribute
        # only to what is passed into it
        
    @staticmethod
    def can_withdraw(balance, amount):
        return balance - amount >= 0
            
    def display_account_info(self):
        print("Balance:", self.balance)
        return self

        def yield_interest(self):
            self.balance += self.balance * self.int_rate
        return self