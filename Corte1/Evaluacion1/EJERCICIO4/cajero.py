class MovimientosBancarios:
    def __init__(self):
        self.saldo = 0.0 #Saldo como una variable float
        self.contraseña_correcta = "2025"  

    def depositar(self, cantidad):
        try:
            cantidad = float(cantidad) #cantidad como una variable tipo float
            if cantidad <= 0:
                return "Error: La cantidad a depositar debe ser positiva"
            self.saldo = self.saldo + cantidad  
            return f"Depósito exitoso. El saldo actual es de: {self.saldo:.2f}" #Mostrar el saldo con 2 decimales
        except ValueError: #Excepción al no ingresar un valor numérico
            return "Error: Ingrese un valor numérico válido"

    def retirar(self, cantidad):
        try:
            cantidad = float(cantidad)
            if cantidad <= 0:
                return "Error: La cantidad a retirar debe ser positiva"     #en caso de poner un valor negativo
            if cantidad > self.saldo:
                return "Error: Saldo insuficiente"      #en caso de querer retirar más de lo que hay de saldo
            self.saldo = self.saldo - cantidad
            return f"Retiro exitoso. El saldo actual es de: {self.saldo:.2f}"
        except ValueError:      #Excepción al no ingresar un valor numérico
            return "Error: Ingrese un valor numérico válido"

    def consultar_saldo(self):
        return f"Su saldo actual es: {self.saldo:.2f}"

    def autenticar(self):   
        intentos = 3    #En este caso el usuario tiene 3 intentos para ingresar
        while intentos > 0:
            contraseña = input("Ingrese la contraseña para acceder al cajero: (LA CONTRASEÑA ES: 2025)")
            if contraseña == self.contraseña_correcta:
                return True
            else:
                intentos = intentos - 1
                print(f"Contraseña incorrecta. Le quedan {intentos} intentos.")
        print("Ha excedido el número máximo de intentos. Acceso denegado")
        return False

    def ejecutar_cajero(self):
        if self.autenticar():
            while True:
                print("\n---BIENVENIDO al Cajero Automático ---")       #Menú cajero
                print("¿Qué desea realizar?")
                print("1. Depositar dinero")
                print("2. Retirar dinero")
                print("3. Consultar saldo")
                print("4. Salir")

                opcion = input("Seleccione una opción (1-4): ")

                if opcion == "1":
                    cantidad = input("Ingrese la cantidad a depositar: ")
                    print(self.depositar(cantidad))
                elif opcion == "2":
                    cantidad = input("Ingrese la cantidad a retirar: ")
                    print(self.retirar(cantidad))
                elif opcion == "3":
                    print(self.consultar_saldo())
                elif opcion == "4":
                    print("Gracias por usar nuestro cajero.")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")