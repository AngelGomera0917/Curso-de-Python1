#Tuplas
print("\n")

# Una tupla es inmutable, osea que no se puede modificar al igual que las listas.

my_tupla = tuple()

my_tupla = (1,7, "Gomera" ,5, "Angel", 9, 6)

print(my_tupla)

print(type(my_tupla))

print("\n")

print(my_tupla.index(7)) # Busca el valor 7 en la tupla y devuelve su posición.

print(my_tupla.count(5)) # Cuenta cuantas veces se repite el valor 5 en la tupla.

print(my_tupla[2:5]) # Imprime los valores de la posición 2 a la 5.

print(my_tupla[2:]) # Imprime los valores de la posición 2 hasta el final.

print(my_tupla[::-1]) # Invierte la tupla.

print(my_tupla[::2]) # Imprime los valores de la tupla de 2 en 2.

print(my_tupla[1::2]) # Imprime los valores de la tupla de 2 en 2 desde la posición 1.

print(my_tupla[:-1]) # Imprime los valores de la tupla desde el principio hasta el penúltimo.

print("\n")

print(type(my_tupla))

my_tupla = list(my_tupla) # Convierte la tupla en una lista, para poder modificarla. por esto python es de tipado dinámico.
print(type(my_tupla))

my_tupla.append("Romero") # Ahora si la puedo modificar porque la converti en lista.
print(my_tupla)

my_tupla = tuple(my_tupla) # Convierto la lista en una tupla nuevamente, para no poder modificarla mas.
print(type(my_tupla))

# my_tupla.insert(2, "Moure") # No se puede insertar en una tupla. (Error)

print("\n")

# print(my_tupla.sort()) No se puede ordenar una tupla con sort. (Error)

print("\n")

tupla_ordenada = 2,4,6,7,1,9,11
print(sorted(tupla_ordenada)) # Pero con la funcion sorted si se puede...

print("\n")

# del my_tupla     # Elimina la variable con todo y contenido, por completo.
# print(my_tupla)    # No se puede imprimir una variable que ya fue eliminada. (Error)

print(my_tupla)

print("\n")

# Funcion ZIP en las tuplas

integrantes = ["Darli", "Anyeli", "Dayi", "Alexander", "Delfi"]
courses = ("Lenguas Modernas", "Educacion", "Contable", "Ciberseguridad", "Freelancer")
edad = 22,25,23,20,28,

union = zip(integrantes,courses,edad)

print(list(union))
