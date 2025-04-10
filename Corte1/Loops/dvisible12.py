#Este código imprime todos los números entre 100 y 300 que son divisibles por 12

#Bucle que itera todos los números enteros desde 100 hasta 300
#Si el residuo no es igual a 0, ejecuta continue, lo que hace que el bucle salte a la siguiente iteración sin ejecutar el código restante
#Si el resto es igual a 0, no ejecuta el continue y pasa a la siguiente línea para imprimir el número
for i in range(100, 301):
    if (i%12) != 0:
        continue
    print(i)