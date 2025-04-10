#Este código identifica números primos entre 0 y 30 y mide el tiempo que tarda en ejecutarse

import time
inicio = time.time()

for i in range(0,31):
    contador = 0 #Contador de divisores
    for n in range(1, i+1):
        residue = i%n
        if residue == 0:
            contador = contador + 1
              
    if contador == 2:
        print(f'{i} es un primo') #Verificación de números primos
        
fin = time.time()
print("t = ", (fin - inicio)*1000) #Medición del tiempo final