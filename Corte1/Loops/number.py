#Este código genera datos aleatorios y los visualiza usando la biblioteca Matplotlib

import random
from matplotlib import pyplot as plt # type: ignore

#
numeros_a = range(1, 13) #Crea un rango de números del 1 al 12 
numeros_b = [random.randint(1, 1000) for i in range(12)] #Genera una lista de 12 números aleatorios entre 1 y 1000
plt.plot(numeros_a, numeros_b)
plt.show() #Muestra la ventana con el gráfico generado