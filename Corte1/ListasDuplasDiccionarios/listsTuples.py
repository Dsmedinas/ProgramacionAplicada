"""LISTAS"""

my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde'] #Crea una lista llamada 'my_lista'

print(my_lista) #Imprime la lista completa
print(type(my_lista))   #Muestra el tipo de dato de 'my_lista'
print(my_lista[2])  #Imprime el elemento en la posición 2 de la lista, teniendo en cuenta que inicia con la posición 0

'''s
print("my_lista size: ", len(my_lista)) #Muestra la cantidad de elementos de la lista
print(my_lista[0:2])    #Extrae e imprime una parte de la lista, los elementos 0 y 1 sin incluir el 2
print(my_lista[:2]) #Versión abreviada de la línea anterior cuando quieres extraer desde el elemento 0

my_lista.append('Blanco')      #Agrega un elemento al final de la lista ya creada
print(my_lista)

my_lista.insert(3, 'Negro')  #Inserta un elemento en una posición específica, en este caso la 3
print(my_lista)'''


my_lista.extend(['Marron', 'Gris'])   #Concatena la lista existente con la nueva
print(my_lista)

print(my_lista.index('Azul')) #Busca la posición del elemento que coincida con 'Azul' en la lista

#my_lista.remove('Magenta')
my_lista.remove('Marron') #Remueve el elemento 'Marron'
print(my_lista)

my_lista.insert(8, 'Marron')
print(my_lista)

print(my_lista.pop())
size = len(my_lista)
print("size = ", size)
#print(my_lista.pop(size))

my_lista_3 = my_lista*3
print("my_lista_3: ", my_lista_3)

print("Sort:")
print()
my_listaSort = my_lista.sort()
print(my_listaSort)

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")
my_NumList.sort()
print(my_NumList)
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList)



"""TUPLAS"""


#Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ", my_tupla)

print(my_tupla[0])
print(my_tupla[2])


#Evalua si un elemento está contenido en la tupla
print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)