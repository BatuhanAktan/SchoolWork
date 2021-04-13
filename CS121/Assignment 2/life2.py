'''
This module provides functions for the 2-dimensional Game of Life.

The 2-dimensional Game of Life occurs on an n-by-n array of
cells where each cell is either alive or dead. The population of cells
evolves from one generation to the next according to three rules:

1. Any live cell survives into the next generation if it has 2 or 3
living neighbours in its 1-neighborhood (the cell itself does not
count towards the number of living neighbors).
2. Any dead cell becomes alive in the next generation if it has 3
living neighbours in its 1-neighborhood.
3. All other live cells die, and all other dead cells remain dead.

The rules are applied to each cell simultaneously to compute the
next generation of cells.

The 1-neighborhood of a cell consists of the cell itself and its
eight neighbours, which are the cells that are horizontally, vertically,
or diagonally adjacent (if those neighbors exist).

Author: Dr. Burton Ma
Edited by: Batuhan Aktan
Student Number: 20229360
Date:  March 2021
'''

import math
import sys


def test_indexes(cells, row, col, func_name):
    '''
    Test if row and column indexes are valid for a square array.

    This function tests if `row` and `col` are both in the
    range 0 to (n - 1), inclusive, where n is equal to
    len(cells). Raises a ValueError if an index is out of
    range.

    Parameters
    ----------
    cells : list-of-list of bool
        The n-by-n cells of a 2D Game of Life.
    row : int
        A row index for cells.
    col : int
        A column index for cells.
    func_name : str
        The name of the function that called test_indexes

    Raises
    ------
    ValueError
        If `row` or `col` is out of range.
    '''
    n = len(cells)
    if row < 0:
        raise ValueError(func_name, 'number of rows < 0, row = ', row)
    elif row >= n:
        raise ValueError(func_name, 'number of rows >= len(cells), row = ', row)
    if col < 0:
        raise ValueError(func_name, 'number of cols less than zero, col = ', col)
    elif col >= n:
        raise ValueError(func_name, 'number of cols >= len(cells), col = ', col)


def make_cells(rows, cols, val):
    '''
    Return an array filled with a specified value.

    Parameters
    ----------
    rows : int
        The number of rows in the array.
    cols : int
        The number of columns in the array.
    val : bool
        The element to appear repeatedly in the returned list.

    Returns
    -------
    list
        A list-of-lists of `rows`-by-`cols` copies of `val`

    Raises
    ------
    ValueError
        If `rows` or `cols` is less than zero.
    '''
    if rows < 0:
        raise ValueError('make_cells() size less than zero, rows = ', rows)
    if cols < 0:
        raise ValueError('make_cells() size less than zero, cols = ', cols)
    a = []
    for i in range(0, rows):
        row = [val] * cols
        a.append(row)
    return a


def print_cells(cells):
    '''
    Prints the given list of cells with # representing alive and - representing dead

    Parameters
    ----------
    cells : list
        The list containing the status of cells.

    Returns
    -------
    None

    Raises
    ------
    None
    '''
    for element in cells:
        line =""
        for i in element:
            if i:
                line+= "#"
            else:
                line+= "-"
        print(line)


def neighborhood(cells, row, col):
    '''
    Checks the neighborhood of a cell at a specific index.

    Parameters
    ----------
    cells : list 
        The list containing the status of cells.
    row, col: int
        The location of the cell which will be checked for
        neighborhood conditions.

    Returns
    -------
    neighbors: list
        A 2 dimensional list containing the segment of cells list at index
        with neighbors

    Raises
    ------
    ValueError
        if 'row' or 'col' is less than 0
    '''
    neighbors =[]

    if row < 0 or col < 0:
         raise ValueError('neighborhood() row or col is less than 0, row, col = '\
         + str(row)+','+str(col))
        
    test_indexes(cells, row, col, "neighborhood()")

    #creating upper and lower bound for rows and cols.
    if col + 2 > len(cells):  #checking if the col would exceed the cells len
        CUpBound = None
        CLowBound = col-1
    elif col - 2 < 0: # checking if the col is close to the left border
        CLowBound = None
        CUpBound = col+2
    else:	# regular 3x3 neighborhood
        CLowBound = col-1
        CUpBound = col+2
    if row + 2 > len(cells[1]):
        RUpBound = None
        RLowBound = row-1
    elif row - 2 < 0: 
        RUpBound = row+2
        RLowBound = None
    else: # regular vertical segment
        RUpBound = row+2
        RLowBound = row-1

    rowSeg = cells[RLowBound:RUpBound]
    for i in rowSeg:
        neighbors.append(i[CLowBound:CUpBound]) #adds all the neighboring parts creates a 3x3

    return neighbors


def evolve(cells):
    '''
    Creates the next generation of cells according 
    to the rules.

    Parameters
    ----------
    cells : list 
        The list containing the status of cells.

    Returns
    -------
    None, changes c

    Raises
    ------
    ValueError
        if 'cells' is empty
    '''
    if len(cells) < 0:
        raise ValueError('evolve() cells list is empty, cells = ' + str(cells))

    newCells = []

    for i in range(len(cells)): #iterates through cells
        newRow = []
        for j in range(len(cells[1])):
            if cells[i][j]:

                total = 0 # total number of alive neighbours

                for k in neighborhood(cells, i, j):

                    total += k.count(True) # counts living neighbours


                if total-1 == 2 or total-1 == 3: #checks rules and -1 to not count itself

                   newRow.append(True) 

                else:

                    newRow.append(False)

            elif not cells[i][j]:
                total = 0 # total number of alive neighbours

                for k in neighborhood(cells, i, j):
                    total += k.count(True) # counts living neighbours

                if total == 3:
                    newRow.append(True)

                else:
                    newRow.append(False)

        newCells.append(newRow)

    for i in range(len(cells)):
        for j in range(len(cells[1])):
            cells[i][j] = newCells[i][j] # updates cells


def glider(cells, top_row, left_col):
    '''
    Inserts glider pattern into the given cells.

    Parameters
    ----------
    cells : list 
        The list containing the status of cells.
    top_row, left_col : int
        The location in which the pattern will be insterted
        at.

    Returns
    -------
    None, changes c.

    Raises
    ------
    ValueError
        if 'top_row' or 'left_col' is lesser than 0

    Exeption
        if glider pattern cannot be inserted
        at the given index.

    '''
    if top_row < 0 or left_col < 0:
         raise ValueError('glider() top_row or left_col is less than 0, top_row, left_col = '\
         + str(top_row)+','+str(left_col))
        
    test_indexes(cells, top_row, left_col, "glider()")
    
    pattern = [[False,False,False,False,False],
               [False,True,False,False,False],
               [False,False,True,True,False],
               [False,True,True,False,False],
               [False,False,False,False,False]]

    if top_row+5 <= len(cells) and left_col+5 <= len(cells[1]): #checking if the pattern would fit.
        for i in range(5):
            cells[top_row+i] = cells[top_row+i][:left_col]\
            +pattern[i]+cells[top_row+i][left_col+5:] # inserts the pattern

    else:
        raise Exception('glider() pattern cannot fit, top_row, left_col = '\
         + str(top_row)+','+str(left_col)) # if glider pattern can't fit raises exception.

