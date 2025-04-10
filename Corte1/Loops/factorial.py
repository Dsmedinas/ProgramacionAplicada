#Este código es un programa que calcula el factorial de un número positivo ingresado por el usuario.

while True:

    value = int(input("Ingresa un número entero positivo: "))
    print("Value: ", value)
    a = isinstance(value, int)
    if a == True and value > 0:
        fact = 1
        for i in range (1, value + 1):
            fact = fact*i            
        print(f'El factorial de {value} de: ', fact)
    else:
        print("Por favor, ingresa un número entero positivo")