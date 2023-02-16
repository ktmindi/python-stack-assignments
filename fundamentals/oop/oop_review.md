# Python OOP Review
### Fundamentals
- To turn our terminal into a shell for Python we type **`python3`** into our terminal for Macs and **`python`** for Windows
    - If we see three forward arrows >>> then we know that we are inside our Python Shell
- To run a Python file first create our python file using the extension **`.py`** then save the file and inside our terminal we can run this file now by typing **`python3 file_name.py`**
---
### Syntax
- Rather than using brackets or curly braces python uses indentation for blocks of code
```python
x = 10
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
```
- Everytime we start a code block there must be at least one line of indented code following or we will get a syntax error. If we dont know what we are going to put in it yet we can use **`pass`** to prevent this.
```python
for val in my_string:
    pass
```
---
### Data Types - PRIMITIVE
- **Primitive** data types include: boolean, numbers, and strings
    - `Numbers` - there are three basic types
        - int: whole numbers positive or negative ex. 30
        - float: decimal numbers, positive or negative ex. 3.4
        - complex: a part of the real number system and often referenced with the letter j ex. 1+3j
        - if we need to convert one data type to another we can use the following
        ``` python
        int_to_float = float(35)
        float_to_int = int(44.2)
        int_to_complex = complex(35)
        print(int_to_float)
        print(float_to_int)
        print(int_to_complex)
        print(type(int_to_float))
        print(type(float_to_int))
        print(type(int_to_complex))
        ```
        - Python does not have a built in random number generator so we can use the random module instead
        ``` python
        import random
        print(random.randint(2,5)) # will provide a random number between 2 and 5
        ```
    - `Strings` - can be enclosed with single or double quotes
        - String can be printed containing data from variables in a few different ways
        ```python
        # We can use a comma
        name = "Charlotte"
        print("My name is", name) 

        # We can concatenate into a new string with +
        name = "Charlotte"
        print("My name is" + name) 
        # output for both will be: My name is Charlotte


        # One difference between these two methods is clear when we try to print an integer 
        num = 94
        print("My age is", num)
        # Output: My age is 94

        num = 94
        print("My age is" + num)
        # Type Error: can only concatenate str (not "int") to str

        # To fix this we can convert the int to a string like so
        print("My age is" + str(94))

        # We can also convert a str into an int if we need to
        total = 35
        user_val = "34"
        total = total + user_val  #output: TypeError
        total = total + int(user_val) #output: total will be 69
        ```
        - String Interpolation - when we inject variables into our strings. This can be done in a few ways.
            - `F-Strings`
            ```python
            first_name = "Mindy"
            last_name = "Nguyen"
            age = 27
            print(f"My name is {first_name} {last_name} and I am {age} years old.")
            ```
            - `string.format()` method was used prior to f-strings. Format method reads from left to right, replacing the curly braces with the value of the arguments provided in order. So the same number of {} and arguments must be provided.
            ```python
            first_name = "Mindy"
            last_name = "Nguyen"
            age = 27
            print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
            # output: My name is Mindy Nguyen and I am 27 years old.
            print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
            # output: My name is 27 Mindy and I am Nguyen years old.
            ```
            - `% - formatting` method is even older than the .format() method. We may encounter this when troubleshooting or researching
            ```python
            hw = "Hello %s" % "world" 	# with literal values
            py = "I love Python %d" % 3 
            print(hw, py)
            # output: Hello world I love Python 3
            name = "Zen"
            age = 27
            print("My name is %s and I'm %d" % (name, age))		# or with variables
            # output: My name is Zen and I'm 27
            ```
        - Commonly used string methods:
            - `string.upper()`: returns a copy of the string with all the characters in uppercase.
            - `string.lower()`: returns a copy of the string with all the characters in lowercase.
            - `string.count(substring)`: returns number of occurrences of substring in string.
            - `string.split(char)`: returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
            - `string.find(substring)`: returns the index of the start of the first occurrence of substring within string.
            - `string.isalnum()`: returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
            - `string.join(list)`: returns a string that is all strings within our set (in this case a list) concatenated.
            - `string.endswith(substring)`: returns a boolean based upon whether the last characters of string match substring.
---
### Data Types - COMPOSITE

