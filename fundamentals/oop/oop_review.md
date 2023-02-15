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

### Loop Control    
---
### Functions
---
