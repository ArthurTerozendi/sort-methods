import time
import random


def insertion_sort( lista ):
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
    return comps, movs

def selection_sort(array):

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
    return comps, movs

def bubble_sort(lista):

    movs = 0
    comps = 0

    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        comps+=1
        for i in range(elementos):
            movs+=1
            if lista[i] > lista[i+1]:
                movs+=1
                comps+=1
                lista[i], lista[i+1] = lista[i+1],lista[i]

                ordenado = False

    return comps, movs

def run_insertion_sort(array):
    data = []
    inicio = time.time()
    data.append(insertion_sort(array))
    fim = time.time()
    tempo = fim - inicio
    data.append(tempo)
    return data

def run_selection_sort(array):
    data = []
    inicio = time.time()
    data.append(selection_sort(array))
    fim = time.time()
    tempo = fim - inicio
    data.append(tempo)
    return data

def run_bubble_sort(array):
    data = []
    inicio = time.time()
    data.append(bubble_sort(array))
    fim = time.time()
    tempo = fim - inicio
    data.append(tempo)
    return data

arquivo = open("entrada.txt","r")

infos = arquivo.read()

infos_formated = infos.split('\n')

metodo = infos_formated[0]
tamanho = infos_formated[1]
tipo = infos_formated[2]
arquivo.close()

def write_results_bubble():
    arquivo = open('resultados.txt', 'a')
    arquivo.truncate(0)
    arquivo.write(metodo)
    arquivo.write(" ")
    arquivo.write(tamanho)
    arquivo.write(" ")
    arquivo.write(tipo)
    arquivo.write(" ")
    arquivo.write("\n")
    arquivo.write("Comparacoes  Movimentacoes  Tempo")
    arquivo.write("\n")
    arquivo.write(str(run_bubble_sort(array)))
    arquivo.close()

def write_results_selection():
    arquivo = open('resultados.txt', 'a')
    arquivo.truncate(0)
    arquivo.write(metodo)
    arquivo.write(" ")
    arquivo.write(tamanho)
    arquivo.write(" ")
    arquivo.write(tipo)
    arquivo.write(" ")
    arquivo.write("\n")
    arquivo.write("Comparacoes  Movimentacoes  Tempo")
    arquivo.write("\n")
    arquivo.write(str(run_selection_sort(array)))
    arquivo.close()

def write_results_insertion():
    arquivo = open('resultados.txt', 'a')
    arquivo.truncate(0)
    arquivo.write(metodo)
    arquivo.write(" ")
    arquivo.write(tamanho)
    arquivo.write(" ")
    arquivo.write(tipo)
    arquivo.write(" ")
    arquivo.write("\n")
    arquivo.write("Comparacoes  Movimentacoes  Tempo")
    arquivo.write("\n")
    arquivo.write(str(run_insertion_sort(array)))
    arquivo.close()

def rand_quant():
    return 0.1


if(tamanho == '100'):
    array = list(range(0,100))

    if(tipo == 'OrdC'):
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

    elif(tipo == 'OrdD'):
        array.reverse()
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

    elif(tipo == 'OrdA'):
        random.shuffle(array)
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

    elif(tipo == 'OrdP'):
        random.shuffle(array,rand_quant)
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

elif(tamanho == '1000'):
    array = list(range(0,1000))

    if(tipo == 'OrdC'):
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

    elif(tipo == 'OrdD'):
        array.reverse()
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

    elif(tipo == 'OrdA'):
        random.shuffle(array)
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

    elif(tipo == 'OrdP'):
        random.shuffle(array,rand_quant)
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

elif(tamanho == '100000'):
    array = list(range(0,100000))

    if(tipo == 'OrdC'):
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

    elif(tipo == 'OrdD'):
        array.reverse()
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

    elif(tipo == 'OrdA'):
        random.shuffle(array)
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

    elif(tipo == 'OrdP'):
        random.shuffle(array,rand_quant)
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

elif(tamanho == '1000000'):
    array = list(range(0,1000000))

    if(tipo == 'OrdC'):
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

    elif(tipo == 'OrdD'):
        array.reverse()
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

    elif(tipo == 'OrdA'):
        random.shuffle(array)
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()

    elif(tipo == 'OrdP'):
        random.shuffle(array,rand_quant)
        if(metodo == 'Bubble'):
            write_results_bubble()
        elif(metodo == 'Select'):
            write_results_selection()
        elif(metodo == 'Insert'):
            write_results_insertion()
