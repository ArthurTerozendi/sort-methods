import time

def insertion_sort( lista ):
    inicio = time.time()
    comps = 0
    movs = 0
    for i in range( 1, len( lista ) ):
        chave = lista[i]
        k = i
        comps+=1
        movs+=1
        while k > 0 and chave < lista[k - 1]:
            lista[k] = lista[k - 1]
            movs+=1
            k -= 1
        lista[k] = chave
        movs+=1
    return comps, movs, time.time() - inicio