- **Composite** data types include:
    - `Lists` - (also known as an **array** in other programming languages) can hold a group of values, usually collection of related data, and is **mutable** (can be modified after creation)
        - We can think of a list like a dresser with multiple drawers in which each drawer stores some information
        - Can be a mixture of any Python data types: tuples, strings, numeric, and even a list itself (a list within a list)
        - Built in functions for sequences:
            - `enumerate(sequence)` used in a for loop context to return two-item-tuple for each item in the list indicating the index followed by the value at that index.
            - `map(function, sequence)` applies the function to every item in the sequence you pass in. Returns a list of the results.
            - `min(sequence)` returns the lowest value in a sequence.
            - `sorted(sequence)` returns a sorted sequence
        - Built in methods for lists:
            - `list.extend(list2)` adds all values from a second sequence to the end of the original sequence.
            - `list.pop(index)` remove a value at given position. if no parameter is passed, defaults to final value in the list.
            - `list.index(value)` returns the index position in a list for the given parameter.
        - Useful Links:
            - https://docs.python.org/2/library/functions.html
    ```python
    #Lists are created with values inside of square breackets
    empty_list = []

    ninjas = ['Brandon', 'Steve', 'Wilber']

    #We access values using an index number starting with 0
    print(ninjas[2]) #output: Wilber
    ninjas[0] = 'Drake'

    #Add to the end of the list
    ninjas.append('Mike')
    print(ninjas) # output: ['Drake', 'Steve', 'Wilber', 'Mike']

    #Remove the last value from the list
    ninjas.pop()
    print(ninjas) # output: ['Drake', 'Steve', 'Wilber']

    #Remove the value at the specified index from the list
    ninjas.pop(1)
    print(ninjas) # output: ['Drake', 'Wilber']



    #Another list example
    fruits = ['apple', 'banana', 'orange', 'strawberry']
    vegetables = ['lettuce', 'cucumber', 'carrots']

    fruits_and_vegetables = fruits + vegetables
    print(fruits_and_vegetables)
    # output: ['apple', 'banana', 'orange', 'strawberry', 'lettuce', 'cucumber', 'carrots']

    salad = 3 * vegetables
    print(salad)
    # output: ['lettuce', 'cucumber', 'carrots', 'lettuce', 'cucumber', 'carrots', 'lettuce', 'cucumber', 'carrots']



    #Like the slice function in JAVASCRIPT we can return a copy of the list, constrained to the specified indicies in python like so
    x = [99,4,2,5,-3]
    print(x[:])
    #the output would be [99,4,2,5,-3]
    print(x[1:])
    #the output would be [4,2,5,-3]
    print(x[:4])
    #the output would be [99,4,2,5]
    print(x[2:4])
    #the output would be [2,5]
    ```
    - `Tuples` - can contain mixed data types and is **immutable** (cannot be modified after creation)
        - Is a container for a fixed sequence of data objects. They are sequences and again cannot be changed once created.
        - Name comes from the Latin suffix for multiples: double, triple, quadruple, quintuple.
        - Tuples are useful for representing what other languages often call records — some related information that belongs together, like your student record. 
        - **List functions can also be used for tuples**
        - *TUPLE AS RETURN VALUES*: Functions can always only return a single value, but by making that value a tuple, we can effectively group together as many values as we like, and return them together. This is very useful — we often want to know some highest and lowest score, or we want to find the mean and the standard deviation, or we want to know the year, the month, and the day.
        - With tuples we can write our code with the assumption that each value will be found at its original position and this guards against errors
        - Like strings, tuples are immutable. Once Python has created a tuple in memory, it cannot be changed. **But we can add and slice tuples.** See example below
    ```python
    #Tuples are created by declaring different comma-separated values
    tuple_letters = 'a', 'b', 'c', 'd', 'e'

    #Optionally we can put these values between parentheses. 
    #This is the conventional way to write tuples.
    tuple_data = ('physics', 'chemistry', 1997, 2000)
    tuple_num = (1, 2, 3, 4, 5)
    dog = ('Bruce', 'poodle', 19, False)

    # We can print data from a tuple via an index that again starts at 0
    print (dog[0]) #output: Bruce

    #Add tuples
    dog = dog + ("domestic",)
    # output: ('Bruce', 'poodle', 19, False, 'domestic')


    #Slice tuples
    dog = dog[:3] + ("man's best friend",) + dog[4:]
    # output: ('Bruce', 'poodle', 19, 'man's best friend', 'domestic')
    
    #Tuples as return Values
    def get_circle_area(r):
        c = 2 * math.pi * r
        a = math.pi * r * r
        return (c, a) #Return (circumference, area) of a circle of radius r
    
    ```

    - `Dictionaries` - A group of key-value pairs
        - They are a mutable set type that can store any number of Python objects, including other set types. 
        - Dictionaries consist of pairs (called items) of keys and their corresponding values. 
        - In other languages dictionaries are referred to as an associative array or hash table - with hash table being the most generic term.
        - Characteristics of a python dictionary
            - Unordered collection of objects
            - Values are accessed using a key.
            - A dictionary can shrink or grow as needed.
            - The contents of dictionaries can be modified.
            - Dictionaries can be nested.
            - Sequence operations such as slice cannot be used with dictionaries.
        - Each KEY in a dictionary MUST BE UNIQUE
            - If you make an assignment using an existing key as the index, the old value associated with that key is overwritten by the new value.
            - This characteristic is an advantage when you need to modify an existing value for an existing key.
        - **Nesting** is also allowed in dictionaries. Dictionaries may contain lists and tuples. 
        - Built in functions for dictionaries:
            - `cmp(dict1, dict2)` - Compares two dictionaries. The comparison process starts with the length of each dictionary, followed by key names, followed by values. The function returns 0 if the two dicts are equal, -1 if dict1 > dict2, 1 if dict1 < dict2.
            - `len()` - give the total length of the dictionary.
            - `str()` - produces a string representation of a dictionary.
            - `type()` - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dict type.
        - Built in methods for dictionaries: (either dict.method(yourDictionary) or yourDictionary.method() will work)
            - `.clear()` - removes all elements from the dictionary
            - `.copy()` - returns a shallow copy dictionary
            - `.fromkeys(sequence, [value] )` - create a new dictionary with keys from sequence and values set to value.
            - `.get(key, default=None)` - For key key, returns value or default if key is not in dictionary.
            - `.items()` - returns a list of dictionary's (key, value) tuple pairs.
            - `.keys()` - return a list of dictionary keys.
            - `.setdefault(key, default=None)` - similar to get(), but will set dict[key]=default if key is not already in dictionary.
            - `.update(dict2)` = adds dictionary dict2's key-values pairs to an existing dictionary.
            - `.values()` - returns list of dictionary values.
    ```python
    #Dictionaries are created with values inside of curly braces {}
    empty_dict = {}

    #Instead of indicies, we use keys to track position
    new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}

    new_person['name'] = 'Jack'	
    # updates if the key exists, adds a key-value pair if it doesn't

    new_person['hobbies'] = ['climbing', 'coding']
    print(new_person)	# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}


    w = new_person.pop('weight')	
    # removes the specified key and returns the value

    print(w)
    # output: 160.2
    print(new_person)
    # output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}




    #Another example showing techniques when building dictionaries
    #literal notation
    weekend = {"Sun": "Sunday", "Sat": "Saturday"}

    #create an empty dictionary then add values
    capitals = {}
    capitals["svk"] = "Bratislava"
    capitals["deu"] = "Berlin"
    capitals["dnk"] = "Copenhagen"
    print(capitals)
    # output: {'svk': 'Bratislava', 'deu': 'Berlin', 'dnk': 'Copenhagen'}



    #To access values use the key
    print(weekend["Sun"]) # output "Sunday"
    print(capitals["svk"]) # output "Bratislava"



    #Removing values can be done in two ways
    value_removed = capitals.pop('svk') 
    # will remove the key 'svk' and return it's value

    del capitals['dnk'] 
    # will delete the key, and not return anything



    #Nested Dictionaries
    context = {
        'questions':[
            {'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
            { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
            { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
            { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
        ]
    }
    ```
