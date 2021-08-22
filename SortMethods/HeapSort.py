import random
import time
def heap_sort(array):
    count = 0;
    mov = 0;
    n = len(array)
    init = time.time()
    for i in range(n//2 - 1, -1, -1):
        mov, count = create_heap(array, i, n, mov, count)

    for i in range(n-1, 0, -1):
        mov += 2
        array[i], array[0] = array[0], array[i]
        mov, count = create_heap(array, 0, i, mov, count)
    
    return count, mov, time.time() - init

def create_heap(array, init, final, mov, count):
    largest = init
    left = 2 * init + 1     
    right = 2 * init + 2     
    
    count += 2
    if left < final and array[largest] < array[left]:
        mov += 1
        largest = left
    
    count += 2
    if right < final and array[largest] < array[right]:
        mov += 1
        largest = right
    
    count += 1
    if largest != init:
        mov += 2
        array[init], array[largest] = array[largest], array[init]  
        create_heap(array, largest, final, mov, count)
    
    return mov, count;
