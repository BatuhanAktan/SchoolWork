'''
This module provides functions for the 1-dimensional Game of Life.

The 1-dimensional Game of Life occurs on a list of cells where each
cell is either alive or dead. The population of cells evolves from
one generation to the next according to three rules:

1. Any live cell survives into the next generation if it has 2 or 4
living neighbours in its 2-neighborhood.
2. Any dead cell becomes alive in the next generation if it has 2 or 3
living neighbours in its 2-neighborhood.
3. All other live cells die and all other dead cells remain dead.

The rules are applied to each cell simultaneously to compute the
next generation of cells.

The 2-neighborhood of a cell consists of the cell itself and its
two neighbors to the left and two neighbors to the right of the cell
(if those neighbors exist).

Author: Dr. Burton Ma
Edited by: Batuhan Aktan
Student Number: 20229360
Date:  March 2021

'''


def make_cells(n, val):
    '''
    Return a list filled with a specified value.

    Parameters
    ----------
    n : int
        The number of elements in the returned list.
    val : bool
        The element to appear repeatedly in the returned list.

    Returns
    -------
    list
        A list of `n` copies of `val`

    Raises
    ------
    ValueError
        If `n` is less than zero.
    '''
    
    if n < 0:
        raise ValueError('make_cells() number of elements less than zero, n = ' + str(n))
    a = [val] * n
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
    gen = "" #creates empty string
    for i in cells:
        if i:
            gen+= "#" # adds "#" if value is true
        else:
            gen+= "-" # adds "-" if value is false

    print(gen)


def neighborhood(cells,index):
    '''
    Checks the neighborhood of a cell at a specific index.

    Parameters
    ----------
    cells : list 
        The list containing the status of cells.
    index: int
        The index of the cell which will be checked for
        neighborhood conditions.

    Returns
    -------
    neighbors: list
        A list containing the segment of cells list at index
        with the neighbors

    Raises
    ------
    ValueError
        if 'index' is less than 0
    '''

    if index < 0:
        raise ValueError('neighborhood() index is less than zero, index = '\
         + str(index))

    if len(cells)-2 >= index >= 2: #makes sure that 5x1 can be taken.
         neighbors = cells[index-2:index+3]

    elif len(cells)-2 < index: # takes into consideration its at most left
        neighbors = cells[index-2:]

    elif index < 2: # takes into consideration that its at most right
        neighbors = cells[:index+3]

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
    if len(cells) <= 0:
        raise ValueError('cells list is empty, cells = ' + str(cells))

    nextGen = []

    for i in range(len(cells)):
        # checks for the rules if the cell is alive
        if cells[i]:

            if neighborhood(cells, i).count(True)-1 == 2 or \
            neighborhood(cells, i).count(True)-1 == 4: # does not count itself thus -1
                nextGen.append(True)

            else:
                nextGen.append(False)
        elif not cells[i]:

            if neighborhood(cells, i).count(True) == 2 or \
            neighborhood(cells, i).count(True) == 3:
                nextGen.append(True)

            else:
                nextGen.append(False)

        else:
            
            nextGen.append(False)

    for i in range(len(cells)):
        cells[i] = nextGen[i]


def blinker(cells, index):
    '''
    Inserts blinker pattern into the given cells.

    Parameters
    ----------
    cells : list 
        The list containing the status of cells.
    index : int
        The index which the pattern will be insterted
        at.

    Returns
    -------
    None, c is changed

    Raises
    ------
    ValueError
        if 'index' is lesser than 0

    Exeption
        if blinker pattern cannot be inserted
        at the given index.

    '''

    if index < 0:
        raise ValueError('blinker() index less than zero, index = '\
         + str(index))

    blinkerPattern = [False, False, True, True, False, False]

    if len(cells[index:]) < 6: #checking if pattern fits
        raise Exception('blinker() pattern cannot fit, index = '\
         + str(index))

    newCells = cells[:index]+blinkerPattern+cells[index+6:] #inserting blinker pattern
    
    for i in range(len(cells)):
        cells[i] = newCells[i]
