



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
        # print(self.amount)
        # print("this is current price")
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


account1 = BankAccount(100, 0.2)
account2 = BankAccount(100, 0.1)

account1.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest()
account1.display_amount()

account2.deposit(100).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest()
account2.display_amount()

BankAccount.print_all_instances()