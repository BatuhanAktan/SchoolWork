'''
Search related functions for Assignment 4.

Author: Dr. Burton Ma
Edited by: Batuhan Aktan
Student Number: 20229360
Date:  April 2021
'''


def sort1000(t):
    if len(t) != 0:
    	aux = [0]*1000 #list with 1000 0s
    	for i in range(1000): #going through all the numbers
    		for j in t:
    			if i == j:
    				aux[i] += 1 #occurence counter
    index = 0
    for i in range(len(aux)):
        if aux[i] != 0:
            for j in range(aux[i]):
                t[index] = i #t at index equals our index at aux
                index += 1 #index moves 1 up


def min_val(t):
    return min_val_helper(t, 0, len(t)-1, (len(t)-1)//2)


def min_val_helper(t, low, high, mid):
    if high-low <= 1: #high and low are next to one another
        if t[high] > t[low]: #returns lower value
            return t[low]
        else:
            return t[high]
    elif t[low]-t[mid] > 0: # chooses decreasing side always
        return min_val_helper(t, mid, high, mid+(high-mid)//2)
    else:
        return min_val_helper(t, low, mid, mid//2)



    

