class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        print("user:", self.name, "balance:", self.account_balance)

    def make_withdrawl(self, amount):
        self.account_balance += amount
        print("user:", self.name, "balance:", self.account_balance)

    def display_user_balance(self):
        print("user:", self.name, "balance:", self.account_balance)


    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()


brady = User("brady")
monty = User("monty")
carly = User("carly")

brady.make_deposit(100)
brady.make_deposit(300)
brady.make_deposit(200)
brady.make_withdrawl(200)

monty.make_deposit(300)
monty.make_deposit(500)
monty.make_withdrawl(400)
monty.make_withdrawl(100)

carly.make_deposit(1000)
carly.make_withdrawl(50)
carly.make_withdrawl(300)
carly.make_withdrawl(20)

monty.transfer_money(300, brady)