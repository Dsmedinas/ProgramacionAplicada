import random #Para simular los datos de entrada con valores aleatorios
import csv #Para leer y escribir archivos en formato CSV
import time #Controla intervalos de tiempo
import signal #se buscó para manejar señales o comandos como el ctr+c
import sys #Se buscó para interactuar con el sistema
from threading import Thread #Para ejecutar la escritura y lectura en conjunto sin bloquearse

#Configuración
CSV_FILE = "numeros_random.csv"
intervalo_escribir = 0.5 #segundos
intervalo_leer = 0.5 #segundos

#ctrl+c para detener el programa
def signal_handler(sig, frame):
    print("\nDeteniendo el programa")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler) # Capturar la señal SIGINT que se envía al presionar Ctrl+C en el terminal y ejecuta una función personalizada en vez de terminar el programa abruptamente

'''FUNCIÓN DE ESCRIBIR'''
def escribir_csv():
    #Escribe números aleatorios en el CSV indefinidamente 
    with open(CSV_FILE, mode='w', newline='') as file: #Con 'with' nos aseguramos que el archivo se cierre automáticamente al terminar
        writer = csv.writer(file) #Crea un objeto writer para escribir datos en formato CSV
        writer.writerow(['Numero'])  #Escribe la primera línea del CSV con la columna llamada "Numero"

    while True:
        with open(CSV_FILE, mode='a', newline='') as file: #Se usa mode='a' para no sobrescribir datos existentes
            writer = csv.writer(file)
            writer.writerow([random.random()])
        time.sleep(intervalo_escribir) #Pausa el bucle con el tiempo puesto arriba
        
'''FUNCIÓN DE LEER'''
def leer_csv():
    #Lee el archivo CSV y muestra solo el último valor en el terminal
    while True:
        try:    ##Para arbrir el archivo en modo lectura, pide agregar al menos una excepción
            with open(CSV_FILE, mode='r') as file:
                reader = csv.reader(file)   #Se crea un objeto para leer el archivo CSV línea por línea
                ultima_linea = list(reader)[-1] #Convierte el lector en una lista y toma el número de la última línea 
                print(f"\rÚltimo valor: {ultima_linea[0]}", end='', flush=True) #Imprime el número en el terminal
        except (IndexError, FileNotFoundError):
            pass
        time.sleep(intervalo_leer) #Pausa el bucle con el tiempo puesto arriba

#Se buscó esta función para ejecutar la escritura y lectura en conjunto
Thread(target=escribir_csv, daemon=True).start()
Thread(target=leer_csv, daemon=True).start()

#Mantiene el programa en ejecución con un bucle hasta que se presione ctrl+c

try : #Para arbrir el archivo en modo lectura
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass