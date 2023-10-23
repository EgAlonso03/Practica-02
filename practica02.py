import random
import numpy as np
import matplotlib.pyplot as plt
import timeit

def quicksort(arreglo):
    if len(arreglo) <= 1:
        return arreglo
    else:
        pivote = sum(arreglo) / len(arreglo)
        menor = [x for x in arreglo if x < pivote]
        igual = [x for x in arreglo if x == pivote]
        mayor = [x for x in arreglo if x > pivote]
        return quicksort(menor) + igual + quicksort(mayor)

def arreglos(tamaño):
    return [random.randint(1, 100) for i in range(tamaño)]

num_arreglos = 100
longitud_Arreglos = [random.randint(1, 100) for i in range(num_arreglos)]
x_valores = []
y_valores = []

for i, tamaño in enumerate(longitud_Arreglos, 1):
    arreglo = arreglos(tamaño)
    print(f"Arreglo {i} original de tamaño {tamaño}: {np.array(arreglo)}")
    time = timeit.timeit(lambda: quicksort(arreglo), number=1000)  
    x_valores.append(tamaño)
    y_valores.append(time)
    print(f"Arreglo {i} ordenado de tamaño {tamaño}: {np.array(quicksort(arreglo))}")
    print(f"Tardó {time} segundos en ordenarse.")

plt.plot(x_valores)
plt.xlabel('Longitud del arreglo')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución para los arreglos')
plt.show()
