
import random
import time

def shell_sort(array):
    mov = 0
    count = 0   

    start = time.time();
    gap = len(array)//2
    while gap > 0:
        count += 1
        for i in range(gap):
            for j in range(i+gap, len(array), gap):
                currValue = array[j]
                
                while j >= gap and array[j - gap] > currValue:
                    mov += 1
                    count += 2
                    array[j] = array[j-gap]
                    j = j - gap
                
                mov += 1
                array[j] = currValue
        gap = gap // 2

    return array, time.time() - start, mov, count

array = list(range(0,1000000))
random.shuffle(array) 
print(array)
print()
print(shell_sort(array))
