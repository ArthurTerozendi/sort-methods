import time

def selection_sort(array):
    inicio = time.time()
    movs = 0
    comps = 0

    for index in range(1, len(array)):
        min_index = index
        movs+=1
        comps+=1
        movs+=1
        for direita in range(index + 1, len(array)):
            comps+=1
            if array[direita] < array[min_index]:
                min_index = direita
        array[index], array[min_index] = array[min_index], array[index]
        movs+=1
    return comps, movs, time.time() - inicio
