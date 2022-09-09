class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance += amount
        return self
    def display_user_balance(self):
        print(f"user: {self.name}, balance: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self


brady = User("brady")
monty = User("monty")
carly = User("carly")

brady.make_deposit(100).make_deposit(300).make_deposit(200).make_withdrawl(200).display_user_balance()

monty.make_deposit(300).make_deposit(500).make_withdrawl(400).make_withdrawl(100).display_user_balance()

carly.make_deposit(1000).make_withdrawl(50).make_withdrawl(300).make_withdrawl(20).display_user_balance()


monty.transfer_money(300, brady)