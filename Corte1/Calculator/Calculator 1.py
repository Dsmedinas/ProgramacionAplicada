#self permite acceder a los atributos y métodos de la clase

class Operaciones:               # Creamos una clase llamada Calculator que agrupará todas las funciones de la calculadora
 
    def sumar(self, a, b):            #Recibe dos números (a y b) y devuelve su suma
        return a + b            #suma los parámetros y devuelve el resultado

    def restar(self, a, b):          #Recibe dos números (a y b) y devuelve su resta
        return a - b            #resta los parámetros y devuelve el resultado

    def multiplicar(self, a, b):           #Recibe dos números (a y b) y devuelve su multiplicación
        return a * b            #multiplica los parámetros y devuelve el resultado

    def dividir(self, a, b):         #Recibe dos números (a y b) y devuelve su división
        try:                        #con try: se intenta ejecutar a / b
            return a / b        
        except ZeroDivisionError:       #Si b es cero, Python lanza la excepción ZeroDivisionError
            return "Error: No se puede dividir por cero"

    def modulo(self, a, b):         #Devuelve el residuo de la división (a % b)
        return a % b            #aplica el módulo con los parámetros y devuelve el resultado

#Ejemplos
if __name__ == "__main__":          #Ejecuta este código solo si el archivo se usa directamente, no cuando otro lo importe
    opera = Operaciones()           #Crea un objeto "opera" de la clase Operaciones para usar sus funciones
    print(opera.sumar(5, 7))
    print(opera.restar(45, 11))
    print(opera.multiplicar(3, 2))
    print(opera.dividir(10, 0))      # Esto mostrará el mensaje de error con la división
    print(opera.dividir(100, 5))      # Esto mostrará el mensaje de error con la división
    print(opera.modulo(999,15))  