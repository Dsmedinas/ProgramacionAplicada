#Este código es una versión interactiva que permite al usuario verificar números primos múltiples veces.

a = 1
value = input('Ingrese un valor')
value = int(value) #Pide el valor al usuario

while a == 1:
    for i in range(1,value+1): #Proceso para identificar numeros primos
        contador = 0
        for n in range(1, i+1):
            residuo = i%n
            if residuo == 0:
                contador = contador + 1
            
            # print("i = ", i)
            # print("n = ", n)
            # print("residuo = ", residuo)
            # print("contador = ", conta)
    if contador == 2:
       print(f'{i} es un primo')
       print("\n")
    else:
       print(f'{i} No es un primo')
       print("\n")

    print('Quiere continuar?. Ingrese 1 para hacerlo') #Si ingresa 1, repite el proceso con nuevo valor
    a = input()
    a = int(a)

    if a != 1:
        break

    value = input('Ingrese un valor') #Repite el proceso con un nuevo valor dado por el usuario
    value = int(value)