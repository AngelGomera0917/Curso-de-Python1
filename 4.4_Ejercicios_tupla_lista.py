# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.


"""
# Pedir los números ganadores al usuario, separados por espacios
numeros_ganadores = input("Por favor, introducir los números ganadores de la lotería primitiva: ")

# Convertir la entrada en una lista de enteros
numeros_ganadores = list(map(int, numeros_ganadores.split()))

# Ordenar los números de menor a mayor
numeros_ganadores.sort()

# Mostrar los números ordenados
print("Los números ganadores en orden de menor a mayor son:", numeros_ganadores)

# print(type(numeros_ganadores))

print("\n")"""

# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

valor = [6, 2, 10, 8, 9, 1, 7, 4, 5, 3]
valor.sort(reverse=True) # Ordena de mayor a menor
print(type(valor))
print(valor)