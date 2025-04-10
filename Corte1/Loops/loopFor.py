#Este código utiliza un bucle para iterar sobre una cadena de texto
import time

cadena = 'Python'

#La letra 't' no se imprimirá, el uso de continue hace que cuando el bucle encuentra la 't', salte inmediatamente a la siguiente iteración
for letra in cadena:
   if letra == 't':
      continue
   print(letra)
   time.sleep(1)