- Common built in methods for dictionaries: https://www.w3schools.com/python/python_ref_dictionary.asp
---
### Common Functions
- Checking data type we can use **`type`**
```python
print(type(2.63)) # output: <class 'float'>
print(type(new_person)) # output: <classs 'dict'>
```
- For data types that have a length attribute we can use **`len`** function to get the length
```python
print(len(new_person)) # output: 4 (the number of key-value pairs)
print(len('Coding Dojo')) # output: 11
```
---
### Conditional Statements
- Allow us to run certain lines of code depending on whether certain conditions are met
- Keywords for conditional statements are `if`, `elif`, and `else`
- Some Examples:
```python
   x = 12
    if x > 50:
    	print("bigger than 50")
    else:
    	print("smaller than 50")
    # because x is not greater than 50, the second print statement is the only one that will execute
    
    x = 55
    if x > 10:
    	print("bigger than 10")
    elif x > 50:
    	print("bigger than 50")
    else:
    	print("smaller than 10")
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
    if x < 10:
    	print("smaller than 10")
    # nothing happens, because the statement is false   
```
---
### Comparison and Logic Operators
| Operator      | Description | Example |
| ----------- | ----------- | -------- |
| ==   | Checks if the value of two operands are equal| 1 == 2 => False
| !=   | Checks if the value of two operands are not equal| 1 != 2 => True
| >   | Checks if the value of left operand is greater than the value of right operand| 1 > 2 => False
| <   | Checks if the value of left operand is less than the value of right operand| 1 < 2 => True
| >=   | Checks if the value of left operand is greater than or equal to the value of right operand| 1 >= 2 => False
| <=   | Checks if the value of left operand is less than or equal to the value of right operand| 1 <= 2 => True
| and   | Checks that each expression on the left and right are both True| (1 <= 2) and (2 <= 3) => True
| or   | Checks if either the expression on the left or right is True| (1 >= 2) or (2 >= 3) => False
| not   | Reverses the true-false value of the operand| not (1 <= 2 and 2 >= 3)  => True ~~ not 1 <= 2 and 2 >= 3 => False

