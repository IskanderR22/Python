

class User:
    def __init__(self, name, email, balance):

        self.name = name
        self.email = email
        self.balance = balance
    
    def make_deposit(self, deposit):
        self.balance = self.balance + deposit
    
    def make_withdrawl(self, withdrawl):
        self.balance = self.balance - withdrawl

    def display_balance(self):
        print(self.balance)
        

micheal = User("Micheal", "micheal@gmail.com", 1000)
micheal.make_deposit(1000)
micheal.make_deposit(1000)
micheal.make_deposit(1000)
micheal.make_withdrawl(500)
micheal.display_balance()

harry = User("Harry", "harry@gmail.com", 5000)
harry.make_deposit(100)
harry.make_deposit(100)
harry.make_withdrawl(1000)
harry.make_withdrawl(1000)
harry.display_balance()

josh = User("Josh", "josh@gmail.com", 3000)
josh.make_deposit(10000)
josh.make_withdrawl(1000)
josh.make_withdrawl(1000)
josh.make_withdrawl(1000)
josh.display_balance()