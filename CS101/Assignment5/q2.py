"""
The user can play choose your own destiny game.
Author:  Batuhan Aktan
Student Number: 20229360
Date:  Oct 2020
"""
import time
import random
import sys


def mathQuestion():
    """
    This function asks a user a simple math question to determine if they can proceed or not.
    Parameters: None
    Return Value: True, False - Boolean values according to if the user answered the question correctly.
    """
    print("You will be asked a question, if you answer it correctly in 5 seconds you will succesfully attack otherwise you will be devoured.")
    print("Press enter to continue")
    input()
    randNumber = random.randint(1,10) # random number generation
    print("What is the cube root of", randNumber ** 3,"?") # asks the user to find the cube root of the random number 
    a1 = int(input("Your Decision: "))
    time.sleep(5)
    if a1 == randNumber: # if the user gets the random number returns true
        return True
    else:
        return False
    
def inPortal():
    """
    This function is the final destination for going in portal
    Parameters: None
    Return Value: None
    """
    print("In the portal you find a library with unlimited knowledge.")
    print("and the time seems to move slower, You decide to live there forever, never to be bored ever again.")
    print("Thank you for playing")
    sys.exit()
def portalOut():
    """
    This function is the final destination for staying out of the portal
    Parameters: None
    Return Value: None
    """
    print("You are left there not knowing what to do.")
    print("Then you are approached by a spirit.")
    print("Spirit: You shall follow me to find eternal happiness")
    print("You follow it to be happy forever")
    print("Thank you for playing")
    sys.exit()
    
def portal():
    """
    This function is determines if the user will enter or stay out of the portal
    Parameters: None
    Return Value: None
    """
    while True:
        print("You find a portal. You can choose to go through or stay out.")
        print("Please enter your decision 'I' for in and 'O' to stay out")
        d1 = input("Your decision: ")
        if d1.lower() == "i":
            inPortal()
        elif d1.lower() == "o":
            portalOut()
        else:
            print("That does not look like one of the options. Try again")
            continue
def inCave():
    """
    This function is final destination for going in cave
    Parameters: None
    Return Value: None
    """    
    while True:
        print("You are approached by a bear will you fight it. Enter 'F' to fight, 'R' to run")
        d1 = input("Your decision: ")
        if d1.lower() == "f":
            if mathQuestion():
                print("You succesfully answered the question correctly.")
                print("You strike the bear and kill it")
                print("You claim the cave and start living as a caveman")
                print("Thank you for playing")
                sys.exit()
            else:
                print("You Died")
                print("Thank you for playing")
        elif d1.lower() == "r":
            print("You Died")
            print("Thank you for playing")
            sys.exit()
        else:
            print("That does not look like one of the options. Try again")
            continue
def outCave():
    """
    This function is the final destination for staying out of the cave
    Parameters: None
    Return Value: None
    """
    print("You stay out and a blizzard occurs and you die")
    sys.exit()
    
def mountainTop():
    """
    This function determines if the user will enter or stay out of the cave
    Parameters: None
    Return Value: None
    """
    while True:
        print("You find a cave. You can choose to go through or stay out.")
        print("Please enter your decision 'I' for in and 'O' to stay out")
        d1 = input("Your decision: ")
        if d1.lower() == "i":
            inCave()
        elif d1.lower() == "o":
            outCave()
        else:
            print("That does not look like one of the options. Try again")
            continue
def inLake():
    """
    This function is the final destination for staying for going in the cave
    Parameters: None
    Return Value: None
    """
    print("You start swimming when a large alligator approaches you.")
    print("Will you fight it. Enter 'F' to fight, 'R' to run")
    d1 = input("Your decision: ")
    if d1.lower() == "f":
        if mathQuestion():
            print("You succesfully answered the question correctly.")
            print("You strike the fish and kill it")
            print("You cook the fish and enjoy it for the entire night")
            print("Thank you for playing")
            sys.exit()
                
        else:
            print("You Died")
            print("Thank you for playing")
            sys.exit()
def camp():
    """
    This function is the final destination for camping.
    Parameters: None
    Return Value: None
    """
    print("You setup a camp next to the lake and have some smores")
    print("Thank you for playing")
    sys.exit()
def deepForest():
    """
    This function determines if the user will go in or stay out of the lake
    Parameters: None
    Return Value: None
    """
    while True:
        print("You start walking deeper into the forest when you are come across a large lake")
        print("You can choose to go in the lake or stay out and camp")
        print("Please enter your decision 'I' for in and 'O' to stay out")
        d1 = input("Your decision: ")
        if d1.lower() == "i":
            inLake()
        elif d1.lower() == "o":
            camp()
        else:
            print("That does not look like one of the options. Try again")
            continue
while True:
    print("Hello, Summoner welcome to the Enchanted forest. I am your companion Jack,\nbefore we start our journey I should let you know that there will be decisions\nthat need to be made and based on those decisions you will either survive or die trying.")
    print("\nOk, I wish you the best of luck and I'll come back when you need me again")
    print("\nPress enter to continue")
    input()
    print("You start following the path infront of you. You start looking around. You feel uneasy and suddenly notice a wolf running towards you. YOU START RUNNING.\n You come up a fork which way will you go enter 'R' for right, 'L' for Left and 'B' for back")
    d1 = input("Your Decision: ") # decision 1 is assigned
    if d1.lower() == 'r': 
        print("You continue walking along the path.")
        print("The path becomes smaller and smaller, steeper and steeper")
        print("Before you realize, you are on the gigantic mountain and you find a cave.")
        mountainTop()
    elif d1.lower() == 'l':
        deepForest()
    elif d1.lower() == 'b':
        print("You are now face to face with a wolf.")
        print("Decide what you want to do, 'f' for Fight and 'p' for play dead.")
        d2 = input("Your Decision: ") # decision 2 is assigned 
        if d2 == 'f':
            if mathQuestion():
                print("You succesfully answered the question correctly.")
                print("You strike the wolf and kill it")
                print("You start walking back the way you came.")
                portal()
                
            else:
                print("You Died")
                print("Thank you for playing")
                sys.exit() # exits the program.
                    
