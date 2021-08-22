import time

def bubble_sort(lista):
    inicio = time.time()
    movs = 0
    comps = 0

    elementos = len(lista)-1

    for j in range(elementos):
        comps+=1
        for i in range(elementos-1):
            movs+=1
            if lista[i] > lista[i+1]:
                movs+=1
                comps+=1
                lista[i], lista[i+1] = lista[i+1],lista[i]
    return comps, movs, time.time() - inicio