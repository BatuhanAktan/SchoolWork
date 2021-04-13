"""
This program takes a two dimensional list of numbers and returns a one dimensional list containing the sum of the numbers in each sublist.
Author:  Batuhan Aktan
Student Number: 20229360
Date:  Oct 2020
"""
def sublistSum(list1):
    """
    This function takes a two dimensional list of numbers and returns a one dimensional list containing the sum of the numbers in each sublist.
    Parameters: list1 - 2 dimensional list that will be converted to a one dimensional list. 
    Return Value: sumList,list containing the sum of the numbers in each sublist - a List 
    """
    sumList = [] 
    for i in list1: # iterates through the list
        total = 0 # sets total to 0 before each sublist iteration
        for j in i: # iterates through each of the sublists
            total += j
        sumList.append(total)
        
    return sumList


# Test Runs

l1 = [[1,2], []] # Assigns a test list to list 1
l2 = [[7, 9, 12], [3,24]]
l3 = [[5, 4], [2, 1, 7], [1]]
l1Sum =[3,0]
l2Sum = [28, 27]
l3Sum = [9, 10, 1]


print("Test 1","\nInput:", l1, "\nExpected Output:", l1Sum, "\nOutput:", sublistSum(l1))
print("\n\nTest 2","\nInput:", l2, "\nExpected Output:", l2Sum, "\nOutput:", sublistSum(l2))
print("\n\nTest 3","\nInput:", l3, "\nExpected Output:", l3Sum, "\nOutput:", sublistSum(l3))
