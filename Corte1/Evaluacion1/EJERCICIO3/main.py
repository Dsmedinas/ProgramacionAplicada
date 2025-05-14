#Ejemplos
from calculator2fuentes import Operaciones # type: ignore

opera = Operaciones()      

# Llamar a la función
print(opera.sumar(16, 23))
print(opera.restar(33, 11))
print(opera.multiplicar(88, 2))
print(opera.dividir(4, 0))      #este ejemplo mostrará el mensaje de error con la división
print(opera.dividir(100, 25))      
print(opera.modulo(170,15))  