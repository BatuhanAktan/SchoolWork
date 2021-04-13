"""
Plays a game of guess the number with the user.
Author:  Batuhan Aktan
Student Number: 20229360
Date:  Sept 2020
"""

import random, webbrowser # imports the required libraries

print("Lets play a game of guess.\nI will choose a number between 0 and your choice (high) if you get it right there is a big suprise.") 
while True:
    
    high = int(input("Please enter the value for high: "))

    if high < 15:
        print("That is too low. Try again.") # if the input is lower than 15 goes back to the top of the while loop
        continue

    else:
        break


secretNumber = random.randint(0,high) # chooses a number between 0 and high
print("I choose a number between 0 and " + str(high) + " (inclusive) try to guess it.")


while True:
    
    guess = int(input("Please enter your guess: "))
    
    if guess == secretNumber:
        
        for i in range(0,10): # Creates an arrow pointing at You won statement
                print("\t\t |")
        print("\t\t V\n \t      You Won")
        webbrowser.open('https://youtu.be/1Bix44C1EzY', new=2) # Opens a new tab on browser with a congratulations video
        break
    
    elif guess > secretNumber:
        print("Too High")
        
    elif 0 <= guess < secretNumber:
        print("Too Low")
        
    elif guess < 0: # if the guess is lower than 0 ends the while loop
        print("Thank You for playing")
        break
        
