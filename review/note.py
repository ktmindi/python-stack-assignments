# to run a python file type python3 filename.py in the terminal
"""
a 
multi-line 
comment
in
python
"""

print("Hello World!!!")


# loop basics
for x in range(0,10,2):
    print(x)

for x in range(5,10,-3):
    print(X)



# function basics
def add(a,b):
    x = a + b
    return x

new_val=add(2,5)
print(new_val)



def say_hi(name):
    print("hi" + name)

say_hi(mindy)

# OOP basics
class User:
    bank_name = "First Bank Of USA"
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0

guido = User("Eduardo", "eddie@rawr.com")
print(guido.name)