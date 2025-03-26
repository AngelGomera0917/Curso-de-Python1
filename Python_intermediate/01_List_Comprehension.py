### List_Comprehension ###

print("\n")

# Lista de números del 1 al 10
lista = [1,2,3,4,5,6,7,8,9,10]

# Lista de números elevados al cuadrado
cuadrado = [i**2 for i in lista]  # i**2 es igual a i al cuadrado.

# Lista de números pares
pares = [i for i in lista if i % 2 == 0] # Si el residuo de la division es 0, entonces es par.

# Lista de números impares

impares = [i for i in lista if i % 2!= 0] # Si el residuo de la division es diferente de 0, entonces es impar.

print(cuadrado)
print(pares)
print(impares)

print("\n")

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13] # Creo una lista con los numeros del 1 al 13.
print(my_list)

print("\n")

my_range = range(18) # Creo un rango de 17 numeros. 
print(list(my_range))

print("\n")

new_list = [i for i in range(6)] # Creo una lista con los numeros del 0 al 5.
print(new_list)

print("\n")

new_list = [i for i in my_list] # Copio la lista my_list en new_list.
print(new_list)

print("\n")

new_list = [i + 2 for i in my_list] # Sumo 2 a cada elemento de la lista my_list.
print(new_list)

print("\n")

def sum_five(num): # Creo una funcion que suma 5 a un numero.
    return num + 5

new_list = [sum_five(i) for i in my_list]  # Sumo 5 a cada elemento de la lista my_list.
print(new_list)

print("\n")



