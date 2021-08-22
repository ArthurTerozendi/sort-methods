import random
import time

def quick_sort(array, first, last, mov, count):
    init = time.time();
    
    count += 1
    if first < last:
        splitpoint, mov, count = partition(array, first, last, mov, count)

        quick_sort(array, first, splitpoint - 1, mov, count)
        quick_sort(array, splitpoint + 1, last, mov, count)

    return count, mov, time.time() - init


def partition(array, first, last, mov, count):
    pivot = array[first]

    f = first

    first = first + 1
    last = last

    done = False
    while not done:

        while first <= last and array[first] <= pivot:
            count += 2
            first = first + 1

        while array[last] >= pivot and last >= first:
            count += 2
            last = last -1

        if last < first:
            count += 1
            done = True
        else:
            mov += 2
            array[first], array[last] = array[last], array[first]

    mov += 2
    array[f], array[last] = array[last], array[f]


    return last, mov, count
