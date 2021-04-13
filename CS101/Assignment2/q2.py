"""
Computes a basic retail calculation involving 3 items and adding the tax.
Author:  Batuhan Aktan
Student Number: 20229360
Date:  Sept 2020
"""
# asks the user for the price of the 3 items.
item1 = float(input("Please enter the price of the first item: "))
item2 = float(input("Please enter the price of the second item: "))
item3 = float(input("Please enter the price of the third item: "))

total = item1 + item2 + item3 # adds all the items together

totalWithTax = total * 1.15 # adds tax to the total price.

print("Your total is $" + str(round(totalWithTax, 2))) # prints the price rounded to 2 decimals. 