---
### Loops
- If we want to iterate through numbers, we can use Python's range function which can have between 1 and 3 arguments:
    - Range with 1 argument **(argument = stop)**
        - START: Defaults to 0
        - STOP: Exclusive of 1st
        - STEP: Defaults to 1
        ```python
        range(5) 
        #output: 0,1,2,3,4
        ```
    - Range with 2 arguments **(arguments = start, stop)**
        - START: Inclusive of 1st
        - STOP: Exclusive of 2nd
        - STEP: Defaults to 1
        ```python
        range(5,10) 
        #output: 5,6,7,8,9

        #5 is included in the output because the start number is INCLUSIVE
        ```
    - Range with 3 arguments **(arguments = start, stop, step)**
        - START: Inclusive of 1st
        - STOP: Exclusive of 1st
        - STEP: Iterates by 3rd
        ```python
        range(5,10,2) 
        #output: 5,7,9

        for x in range(0, 10, 2):
            print(x)
            # output: 0, 2, 4, 6, 8

        for x in range(5, 1, -3):
            print(x)
            # output: 5, 2
        ```
### For Loops 
- Can be used on any sequence
    - Loops through String
    ```python
    for x in 'Hello':
        print(x)
    #output: 'H', 'e', 'l', 'l', 'o'
    ```
    - Loops through Lists
        - We can use the range function and send in the length of the list as the stopping value
        - BUT IF WE ARE NOT INTERESTED IN THE INDEX VALUES and want to just see the values of each item in the list in order, we can actually loop to get the values of the list directly
    ```python
    my_list = ["abc", 123, "xyz"]
    for i in range(0, len(my_list)):
        print(i, my_list[i])
    # output: 0 abc, 1 123, 2 xyz
        
    # OR 
        
    for v in my_list:
        print(v)
    # output: abc, 123, xyz
    ```
    - Loops through Tuples
        - We can iterate through tuples in the same ways we can iterate through lists above
    ```python
    for data in dog:
        print(data)
    ```
    - Loops through Dictionaries
        - When we iterate through a dictionary, the iterator is each of the **KEYS** of the dictionary
    ```python
    my_dict = { "name": "Mimi", "language": "Python" }
    for k in my_dict:
        print(k)
    # output: name, language



    # if we want the values of our dictionary
    my_dict = { "name": "Mimi", "language": "Python" }
    for k in my_dict:
        print(my_dict[k])
    # output: Mimi, Python



    #Additional methods for iteration
    capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}

    #Iterate through the keys
    for key in capitals.keys():
        print(key)

    #Iterate through the values
    for val in capitals.values():
        print(val)

    #Iterate through both keys and values
    for key,val in capitals.items():
        print(key, "=", val)
    ```
### While Loops
- Another way of looping *while* a certain condition is true
    ```python
    #Basic syntax for a while loop
    while <expression>:
        # do something, including progress towards making the expression False. Otherwise we have an infinite loop.
    

    #Both of these loops are the same:

    #FOR LOOP
    for count in range(0,5):
        print("looping=", count)
    
    #TURNED INTO WHILE LOOP
    count = 0
    while count <= 5:
        print("looping=", count)
        count+=1
    ```
### Else
- We can use an else statement when there are certain conditions in our loop that are not met where we still want to do something.
    - Else section will only be executed if the while loop runs normally and its conditional is false
    - If our while loop is exited prematurely because of a `break` or `return` statement, then the else code section will never be executed
    ```python
    y = 3
    while y>0:
        print(y)
        y = y - 1
    else:
        print("Final else statement")
    #output: 
    # 3
    # 2
    # 1
    # Final else statement
    ```
