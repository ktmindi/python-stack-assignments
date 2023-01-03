# to run a python file type python3 filename.py in the terminal
"""
a 
multi-line 
comment
in
python
"""

#how to print something to the console - in other languages we use console.log()
print("Hello World!!!")

#data types in python

#boolean
is_hungry = True
#numbers
age = 100
#strings
name = "Robo Kat"
# tuples - data that cannot be modified after creation and can hold a group of mixed values
dog = ('Charlotte', 'Mini Poodle', 2, 'Brown')
# to call one of these values we can use
print(dog[1]) # output will be Mini Poodle
# lists - CAN BE modified after creation and usually stores a collection of RELATED data
empty_list=[]
dogs = ('Charlotte', 'Chloe', 'Chester', 'Tyga', 'Kiwi')
print(dogs[4]) # output will be Kiwi
# to change a value in the list 
dogs[1] = 'Chester'
dogs[2] = 'Chloe'
print(dogs) # output: Charlotte, Chester, Chloe, Tyga, Kiwi
# to add a value to the end 
dogs.append('Cookie') 
# to remove a value from the end
dogs.pop() # will remove cookie
# to remove a value in the designated location 
dogs.pop(4) # will remove Kiwi


# loop basics
for x in range(0,10,2):
    print(x)

for x in range(5,10,-3):
    print(x)



# function basics
def add(a,b):
    x = a + b
    return x

new_val=add(2,5)
print(new_val)



def say_hi(name):
    print("hi" + name)

#say_hi(mindy)

# OOP basics
class User:
    bank_name = "First Bank Of USA"
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0

guido = User("Eduardo", "eddie@rawr.com")
print(guido.name)