"""
Asks the user on their preference and matches them with a restaurant.
Author:  Batuhan Aktan
Student Number: 20229360
Date:  Sept 2020
"""

vegeterian = input("Is anyone in your party a vegetarian? ")
vegan = input("Is anyone in your party a vegan? ")
gluten_free = input("Is anyone in your party gluten-free? ")


print("Here are your restaurant choices: ")


if vegeterian.lower() == "yes": # checks vegeterian input

    if vegan.lower() == "yes":  # checks vegan input

        if gluten_free.lower() == "yes": # checks gluten free input
            print("\tThe Chef’s Kitchen") # tabbed to match format given in example 
            print("\tCorner Café")

        elif gluten_free.lower() == "no":
            print("\tCould not match you with any restaurants. Please try again.") # if the users input does not match with any of the potential restaurants, outputs

    elif vegan.lower() == "no":

        if gluten_free.lower() == "yes":
            print("\tMain Street Pizza Company")

        elif gluten_free.lower() == "no":
            print("\tMama’s Fine Italia")

elif vegeterian.lower() == "no":

    if vegan.lower() == "yes":

        if gluten_free.lower() == "yes":
            print("\tCould not match you with any restaurants. Please try again.")

        elif gluten_free.lower() == "no":
            print("\tCould not match you with any restaurants. Please try again.")

    elif vegan.lower() == "no":

        if gluten_free.lower() == "yes":
            print("\tCould not match you with any restaurants. Please try again.")

        elif gluten_free.lower() == "no":
            print("\tJoe’s Gourmet Burgers")


