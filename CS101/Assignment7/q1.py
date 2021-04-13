'''
This is a simplified version of a hangman game. The computer chooses a word
from a pre-defined list of words and the user guesses letters until they have
filled in all the letters in the word.

Author:  Batuhan Aktan
Student Number: 20229360
Date:  Oct 2020
'''
import random

def getSecretWord():
    """
    This function chooses a word from the list of potential secret
    words.
    Parameters:  None
    Return Value: a string representing the secret word
    """

    #DO NOT MODIFY THIS FUNCTION

    
    potentialWords = ["tiger", "lion", "elephant", "snake", "zebra"]

    
    #random.randint(0, 4) will generate an integer between 0 and 4
    #this is then used to select a value from potentialWords
    return potentialWords[random.randint(0,4)]

def printStringWithSpaces(word):
    """
    This function prints the blank representation ("___") of the
    secret word on the screen with spaces between each underscore
    so that the user can better see how many letters there are.
    Parameter: string
    Return Value:  None
    """

    #TODO -- complete this function so that it prints "word" (a string)
    #so that there are spaces between each letter.
    #eg:  word = "watch", the function prints w a t c h
    #you will need a loop to do this.
    #recall that print() can be given a parameter end=' ' to keep all output
    #on the same line.


    for element in word:
        print(element, end=' ')


    #leave the following two lines at the end of your function for nicer output
    print()
    print()


def convertWordToBlanks(word):
    """
    Creates a string consisting of len(word) underscores.
    For example, if word = "cat", function returns "___"

    Parameter: string
    Return Value: string
    """

    #TODO -- complete this function so that it produces a string with
    #underscores representing the parameter "word" (which is a string).
    #eg:  word = "watch", the function returns "_____"  (5 underscores)
    #You will need a loop for this.  Also, a return statement.

    #leave this line (and use the variable newString in your code

    
    newString = ""  #start with an empty string and add onto it


    for i in range(0,len(word)):
        newString += '_'

        
    return newString
    

def updateRepresentation(blank, secret, letter):
    """
    This function replaces the appropriate underscores with the guessed
    letter.
    Eg.  letter = 't', secret = "tiger", blank = "_i_er" --> returns "ti_er"
    Paramters:   blank, secret are strings
                letter is a string, but a single letter.
    Returns:  a string
    """

    #TODO -- complete this function so that it produces a new string
    #from blank with letter inserted into the appropriate locations.
    #For example:
    #   letter = 't', secret = "tiger", blank = "_i_er" --> newString "ti_er"
    #newString should be returned.
    #hint:
    #iterate through each character of secret by index position
    #   check to see if letter = current character at index position
    #      if yes, add this letter to newString
    #      if no, add the letter from blank found at index position

    #leave this line (and use the variable newString in your code

    
    newString = ""

    
    for element in range(0, len(secret)): # goes through the index of the string.
      if letter == secret[element]: # checks if the letter guessed matches the element of secret at the given index.
        newString += letter
      else:
        newString += blank[element]

    return newString


def updateUsedLetters(usedLetters, letter):
    """
    This function concatenates the guessed letter onto the list of letters
    that have been guessed, returning the result.
    Parameters: string representing the used letters
                string respresenting the current user guess
    Return Value:  string
    """

    #TODO -- complete this function so that it returns the concatentation
    #of the string usedLetters with the letter. 
    usedLetters += letter
    
    return usedLetters

def main():
    """
    This implements the user interface for the program.
    """
    usedLetters = "" #no letters guessed yet
    secret = getSecretWord()
    print("The secret word is ", secret)
    #TODO - add one line of code here to call the function
    #convertWordToBlanks to convert the secret word
    #to a string of underscores.  Assign the result to
    #the variable blank as shown below.
    blank = convertWordToBlanks(secret)  

    
    printStringWithSpaces(blank)

    
    while blank != secret:
        userGuess = input("Please enter a single letter guess: ")
        
        #check for valid input
        while not(userGuess.isalpha()) or len(userGuess) != 1:
            userGuess = input("Please enter valid input(a single letter guess):")

        #TODO:  Add one line of code here (at the same level of indentation of
        #this comment) to check that userGuess is NOT in the string usedLetters.
        #ADD YOUR CODE HERE
        if userGuess not in usedLetters: 
            print("You have guessed ", userGuess)

            if userGuess in secret:
                #letter is in the secret word so update the blank representation
                blank = updateRepresentation(blank, secret, userGuess)
            
            printStringWithSpaces(blank)

            #add the letter to the string of used letters 
            usedLetters = updateUsedLetters(usedLetters, userGuess)
            
        else:
            #letter has been guessed already -- update the user
            print("You have already guessed that letter!!!")
            print("Here are the letters you have guessed so far: ")
            printStringWithSpaces(usedLetters)
            
        
    print("You got it!!  The word was", secret)


main()
