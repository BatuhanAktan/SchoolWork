"""
Using the length of the truss, height of the truss and the length of the roof this program calculates the size of the roof.
Author:  Batuhan Aktan
Student Number: 20229360
Date:  Oct 2020
"""
import math
def pythagorean(base, height):
    """
    This function calculates the hypotenuse given the base and the height of a right angle triangle.
    Parameters:  base, height - integer values representing half the width of truss nad truss's height.
    Return Value - hypotenuse - an integer
    """
    hypotenuse = math.sqrt(int(base)**2 + int(height)**2) # Finds the hypotenuse
    return hypotenuse # returns the hypotenuse value

def area(length, hypotenuse):
    """
    This function calculates the area of two sides of the roof.
    Parameters:  lenght, hypotenuse - integer values representing length of the roof and width of the side of the roof.
    Return Value - area of the side of the roof - an integer
    """
    side = int(length)* hypotenuse
    return round(side*2, 2) # returns the rounded area of the roof.

def main():
    """
    This function calculates the area of the roof and gets the user inputs.
    Parameters: None
    Return Value: None
    """
    while True:
        heightTruss = int(input("Please enter the height of the truss: "))
        truss = int(input("Please enter the width of the truss: "))
        roofLength = int(input("Please enter the finished length of the roof: "))

        print("The area of the roof is", area(roofLength, pythagorean(truss/2, heightTruss)), "m^2") # calls area function with pythagorean function as one of the parameters
        print("Would you like to repeat the process?")

        response = input("Please respond with 'y' for yes or 'n' for no: ")
        if response.lower() == 'y':
            continue
        break

main() # calls the main function.
