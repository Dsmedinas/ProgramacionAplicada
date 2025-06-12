class Operaciones:               #creamos una clase llamada Calculator que agrupará todas las funciones de la calculadora
 
    def sumar(self, a, b):            #Recibe dos números (a y b) y devuelve la suma
        return a+b            #suma los parámetros y devuelve el resultado

    def restar(self, a, b):          #Recibe dos números (a y b) y devuelve la resta
        return a-b            #resta los parámetros y devuelve el resultado

    def multiplicar(self, a, b):           #Recibe dos números (a y b) y devuelve la multiplicación
        return a*b            #multiplica los parámetros y devuelve el resultado

    def dividir(self, a, b):         #recibe dos números (a y b) y devuelve su división
        try:                        #con try: se intenta ejecutar a / b
            return a/b                  #se puede usar // para que arroge el resultado entero
        except ZeroDivisionError:       #si b es cero, Python lanza la excepción ZeroDivisionError
            return "Error: no se puede dividir por cero"

    def modulo(self, a, b):         #devuelve el residuo de la división (a % b)
        return a % b    