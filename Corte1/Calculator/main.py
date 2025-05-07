#Ejemplos
from calculadora import Operaciones

opera = Operaciones()      

# Llamar a la función
print(opera.sumar(6, 7))
print(opera.restar(45, 11))
print(opera.multiplicar(3, 2))
print(opera.dividir(10, 0))      #este ejemplo mostrará el mensaje de error con la división
print(opera.dividir(100, 5))      
print(opera.modulo(999,15))  