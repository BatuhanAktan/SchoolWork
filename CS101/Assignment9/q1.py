"""
This program generates the input to a word-cloud generator program
Author:  Batuhan Aktan
Student Number: 20229360
Date:  Nov 2020
"""

def readFile():
    """
    This function reads the input file and gets rid of all the punctuation and \n.
    Parameters:  None
    Return:  List - datalist contains all words in the input file.
    """
    try:
        file = open("cisc101PracticeFile.txt", "r") #tries to open file if not there prints file not found and exits.
    except:
        print("File not Found")
        exit()
    data = file.readlines()
    dataList = []
    newData = ''
    charactersRemove = [".", ",",";",":","?", "!", '"', "'"]
    
    for i in range(len(data)):
        for j in range(len(data[i])): # goes through all of the letters and checks if the letter is in removable characters list.
            if data[i][j] in charactersRemove: 
                continue
            elif data[i][j] == '\n': #if its a newline then it adds a space to newdata so splitting is easier.
                newData += ' '
            else:
                newData += data[i][j] #adds non removable characters into the newdata string.
    dataList = newData.split(" ")  
    return dataList


def isValid(word):
    """
    This function checks if the words is valid.
    Parameters:  word - string that will be checked if its valid.
    Return:  True, False - True is returned if the word is valid and false if it is not.
    """
    if len(word) >= 5 and not word[0].isdigit() and not word[-1].isdigit():
        return True
    else:
        return False


def cleanseWords(listOfWords):
    """
    This function List of words and gets rid of the words that are not valid.
    Parameters:  ListOfWords - A list that contains all the words in the input file.
    Return:  None.
    """
    for i in range(len(listOfWords)-1, -1, -1): #goes through the list in the reverse order
        if not isValid(str(listOfWords[i])):
            listOfWords.pop(i) #if the word is not valid pops the word out of the list.
    
            
def countFrequencies(listOfWords):
    """
    This function counts the frequency of the occurence of each word in the list.
    Parameters:  listOfWords - A list that contains all the words in the input file.
    Return:  wordsDict - A dictionary that contains the word as its key and its frequency as its value
    """
    wordDict = {}
    for i in listOfWords: #goes thorgh the keys in the dictionary
        if i.lower() in wordDict: #if the the key is already in the dictionary adds 1 to the value
            wordDict[i.lower()] = wordDict[i.lower()]+1
        else: #if the key is not in the dictionary then it is added with the value 1.
            wordDict[i.lower()] = 1
    return wordDict


def writeFile(dictionaryOfFrequencies):
    """
    This function writes all the keys and values in a dictionary each in a new line.
    Parameters:  dictionaryOfFrequencies - a dictionary that contains the words and its frequency of occurence.
    Return:  None.
    """
    file = open("outputForWordCloud101.txt", "x") #creates a new file 
    for i in dictionaryOfFrequencies:
        file.write(i +' '+str(dictionaryOfFrequencies[i])+'\n') #writes all the keys and values on seperate lines.


def main():
    """
    This function uses all the previous functions to get input from a file and create a file with the frequency of all valid words.
    Parameters:  None.
    Return: None.
    """
    listOfWords = readFile() 
    cleanseWords(listOfWords)
    dictOfWords = countFrequencies(listOfWords)
    writeFile(dictOfWords)

main()
