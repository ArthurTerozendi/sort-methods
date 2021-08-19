import random
import time

def quick_sort(array, first, last):
    init = time.time();
    
    if first < last:
        splitpoint = partition(array, first, last)

        quick_sort(array, first, splitpoint - 1)
        quick_sort(array, splitpoint + 1, last)

    final = time.time();
    return array, final - init


def partition(array, first, last):
    pivot = array[first]

    f = first

    first = first + 1
    last = last

    done = False
    while not done:

        while first <= last and array[first] <= pivot:
            first = first + 1

        while array[last] >= pivot and last >= first:
            last = last -1

        if last < first:
            done = True
        else:
            temp = array[first]
            array[first] = array[last]
            array[last] = temp

    temp = array[f]
    array[f] = array[last]
    array[last] = temp


    return last

array = list(range(0,1000000))
random.shuffle(array) 
print(array)
print()
print(quick_sort(array, 0, len(array) - 1))
