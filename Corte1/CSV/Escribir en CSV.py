import csv

#Datos que se quieren guardar
datos = [
    ["Nombre", "Edad", "Ciudad"],  # Encabezados
    ["Ana", 28, "Bogotá"],
    ["Carlos", 35, "Boyacá"],
    ["Luisa", 22, "Cali"]
]

#Nombre del archivo CSV
nombre_archivo = "ejemplo1.csv"

#Escribe en CSV
with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
    writer = csv.writer(archivo)
    writer.writerows(datos)

print(f"Archivo '{nombre_archivo}' archivo creado")