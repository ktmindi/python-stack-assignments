"""Countdown - Create a function that accepts a number as an input. 
Return a new list that counts down by one, from the number (as the 0th element) 
down to 0 (as the last element)."""

from ast import Pass


def countdown(n: int):
    integers = []
    if n>=1:
        for i in range(n+1):
            integers.append(n-i)
        print(integers)

countdown(29)

"""Print and Return - Create a function that will receive a list with two numbers. 
Print the first value and return the second."""

def print_and_return(list):
    print(list[0])
    return(list[1])

print(print_and_return([1,2]))

"""First Plus Length - Create a function that accepts a list and returns 
the sum of the first value in the list plus the list's length."""

def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([5,3,1,57,6,3]))


"""Values Greater than Second - Write a function that accepts a list and creates a new list 
containing only the values from the original list that are greater than its 2nd value. 
Print how many values this is and then return the new list. 
If the list has less than 2 elements, have the function return False"""

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range (0,len(list)):
        if list [i] > list[1]:
            output.append(list[i])
            print(len(output))
        return output

print(values_greater_than_second([5,2,1,4,6,3,1,2]))
print(values_greater_than_second([7]))


"""This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
The function should create and return a list whose length is equal to the given size, 
and whose values are all the given value."""

def length_and_value(size,value):
    output= []
    for i in range (0,size):
        output.append(value)
    return output

print(length_and_value(8,10))
print(length_and_value(3,6))