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
### Data Types
- Primitive data types include: boolean, numbers, and strings
- Composite data types include:
    - Tuples - can contain mixed data types and is **immutable** (cannot be modified after creation)
    ```python
    dog = ('Bruce', 'poodle', 19, False)
    print (dog[0]) #output: Bruce
    ```
    - Lists - can hold a group of values, usually collection of related data, and is **mutable** (can be modified after creation)
    ```python
    empty_list = []
    ninjas = ['Brandon', 'Steve', 'Wilber']
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
    ```
    - Dictionaries - group of key-value pairs 
    ```python
    empty_dict = {}
    new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}

    new_person['name'] = 'Jack'	
    # updates if the key exists, adds a key-value pair if it doesn't

    new_person['hobbies'] = ['climbing', 'coding']
    print(new_person)	# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}


    w = new_person.pop('weight')	
    # removes the specified key and returns the value

    print(w)		# output: 160.2
    print(new_person)	# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        
    ```
- Common built in methods for dictionaries: https://www.w3schools.com/python/python_ref_dictionary.asp

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