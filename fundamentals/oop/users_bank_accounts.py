
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


class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "accountone" : BankAccount(.03,1000),
            "accounttwo" : BankAccount(.04,300)
        }

    def display_user_balance(self):
        print(f"user: {self.name}, account one balance: {self.account['accountone'].display_account_info()}")
        print(f"user: {self.name}, account two balance: {self.account['accounttwo'].display_account_info()}")
        return self

# fixed transfer_money method 
# code before looked like 
# def transfer_money(self,amount,user):
        # self.amount -= amount
        # user.amount += amount
        # self.display_user_balance()
        # user.display_user_balance()
        # return self
# this only works in the user.py file because each user has an amount attribute. when we combine the bank account class with the user class this code needs to be updated 
    def transfer_money(self, user, amount):
        print("*" * 80)
        print(f"Transferring {amount} from {self.name} to {user.name}.")
        self.account['accountone'].withdraw(amount)
        user.account['accountone'].deposit(amount)
        print("Transfer Complete")


stacy = User("stacy")
brad = User("brad")
#debugged by changing checking to account one in line below
stacy.account['accountone'].deposit(100)
stacy.display_user_balance()
stacy.transfer_money(brad, 200)
brad.display_user_balance()
stacy.display_user_balance()