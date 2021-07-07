class User:
    def __init__(self, name, email,):

        self.name = name
        self.email = email
        self.account = BankAccount(amount = 0, interest = 0.2) # self.whatever you can name this whatever and link the BankAccount class
    
    def make_deposit(self, deposit):
        self.account.deposit(deposit)
        return self
    
    def make_withdrawl(self, withdrawl):
        self.account.withdraw(withdrawl)
        return self

    def display_balance(self):
        self.account.display_amount()
        return self


class BankAccount:
    bank_instances = []
    def __init__(self, amount, interest):
        self.amount = amount
        self.interest = interest 
        BankAccount.bank_instances.append(self)

    def deposit(self, deposit):
        self.amount = self.amount + deposit
        return self

    def withdraw(self, withdraw):
        if self.amount <= 0:
            print("Insufficient funds: Charging a $5 fee")
            self.amount = self.amount - 5
            self.amount = self.amount - withdraw
        elif self.amount > 0:
            self.amount = self.amount - withdraw
        return self

    def display_amount(self):
        print(self.amount)
        return self
    
    def yield_interest(self):
        if self.amount > 0:
            self.amount += (self.amount * self.interest) # Set in () to make sure the order of the math is done in order
        else:
            print("No funds in account, please deposit")
        return self
        
    @classmethod
    def print_all_instances(cls):
        for bank in cls.bank_instances:
            bank.display_amount()


micheal = User("Micheal", "micheal@gmail.com")
harry = User("Harry", "harry@gmail.com")
josh = User("Josh", "josh@gmail.com")

micheal.make_deposit(100).make_deposit(100).make_withdrawl(100).display_balance()