### Loop Control
- When we want finer control over our loops we can use the following statements to do so
    - Break
        - The break statement exits the current loop prematurely, resuming execution at the first post-loop statement
        - This can be used in both *for* and *while* loops
        - Most Common Use: When some external condition is triggered, requiring a hasty exit from a loop
        - When loops are nested, a break will only exit the innermost loop
    ```python
    for val in "string":
        if val == "i":
            break
        print(val)
    # output: s, t, r
    ```
    - Continue
        - immediately returns control to the beginning of the loop
        - the continue statement rejects, or skips, all the remaining statements in the current iteration of the loop, and continues normal execution at the top of the loop
        - Very useful when you want to skip specific iteration(s) but still want to keep looping to the end.
    ```python
    for val in "string":
        if val == "i":
            continue
        print(val)
        #output: s,t,r,n,g
        #notice, no i in the output, but the loop continued after the i
    
    
    y = 3
    while y > 0:
        print(y)
        y = y - 1
        if y == 0:
            break
    else:
    # only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")

    # output: 3, 2, 1

    ```
---
### Functions
- Functions are named blocks of code that we can execute to perform a specific task. 
- Simply put, a function is a list of instructions
- Characteristics of a function:
    - has a name
    - takes in parameters (parenthesis required, parameters optional)
    - perform a series of instructions
    - return something afterwards (will return None if there is no explicit return statement)
- We can think of the function as a recipe. If we were preparing a meal we would:
    - (1) specify the ingredients (*variables*) needed for the meal
    - (2) use the actual ingredients (*pass arguments*) when starting (*invoke a function*)
    - (3) follow the instructions step by step (*function*) for the ingredients (*parameters*) and prepare them
    - (4) once the food is ready we serve it up to those that are eating (*return*)
```python
#this is out list of ingredients or parameters
def burger(bun, meat, cheese, toppings):
    #instructions or logic in our function
    split bun in half
    cook meat
    place cheese on meat
    place meat on bottom
    add toppings
    place top bun over everything
    #now we can serve up the burger
    return prepared ingredients

#this is where the burger actually gets made and pass in arguments to the function
lunch = burger(sesame bun, ground beef, american cheese, [mayo, lettuce, bacon, onions])
```
- Using functions helps reduce duplication of code, breaks down complex problems into simpler pieces, and improves clarity of code.
- Function syntax
    - `def` keyword signifies the declaration of a function
    - name of the function comes after the def keyword and is what we use to call on it later
    - to run the function we invoke or call it - this is done outside of the function by using `function_name()`
    - inside the parenthesis are our arguments or inputs for the function
```python
def add(a,b):    #function name: 'add', parameters: a and b
    x = a + b    #process
    return x    #return value: x

new_val = add(3,5) #calling function with arguments 3 and 5
print(new_val) #the result gets sent back to and saved into new_val then is printed so we should see 8
```
- Difference between Parameters and Arguments
    - Parameters are used to define the input of functions. In the example below name is a parameter
    - Arguments are passed into functions. In the example below Mike and Abe are arguments that we are passing into the function.
