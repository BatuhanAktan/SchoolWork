"""
Determines if a person is an infant, a child, a teenager, or an adult based on their age
Author:  Batuhan Aktan
Student Number: 20229360
Date:  Sept 2020
"""

'''
Test Cases

Input   Expected Output

1       You are an infant
2       You are a child
15      You are a teenager
60      You are an adult
80      You are a senior
-1      That is not a valid age
'''


age  = int(input("Please enter your age: ")) # Asks user for their age


if 0 <= age <= 1: # checks if the user is in the infant category
    print("You are an infant") # prints you are an infant if they are in that category
elif 1 < age < 13:
    print("You are a child") 
elif  13 <= age < 20:
    print("You are a teenager")
elif 20 <= age < 65:
    print("You are an adult")
elif 65<= age:
    print("You are a senior")
else:
    print("That is not a valid age") # since it is impossible to be less than 0 years old the age is not valid
