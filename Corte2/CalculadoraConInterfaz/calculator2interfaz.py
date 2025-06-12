import tkinter as tk
from tkinter import messagebox
from calculator2fuentes import Operaciones

class CalculadoraApp:
    def __init__(self, root):
        self.operaciones = Operaciones()
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Variables
        self.entrada = tk.StringVar()
        self.operacion_actual = None
        self.primer_numero = None
        self.reiniciar = False
        
        # Diseño de la interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Pantalla de resultados
        pantalla = tk.Entry(self.root, textvariable=self.entrada, font=('Arial', 20), 
                          bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        pantalla.grid(row=0, column=0, columnspan=4, pady=10)
        
        # Botones numéricos
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('%', 5, 0)
        ]
        
        for (texto, fila, columna) in botones:
            if texto == '=':
                btn = tk.Button(self.root, text=texto, padx=20, pady=20, 
                               command=self.calcular_resultado, bg='lightblue')
            elif texto == 'C':
                btn = tk.Button(self.root, text=texto, padx=20, pady=20, 
                               command=self.limpiar, bg='orange')
            else:
                btn = tk.Button(self.root, text=texto, padx=20, pady=20, 
                               command=lambda t=texto: self.agregar_entrada(t))
            
            btn.grid(row=fila, column=columna, sticky='nsew')
            btn.config(font=('Arial', 15))
        
        # Configurar el tamaño de las filas y columnas
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def agregar_entrada(self, valor):
        if self.reiniciar:
            self.entrada.set('')
            self.reiniciar = False
        
        if valor in '+-*/%':
            self.primer_numero = float(self.entrada.get())
            self.operacion_actual = valor
            self.reiniciar = True
        else:
            current = self.entrada.get()
            self.entrada.set(current + valor)
    
    def calcular_resultado(self):
        try:
            segundo_numero = float(self.entrada.get())
            
            if self.operacion_actual == '+':
                resultado = self.operaciones.sumar(self.primer_numero, segundo_numero)
            elif self.operacion_actual == '-':
                resultado = self.operaciones.restar(self.primer_numero, segundo_numero)
            elif self.operacion_actual == '*':
                resultado = self.operaciones.multiplicar(self.primer_numero, segundo_numero)
            elif self.operacion_actual == '/':
                resultado = self.operaciones.dividir(self.primer_numero, segundo_numero)
            elif self.operacion_actual == '%':
                resultado = self.operaciones.modulo(self.primer_numero, segundo_numero)
            else:
                resultado = segundo_numero
            
            self.entrada.set(str(resultado))
            self.reiniciar = True
            self.operacion_actual = None
            
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida")
            self.limpiar()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.limpiar()
    
    def limpiar(self):
        self.entrada.set('')
        self.operacion_actual = None
        self.primer_numero = None
        self.reiniciar = False

