#Identificar números pares e impares de 1 a 20
'''for i in range (1,21):
     residual = i%2
     if residual == 0:
         print(f'{i} es par')
     else:
         #print(f'{i} es impar')
         print(str(i) + ' es impar')'''

#Números elevados al cubo
'''for i in range (0,6):
     result = i**3
     print(result)'''

#Entrada de usuario y bucle NÚMERO DE VECES
times = input("Ingresa un número de veces: ")
times = float(times)
times = int(times)
print(type(times))
print(times)

if times == 0:
    print("No hagas nada")
else:
    for i in range(1,times+1):
        print("i = ", i)