```python
def say_hi(name):
    print("Hi" + name)

say_hi('Mike')
say_hi('Abe')
```
### `Its important to remember that a function call is equal to whatever that function returns`
- returning a value from a function allows us to store that value in a variable 
```python
def say_hi(name):
    return "Hi " + name

greeting = say_hi("Michael") 
# the returned value from say_hi function gets assigned to the 'greeting' variable

print(greeting) # this will output 'Hi Michael'


def add(a, b):
    x = a + b
    return x
sum1 = add(4,6) # output 10
sum2 = add(1,4) # output 5
sum3 = sum1 + sum2 # output 15
```
### Default Parameters
- When we want to allow some of the parameters to be optional to the caller of the function, we can set defaults. 
```python
# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
	print(f"good morning {name}\n" * repeat)
be_cheerful()    # output: good morning (repeated on 2 lines)
be_cheerful("tim")    # output: good morning tim (repeated on 2 lines)
be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
be_cheerful(repeat=6)    # output: good morning (repeated on 6 lines)
be_cheerful(name="michael", repeat=5)    # output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)

```
---
### OOP ( Object Oriented Programming)
- Benefits of using OOP:
    - Implements D.R.Y. (Dont' Repeat Yourself) Code
    - Makes our application scalable
    - Makes our code reusable
    - Makes our applications easily maintainable
### Class
- Whenever we declare a variable we are creating an **instance** of a class 
    - For example x = [1,2,3] ; x is an instance of a list 
- An instance is simply an object that follows the pattern defined by its class
- Think about classes as blueprints for our custom objects. They are NOT the actual objects, but a plan for what properties and functionaltiies they may have.
```python
#to create a class we simply declare a class variable and name it whatever we want
class User:
    pass 
```
### Attributes
- Attributes are characteristics shared by all instances of the class type
- **Instance Attributes** are defined in a 'magic method' called `__init__`, which is called when a new object is instantiated
    - the first parameter of an instance method within a class will be self, and the instance attributes are also indicated by self.. self is a reference to the **instance**, not the class.
    ```python
    #Here we are declaring a class and naming it user
    class User:
        def __init__(self):
            self.name = "Sy"
            self.email = "abc@123.com"
            self.account_balance = 0

    
    #Now we can create instances of the user
    brandy = User()
    #But when we access the instance's attributes we will see the default value of the class we created
    print(brandy.name) #output: Sy

    #To set the values of our instance's attributes we can 
    brandy.name = "Brandy"
    print(brandy.name) #output: Brandy
    ```
- **Class Attributes** are defined outside of any instance methods, and is shared among all instances of the class
    - They are more flexible because we can change them on an instance or the entire class
    ```python
    class User:
        bank_name = "Mindy's Bank of Fun"
        def __init__(self):
            self.name = "Sy"
            self.email = "abc@123.com"
            self.account_balance = 0

    man = User()
    stan = User()
    
    #changing a class attribute on an instance
    stan.bank_name = "Uphill Cred Union"
    print(stan.bank_name) #output: Uphill Cred Union

    #changing a class attribute on the entire class
    User.bank_name = "Bank of Awesomeness"
    print(stan.bank_name) #output: Uphill Cred Union
    print(man.bank_name) #output: Bank of Awesomeness
    ```
- Because we dont want every instance of the user to have the same name, email and account balance we should **pass in arguments** into the `__init__` method to specify a user's instance attributes
    ```python
    Class User:
    # class attributes get defined in the class
    bank_name = "Mindy's Bank of Fun"
    #now our method has two parameters
    def __init__(self, name, email_address):
        #we assign them accordingly
        self.name = name
        self.email = email_address
        # the account is set to 0 as a default value of all user instances
        self.account_balance = 0
    
    #now when we create an instance of our user class we can do the following
    abby = User("Abby", "abster@whoa.com")
    print(abby.name) #output: Abby
    print(abby.email) #output: abster@whoa.com
    ```

### Methods
- Methods are actions that an object can perform
- In other words, methods are just functions that belong to a class
- Therefore when we call them, we have to call them from an instance of a class
- **Remember that the first parameter of EVERY METHOD within a class should be SELF**
    ```python
    abby.make_deposit(1000)
    ```
- To be able to call this method, it needs to exist
    ```python
    class User:
        def __init__(self, name, email):
            self.name = name
            self.email = email
            self.account_balance = 0
        #adding the deposit method
        def make_deposit(self,amount):
            #takes an argument that is the amount of the deposit
            self.account_balance += amount
            #the specific user's account increases by the amnt of the value recieved
            return self
    



    # now our method is written we can call it
    abby = User("Abby", "abster@whoa.com")
    abby.make_deposit(100)
    abby.make_deposit(300)
    print(abby.account_balance) # output: 400

    #we can chain methods together so that we dont have to take up space and repeat calling our user instance over and over again
    abby.make_deposit(200).make_deposit(100).make_deposit(200)
    ```
- Notice that in addition to arguments passed in as a traditional function, *methods also have access to the class's attributes*
### Self
- The self parameter includes all the information about the individual object that has called the method
- It gets passed in because we are calling on the method *from the instance* - this is known as **implicit passage of self**
    - When we call on a method from an instance, that instance, along with all of its information (name, email, balance), is passed in as self.
- The practice of having OOP return its own instance is pretty common and is done in other programming languages, though the variable name in some languages is not self, but instead this.
---
### When to use `Class` and `Static` Methods
- When we create a method on a class we pass in self to refer to the *instance* of the object
    - These normal methods are referred to as **instance methods**
- When we want to implement methods that belong to the **class** and not the **instance** we can use the `class` and `static` method

### `Class Method`
- Defined by declaring `@classmethod` 
- These methods belong to the class itself and therefore instead of implicitly passing in **self** we pass `cls`
    ```python
    class BankAccount:
    # class attribute
    bank_name = "First Venture"
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)


    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name


    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum
    ```
- **Remember that class methods have no access to the instance attribute or any attribute that starts with self.**

### `Static Method`
- Defined by declaring `@staticmethod`
- Static methods are functions that have no access on **instance** or **class** attributes, so if we need any existing values they need to be passed in as arguments
- If we wanted our BankAccount class to have a utility function to add or subtract we could implement @staticmethod on the class.
    ```python
    class BankAccount:
    # ... __init__ goes here

    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self


    # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
    	if (balance - amount) < 0:
            return False
        else:
            return True
    ```
- There is no TRUE PURPOSE for static methods in Python, but they do offer us a way to organize our code in a better way.
- We could do a simple check to see if the account can be withdrawn from but what if we want to scale up our application with more logic around this idea. 
    - Well then we would have to update every where we are making that evaluation, but if we put it in a @staticmethod, then we can update all the checks from one place. 
    - And our code becomes a bit more D.R.Y.
---
### Association Between Classes
- In OOP Terms, the User and BankAccount classes that we created previously have an **association** or relationship between them.
    - Meaning, instead of keeping track of a balance directly in the User class, we'll **encapsulate** all the bank account information and associate a user with a specific instance of a Bank Account
    - MEANING.. the User class, instead of directly having a balance attribute, will now have an attribute of type BankAccount.
    ```python
    class User:
        def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line
    ```
- Note: the BankAccount class at this point should be in the same file as the user class so the reference is recognized - if we want to have both classes in separate files this is called *modularization* which we will get into later.
    ```python
    class User:
        def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line
    
        def example_method(self):
            # we can call the BankAccount instance's methods
            self.account.deposit(100)
            # or access its attributes
            print(self.account.balance)
    ```
- Look at python-stack-assignments > fundamentals > oop > users_bank_account.py for example
---
### Four Pillars of OOP
1. Encapsulation - the idea that we can group code (attributes and methods) together into objects; we use classes or "coding blue prints" to define what our objects are and how they behave.
```python
class SouperL:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200
    def stew_now(self,veggies):
        print(f"Using {veggies}!")
        print("Stew it up!")
    def clean(self):
        print("Cleaning!")
```
2. Inheritance - the idea that we pass along attributes and methods from one class into a 'sub-class' or child class (thus not having to re-write it). Child classes can be more specific versions of their Parent class.
```python
class Broccoli( SouperL ):
    def __init__(self,name):
        super().__init__(name)
        self.ingredient = "broccoli"
    def make_broccoli(self,veggies):
        super().stew_now(veggies)
        print("Greeniess!")
```
3. Polymorphism - means 'many forms', and the idea is that a Child class can have a different version of a method than the parent class. 
```python
#Depending on the class, the clean method will do different things
class Broccoli( SouperL ):
    def __init__(self,name):
        super().__init__(name)
        self.ingredient = "broccoli""
    def make_broccoli(self,veggies):
        super().stew_now(veggies)
        print("Greeniess!")
    def clean(self):
        print("Cleaning the greens!")
```
4. Abstraction - an extension of encapsulation. allowing us to hide attributes or methods that a specific class doesnt need to know about, like SouperL. This way the chef can make a bowl of soup in a simpler manner.
```python
class Chef:
    def __init__(self,name):
        self.name = name
        self.soup = SouperL("Stew")
    def make_soup(self):
        self.soup.stew_now()
```
---
### More on Inheritance
- A relationship between classes where we define a new class based on another class. It allows one class to take on the attributes and methods from another class with little additional code.
- Results in reduced redundancy and complexity.
- Example: in our bank account example, lets say that a user can have both a checking account and a retirement account. 
    - These two accounts would have alot in common with little differences.
    ```python
    #If we created two separate classes for these two accounts it would look something like this 
    class CheckingAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
    	# code
    def withdraw(self, amount):
    	# code
    def write_check(self, amount):
    	# code
    def display_account_info(self):
    	# code
    
    class RetirementAccount:
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    	self.is_roth = is_roth
    def deposit(self, amount):
    	# code - assess tax if necessary
    def withdraw(self, amount):
    	# code - assess penalty if necessary
    def display_account_info(self):
    	# code

    #Right away we see alot of redundancy
    #Using inheritance by putting the parent class in parenthesis, both the child classes (checking and retirement) now have ALL the attributes and functionality of the parent class
    class CheckingAccount(BankAccount):
        pass
    class RetirementAccount(BankAccount):
        pass
    #From here we just need to figre out the differences between the classes and add them while maintaining what we need from the parent class
    ```
 ### Super
- To indicate we are trying to use the parent's methods, we call on it with the keyword `super`
    ```python
    #Here is what we want our retirement account __init__ method to do and what our parent bankaccount class __init__ method does:
    class RetirementAccount(BankAccount):
        def __init__(self, int_rate, is_roth, balance=0):
            self.int_rate = int_rate
            self.balance = balance
    	    self.is_roth = is_roth

    class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    #We quickly observe that the parent class already does 2 of the 3 lines we are trying to execute in our retirement account class. 

    #Now we will utilize super to call on any of the parent's methods
    class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
    	super().__init__(int_rate, balance)	
        self.is_roth = is_roth

    class BankAccount:
        def __init__(self, int_rate, balance=0):
            self.int_rate = int_rate
            self.balance = balance
    ```
    - The first line in our RetirementAccount init method allows the parent to manage the setting of int_rate and balance. The only line we need to add is to set the is_roth attribute since this is the attribute unique to the RetirementAccount Class
- Another example - suppose we wanted to add some logic to our withdraw method
    ```python
    class RetirementAccount(BankAccount):
        def withdraw(self, amount, is_early):
            if is_early:
                amount = amount * 1.10
            super().withdraw(amount)
            return self
        
    class BankAccount:
    def withdraw(self, amount):
    	if (self.balance - amount) > 0:
    	    self.balance -= amount
        else:
    	    print("INSUFFICIENT FUNDS")
    	return self
    ```
    
---
### Modules & Packages
Modules
- Modules are python files with the `.py` extension which implement a set of functions. 
- Modules are imported using the `import` command
- Built in modules can be found here: https://docs.python.org/3.6/library/index.html
- Creating Your Own Modules
    - Inside your project folder/directory **create** two `.py` files
        1. modular_example/arithmetic.py
        2. modular_example/calculations.py
    - To import the arithmetic module (or file) into the calculations module open the calculations.py file and on line one write `import arithmetic`
    - You will notice that you do not need to write the `.py` extension when you are importing 
```python
#arithmetic.py file
def add(x, y):
    return x + y
def multiply(x, y):
    return x * y
def subtract(x, y):
    return x - y

#calculations.py file
import arithmetic
print(arithmetic.add(5, 8))
print(arithmetic.subtract(10, 5))
print(arithmetic.multiply(12, 6))
```
Packages
- A package is a collection of modules in directories that give a package hierarchy
- Packages are imported using `from` subdirectory `import` module/file
- EXAMPLE: Lets say we have a directory named **sample_project**
    - Inside this directory we have **python_file.py** and **my_modules**
        - Inside our sub-directory **my_modules** we have four more python files: **init.py , test_module.py, another_module.py, third_module.py**

| sample_project      |  |  |
| ----------- | ----------- | -------- |
|    | python_file.py| 
|    | my_modules|
|    || --init--.py
|    | | test_module.py
|    | | another_module.py
|    | | third_module.py

- In the example above, the package name is **my_modules**
- To use the module test_module we can import it in two ways
```python
import my_modules.test_module

# OR 

from my_modules import test_module
```
--init--.py File
- This file was required for all packages in Python 2.7; it would often be empty, but was required to indicate that the files in the folder were part of the package.
- Python 3.3+, we only need this file if we need to customize what modules are available to anyone attempting to import the package. 
    - For example, if we didn't want another_module or third_module to be accessible for importing, we could override the __all__ variable
```python
#sample_project/my_modules/__init__.py
__all__ = ["test_module"]
```
---
### Overriding & Polymorphism
Overriding
- If we want the child class to behave completely differently than the parent we can **override** the function to replace the functionality.
    ```python
    class Parent:
        def method_a(self):
            print("invoking PARENT method_a!")
    class Child(Parent):
        def method_a(self):
            print("invoking CHILD method_a!")
    dad = Parent()
    son = Child()
    dad.method_a()
    son.method_a() #notice this overrides the Parent method!

    #In our terminal we will see invoking PARENT method_a! followed by invoking CHILD method_a! when we call on each class
    ```
Polymorphism
- Allows us to specify common methods in an "abstract" level and implement them in particular instances
- Its the process of using an operator or function in different ways for different data input
    ```python
    # We'll use the Person class to demonstrate polymorphism
    # in which multiple classes inherit from the same class but behave in different ways
    class Person:
    def pay_bill(self):
        raise NotImplementedError

    # Millionaire inherits from Person
    class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!")

    # Grad Student also inherits from the Person class
    class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?")
    ```
    - Based on this example, a millionair and grad student are both persons but when it comes to paying a bill they can act quite different. 
- This pattern is useful when you know that each subclass of a parent class must define a specific behavior in a method, and you dont want to define a default behavior in the parent class
---
### Inputs and Outputs
- The ability to interpret some code and give a result (Output) is a common ability in all coding languages.
- Results can be a variety of different results including print statements, data types, html/css/javascript to render on a browser, etc.
- Many times, we write our code to work with a certain set of data, but the data could be different in different situations. 
    - In this case, we set up to pass an input to our code, so the interpreter can work with that data. 
- For now we will look at the input() function which allows us to interact with the bash window.
```python
favorite_color = input("what is your favorite color?") 
# input takes a prompt, which needs to be a string
print(f'Your favorite color is: {favorite_color}')
# output prints the color given to the console. 

# When we save this python file and run it the first thing that will pop up is the prompt

#What is your favorite color? 

#The print statement will not be executed until you enter a response. Because the program is expecting an input and cannot move forward until it is provided
# Lets say you type in yellow and press enter. Then you will see the print statement

# Your favorite color is: yellow
```