"""
Determines if the inputted number is a groovy number.
Author:  Batuhan Aktan
Student Number: 20229360
Date:  Sept 2020
"""
'''
Test Cases

Input   Expected Output                   Reason

13      Its a groovy number          13 is divisible by 13
14      Its a groovy number          14 is greater than 10 and even
8       Its not a groovy number      less than 10
17      Its not a groovy number      greater than 10 but not even and not divisible by 13
'''


number = int(input("Please enter a number: ")) # Asks user to enter a number


if number > 10 and number % 2 == 0: # Checks if the number meets the first condition of being a groovy number
    print("Its a groovy number")
elif number % 13 == 0: # Checks if the number meets the second condition.
    print("Its a groovy number")
else: # If none of the conditions are met
    print("Its not a groovy number")
