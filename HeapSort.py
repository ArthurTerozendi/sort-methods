import random
import time
def heap_sort(array):
    n = len(array)
    init = time.time()
    for i in range(n//2 - 1, -1, -1):
        create_heap(array, i, n)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        create_heap(array, 0, i)
    
    return array, time.time() - init

def create_heap(array, init, final):
    largest = init
    left = 2 * init + 1     
    right = 2 * init + 2     
 
    if left < final and array[largest] < array[left]:
        largest = left
    
    if right < final and array[largest] < array[right]:
        largest = right
    
    if largest != init:
        array[init], array[largest] = array[largest], array[init]  
        create_heap(array, largest, final)

array = list(range(0,1000000))
random.shuffle(array) 
print(array)
print()
print(heap_sort(array))
