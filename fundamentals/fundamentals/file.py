num1 = 42 # variable declaration, initialize integer

num2 = 2.3 # variable declaration, initialize float

boolean = True # variable declaration, initialize boolean, must be capital T or error occurs

string = 'Hello World' # variable declaration, initialize string

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary

fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuple

print(type(fruit)) # log statement, type check

print(pizza_toppings[1]) # log statement, access value 'Sausage'

pizza_toppings.append('Mushrooms') # add value to end of list 'Mushrooms'

print(person['name']) #log statement, access 'name' value

person['name'] = 'George' #change 'name' value of variable person

person['eye_color'] = 'blue' #change 'eye_color' value of variable person

print(fruit[2]) # log statement, access value 'banana'


if num1 > 45: # conditional if statement, a greater than b
    print("It's greater") # log statement, string
else: # conditional else statement
    print("It's lower") # log statement , string

if len(string) < 5: # conditional if statement, length check, a less than b
    print("It's a short word!") # log statement, string
elif len(string) > 15: # conditional else if statement, length check, a greater than b
    print("It's a long word!") # log statement, string
else: # condiitonal else statement
    print("Just right!") # log statement, string

for x in range(5): # start for loop, end at 4,
    print(x) # log statement, sequence 0,2,3, end at 4
    
for x in range(2,5): # start for loop, increment
    print(x) # log statement, sequence 2,3, end at 4 
    
for x in range(2,10,3): # start for loop, 2 to 10 increments of 3
    print(x) # log statement, sequence 2,5, end at 8

x = 0 # variable declaration
while(x < 5): # start while loop
    print(x) # log statement
    x += 1 # increment

pizza_toppings.pop() # remove value from end of list
pizza_toppings.pop(1) # remove value second on the list 'Sausage'

print(person) #log statement, access 'person' value

person.pop('eye_color') #remove 'eye_color' value from list

print(person) #log statement, access 'person' value

for topping in pizza_toppings: # start for loop
    if topping == 'Pepperoni': # conditional if statement
        continue # continue statement
    print('After 1st if statement') # log statement, string
    if topping == 'Olives': # conditional if statement
        break # break statement

def print_hello_ten_times(): # create function
    for num in range(10): # for loop
        print('Hello') # log statement, string 

print_hello_ten_times() # calling function

def print_hello_x_times(x): # create function, parameter x
    for num in range(x): # for loop sequence
        print('Hello') # log statement, string

print_hello_x_times(4) #calling function, parameter 4

def print_hello_x_or_ten_times(x = 10): # create function, parameter x = 10
    for num in range(x): # for loop sequence
        print('Hello') # log statement, string

print_hello_x_or_ten_times() # calling function
print_hello_x_or_ten_times(4) # calling function, parameter x=4


"""
Bonus section
"""

print(num3) # NameError
num3 = 72 #NoError, Variable declaration
fruit[0] = 'cranberry' # TypeError
print(person['favorite_team']) # KeyError 
print(pizza_toppings[7]) # IndexError
print(boolean) #NameError
fruit.append('raspberry') #AttributeError
fruit.pop(1) #AttributeError
