
import random
import time

def shell_sort(array):
    start = time.time();
    gap = len(array)//2
    while gap > 0:
        for i in range(gap):
            for j in range(i+gap, len(array), gap):
                currValue = array[j]
                
                while j >= gap and array[j - gap] > currValue:
                    array[j] = array[j-gap]
                    j = j - gap
                
                array[j] = currValue
        gap = gap // 2
    end  = time.time();
    totalTime = end - start
    return array, totalTime

array = list(range(0,1000000))
random.shuffle(array) 
print(array)
print()
print(shell_sort(array))
