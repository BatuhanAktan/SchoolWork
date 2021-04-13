'''
8 programming questions about recursion answered.

Author: Dr. Burton Ma
Edited by: Batuhan Aktan
Student Number: 20229360
Date:  March 2021
'''

import math
# The math module is needed by the starter code in Question 7
# You should not use any functions from the math module in the
# functions that you write, and you cannot import any other modules
# in this assignment.

# Question 1
def zipper(s, t):
    '''
    Given two equal length strings s and t, zipper(s, t)
    returns a new string formed by taking letters from s 
    and t in alternating order.

    Parameters
    ----------
    s: str
    String to be used in the formation of new str.
    
    t: str
    String to be used in the formation of new str.

    Returns
    ------
    str 
	the string formed with alternating letters.

    Raises
    ------
   	None
    '''
    return zipper_helper(s, t, 0)


def zipper_helper(s,t,index):
    '''
    Helper to zipper()in the formation of the word

    Parameters
    ----------
    s: str
    String to be used in the formation of new str.

    t: str
    String to be used in the formation of new str.

    index: int
    index that will be used to form the prefix
	
    Returns
    ------
    str 
        the string formed with alternating letters.

    Raises
    ------
   	None
    '''
    if not index == len(s):
        
        prefix = s[index]+t[index] #adding the first letters
        prefix += zipper_helper(s,t, index+1)
        return prefix #returns the completed word.
    
    else: 
        return ''

# Question 2
def zipper2(s, t):
    '''
    Does the same thing as zipper(s, t) except that s and
    t can now have different lengths

    Parameters
    ----------
    s: str
    String to be used in the formation of new str.

    t: str
    String to be used in the formation of new str.

    Returns
    ------
    str 
	the string formed with alternating letters.

    Raises
    ------
   	None
   	'''
    return zipper2_helper(s, t, 0)


def zipper2_helper(s,t,index):
    '''
    Helper to zipper2() forms the word.

    Parameters
    ----------
    s: str
    String to be used in the formation of new str.

    t: str
    String to be used in the formation of new str.
	
    index: int
    index that will be used to form the prefix

    Returns
    ------
    str 
	the string formed with alternating letters.

    Raises
    ------
   	None
   	'''
    if index != len(s) and index != len(t): # checking if any lengths are violated.

        prefix = s[index] + t[index]
        prefix += zipper2_helper(s,t,index+1)
        return prefix
    elif index == len(s):
        prefix = t[index:] #adds remaining letter to prefix.
        return prefix
    elif index == len(t):
        prefix = s[index:]
        return prefix
    else:
        return ''

