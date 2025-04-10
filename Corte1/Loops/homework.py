#Este código realiza operaciones con dos números ingresados por el usuario y compara sus valores y tipos.

a = input("Ingresa un número a: ")
a = int(a)
b = input("Ingresa un número b: ")
b = float(b)
c = a + b

#Compara si los valores son iguales (aunque sean de tipos diferentes)
if a == b:
    print("Igual")
else:
    print("Diferente")

print("El tipo de a es: ", type(a))
print("El tipo de b es: ", type(b))
print("c = ", c)

#En este caso siempre serán diferentes porque a es int y b es float
if type(a) == type(b):
    print("a and b son del mismo tipo")
else:
    print("a and b son de diferente tipo")