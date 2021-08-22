import time
import random
from HeapSort import heap_sort
from QuickSort import quick_sort
from ShellSort import shell_sort

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

def write_results(results):
    arquivo = open('resultados.txt', 'a')
    arquivo.truncate(0)
    arquivo.write(metodo)
    arquivo.write(" ")
    arquivo.write(tamanho)
    arquivo.write(" ")
    arquivo.write(tipo)
    arquivo.write(" ")
    arquivo.write("\n")
    arquivo.write("Comparacoes: " + str(results[0]))
    arquivo.write("\n")
    arquivo.write("Movimentacoes: " + str(results[1]))
    arquivo.write("\n")
    arquivo.write("Tempo: " + str(results[2]) + "s")
    arquivo.close()

def rand_quant():
    return 0.1

arquivo = open("entrada.txt","r")

infos = arquivo.read()

infos_formated = infos.split('\n')

metodo = infos_formated[0]
tamanho = infos_formated[1]
tipo = infos_formated[2]
arquivo.close()

array = list(range(0,int(tamanho)))

if(tipo == 'OrdD'):
    array.reverse()
elif(tipo == 'OrdA'):
    random.shuffle(array)
elif(tipo == 'OrdP'):
    random.shuffle(array,rand_quant)

if(metodo == 'Bubble'):
    write_results(bubble_sort(array))
elif(metodo == 'Select'):
    write_results(selection_sort(array))
elif(metodo == 'Insert'):
    write_results(insertion_sort(array))
elif(metodo == 'Shell'):
    write_results(shell_sort(array))
elif(metodo == 'Quick'):
    write_results(quick_sort(array, 0, len(array) - 1, 0, 0))
elif(metodo == 'Heap'):
    write_results(heap_sort(array))