# Question 3
def is_pow2(n):
    '''
    Returns True if the positive integer n is an integer power of 2

    Parameters
    ----------
    n: int
    The number that will be evaluated
	
    Returns
    ------
    bool 
	True if n is an integer power of 2
	False if not.

    Raises
    ------
   	None
   	'''
    if n / 2 == 1.0:
        return True
    elif n / 2 != 1.0 and n < 2: #checks if the number is less than 2 and not divisible.
        return False
    else:
        return is_pow2(n // 2)


# Question 4
def next_pow2(n):
    '''
    Returns the smallest integer value p such that  
    for a non-negative value n

    Parameters
    ----------
    n: int
    The number that will be evaluated
	
    Returns
    ------
    int 
        Value of p

    Raises
    ------
   	None
    '''
    return next_pow2_helper(n, 0)


def next_pow2_helper(n, index):
    '''
    Helper to next_pow2() 

    Parameters
    ----------
    n: int
    The number that will be evaluated

    index: int
    index that will be attempted.

    Returns
    ------
    int 
        Value of p

    Raises
    ------
   	None
    '''
    
    if 2**index >= n: #if 2^n isnt big enough tries again.
        return index
    else:	
        return next_pow2_helper(n, index+1) 


# Question 5
def max_to_end(t):
    '''
    Moves the largest element in a non-empty 
    list t to the end of the list.

    Parameters
    ----------
    t: list
    The list that will be altered

    Returns
    ------
    list  
	list with the max moved to the end.

    Raises
    ------
   	None
    '''
    val = max_to_end_helper(t)

    index = t.index(val)
    t.pop(index) # pops max
    t.append(val) # adds it to the end.
    return t
    

def max_to_end_helper(t):
    '''
    Finds the largest number in a list 
    recursively

    Parameters
    ----------
    t: list
    The list that will be evaluated

    Returns
    ------
    int
	the largest value in the list.

    Raises
    ------
   	None
    '''
    if len(t) == 1:
        return t[0]
    else:
        current = max_to_end_helper(t[1:])

        if current > t[0]: #checks if current is larger than initial.
            return current
        else:
            return t[0]


# Question 6
def get_enclosed(s):
    '''
    Returns the part of the string s that is 
    enclosed by the outermost pair of matching 
    parentheses.

    Parameters
    ----------
    s: str
    string with the parantheses.

    Returns
    ------
    str
        enclosed segment.

    Raises
    ------
    None
    '''
    if len(s) == 1: #checks if the len is 1.
        return ''
    else:
        if s[0] == '(': #looks for the opening bracket
            return get_enclosed_helper(s)

        else:
            return get_enclosed(s[1:])
	

def get_enclosed_helper(s):
    '''
    Returns the part of the string s that is 
    enclosed by the outermost pair of matching 
    parentheses. Helper to get_enclosed()

    Parameters
    ----------
    s: str
    string with the parantheses.

    Returns
    ------
    str
	enclosed segment.

    Raises
    ------
    None
    '''
    if len(s)== 1:
        return ''
    else:
        if s[-1] == ')': #looks for the ending bracket
            return (s) #returns sliced segment
        else:
            return get_enclosed_helper(s[:-1]) 

# Question 7
def pretty_print(t):
    for sublist in t:
        for elem in sublist:
            print('{:>4}'.format(elem), end='')
        print()
       

def to_triangular_grid(t):
    k = len(t)
    if k == 0:
        return [[]]
    n = (-1 + math.sqrt(1 + 8 * k)) / 2
    if not n.is_integer():
        raise ValueError('')
    return to_triangular_grid_impl(t, int(n))


def to_triangular_grid_impl(t, n):
    '''
    Returns a list of n sublists. Helper
    to to_triangular_grid()

    Parameters
    ----------
    t: list
    with a range of numbers.

	
    n: int
    value of n for sublist
    arrangement
    
    Returns
    ------
    list
	segmented list.

    Raises
    ------
   	None
    '''
    if not len(t) == 0:
        relist = []
        relist.append(t[:n]) #initial segment
        relist += to_triangular_grid_impl(t[n:], n-1) 
        return relist
    else:
        return ''

# Question 8
def triangle_cost(t):
    '''
    Recursively computes the lowest cost
    path to the bottom of the triangle

    Parameters
    ----------
    t: list
    A range of numbers.

    Returns
    ------
    int
	lowest cost path cost.

    Raises
    ------
   	None
    '''
    return triangle_cost_impl(t, 0, 0)

def triangle_cost_impl(t, row, col):
    '''
    Recursively computes the lowest cost
    path to the bottom of the triangle.
    Helper to triangle_cost().

    Parameters
    ----------
    t: list
    A range of numbers.
	
    row, col: int
    Location that will be used as the root

    Returns
    ------
    int
	lowest cost path cost.

    Raises
    ------
   	None
    '''
    if not row+1 > len(t)and not col+1 > len(t[row]):
        totalR = t[row][col] #starting right total
        totalL = t[row][col] #starting left total
        totalR += triangle_cost_impl(t, row, col+1)
        totalL += triangle_cost_impl(t, row+1, col)
        if totalR > totalL: #decides on which side is the lowest.
            return totalL
        else:
            return totalR
    else:
        return 0 #if there are no paths 0 will be added to the total.



