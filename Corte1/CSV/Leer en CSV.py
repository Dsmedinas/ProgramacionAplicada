import csv

#Nombre del archivo CSV(el mismo que se arrojó antes al escribir en CSV)
nombre_archivo = "ejemplo1.csv"

#Lee el archivo CSV
with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:  
        print(fila)  