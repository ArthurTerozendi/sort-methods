import time
import random
from BubbleSort import bubble_sort
from InsertionSort import insertion_sort
from SelectionSort import selection_sort
from HeapSort import heap_sort
from QuickSort import quick_sort
from ShellSort import shell_sort

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
    arquivo.write("Tempo: " + str(results[2]))
    arquivo.close()

def rand_quant(tam):
    t = int(tam * 0.1);
    arr = (list(range(0,int(tam - t))))
    rArr = (list(range(0, int(tam * 0.1))))
    random.shuffle(rArr);
    arr.extend(rArr);
    return arr;

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
    array = rand_quant(int(tamanho))

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
