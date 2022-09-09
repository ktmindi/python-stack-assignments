class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: $ {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

account_one = BankAccount(.03,1000)
account_two = BankAccount(.04,300)

account_one.deposit(100).deposit(300).deposit(200).withdraw(400).yield_interest().display_account_info()
account_two.deposit(400).deposit(550).withdraw(50).withdraw(300).withdraw(10).withdraw(55).yield_interest().display_account_info()

BankAccount.print_all_accounts()