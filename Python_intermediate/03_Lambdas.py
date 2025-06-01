

# ==== # Lambdas # ==== #

# Lambdas son funciones anónimas que se pueden definir en una sola línea.
# Se pueden usar para crear funciones simples sin necesidad de definirlas con def.

print("\n")

sum_two_values = lambda values1, values2: values1 + values2

print("La Suma de ambos valores es de:", sum_two_values(15,40))

print("\n")

# Las lambdas son útiles para funciones pequeñas y rápidas, que solo se le dara un uso específico y no se reutilizarán en otras partes del código.

# Ejemplo de uso de lambda con map

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))  # Eleva al cuadrado cada número en la lista
print("Los números al cuadrado son:", squared_numbers)

print("\n")

multi = lambda x, y: x * y - 8 + 3 # Multiplica x por y, luego resta 8 y suma 3
print("El resultado de la multiplicación es:", multi(5, 20))
