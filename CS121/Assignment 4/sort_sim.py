'''
Demonstration of time complexities using sorting algorithms.

Author: Dr. Burton Ma
Edited by: Batuhan Aktan
Student Number: 20229360
Date:  April 2021
'''
import random
import time
import a4

def time_to_sort(sorter, t):
    '''
    Returns the times needed to sort lists of sizes sz = [1024, 2048, 4096, 8192]
    
    The function sorts the slice t[0:sz] using the sorting function
    specified by the caller and records the time required in seconds.
    Because a slice is sorted instead of the list t, the list t is not modified by
    this function. The list t should have at least 8192 elements.

    The times are returned in a list of length 4 where the times in seconds
    are formatted strings having 4 digits after the decimal point making it easier to
    print the returned lists.

    Parameters
    ----------
    sorter : function
             A sorting function from the module a4.
    t : list of comparable type
        A list of elements to slice and sort.

    Returns
    -------
    list of str
        The times to sort lists of lengths 1024, 2048, 4096, and 8192.

    Raises
    ------
    ValueError
        If len(t) is less than 8192.
    '''
    if len(t) < 8192:
        raise ValueError('not enough elements in t')
    times = []
    for sz in [1024, 2048, 4096, 8192]:
        # slice t
        u = t[0:sz]
        # record the time needed to sort
        tic = time.perf_counter()
        sorter(u)
        toc = time.perf_counter()
        times.append(f'{toc - tic:0.4f}')
    return times

list8192 = list(range(8192))

def sim_sorted():

	print(time_to_sort(a4.selection_sort, list8192), "Selection Sort")
	print(time_to_sort(a4.insertion_sort, list8192), "Insertion Sort 1")
	print(time_to_sort(a4.insertion_sort2, list8192), "Insertion Sort 2")
	print(time_to_sort(a4.merge_sort, list8192), "Merge Sort")

def sim_partial():

	a4.partial_shuffle(list8192)

	print(time_to_sort(a4.selection_sort, list8192), "Selection Sort")
	print(time_to_sort(a4.insertion_sort, list8192), "Insertion Sort 1")
	print(time_to_sort(a4.insertion_sort2, list8192), "Insertion Sort 2")
	print(time_to_sort(a4.merge_sort, list8192), "Merge Sort")


def sim_reverse():

	list8192.reverse()

	print(time_to_sort(a4.selection_sort, list8192), "Selection Sort")
	print(time_to_sort(a4.insertion_sort, list8192), "Insertion Sort 1")
	print(time_to_sort(a4.insertion_sort2, list8192), "Insertion Sort 2")
	print(time_to_sort(a4.merge_sort, list8192), "Merge Sort")

def sim_shuffled():
	
	random.shuffle(list8192)

	print(time_to_sort(a4.selection_sort, list8192), "Selection Sort")
	print(time_to_sort(a4.insertion_sort, list8192), "Insertion Sort 1")
	print(time_to_sort(a4.insertion_sort2, list8192), "Insertion Sort 2")
	print(time_to_sort(a4.merge_sort, list8192), "Merge Sort")
	
sim_shuffled()
sim_reverse()
sim_partial()
sim_sorted()
