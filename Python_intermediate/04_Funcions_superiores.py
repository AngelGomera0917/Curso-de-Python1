
# ========================= Funciones de orden superior ========================= #

# Funciones de orden superior son aquellas que pueden recibir otras funciones como argumentos o devolver funciones como resultados.
# Estas funciones son útiles para crear código más modular y reutilizable.

# Vamos a ir paso a paso con ejemplos de cada una de estas funciones de orden superior.


print("\n")


def increment_by_five(value):
  return value + 5 # Esta función toma un valor y le suma 5.

# Aqui le pasamos la funcion por parametro
def sumar(value1, value2, value3):
  return value3(value1 + value2)

print(sumar(10, 20, increment_by_five)) # Llama a la función sumar con los valores 10 y 20, y la función valores que suma 5 a la suma de los dos primeros valores.

print("\n")

# Ahora vamos a llamar la funcion directamente, osea sin parametros...

def increment_by_six(base_value):
  return base_value + 6 # Esta función toma un valor y le suma 6.

def sumar_dos_valores(first_value, second_value):
  return increment_by_six(first_value + second_value) # Esta función toma dos valores y los suma.

print(sumar_dos_valores(10, 20)) # Llama a la función sumar_dos_valores con los valores 10 y 20. 

print("\n")

# ======== # Tambien trae algunas que ya vienen con Python, como Map, Filter y Reduce. # ======== #

# ========================= # Map # ========================= #

# Se puede usar Map como función de orden superior, ya que recibe una función y una lista como argumentos, y aplica la función a cada elemento de la lista.

number_list = 1, 4, 6, 7, 5 # Aqui tenemos una lista de números.
# Vamos a usar map para sumar 2 a cada elemento de la lista.

using_map = list(map(lambda number_sum: number_sum + 2, number_list)) # Usamos map para aplicar la función lambda que suma 2 a cada elemento iterable de la lista.

print(using_map) # Imprimimos el resultado de la lista con los elementos sumados.

print("\n")

# ========================= # Filter # ========================= #

# Se puede usar Filter para filtrar elementos de una lista según una condición.

number_list_Filter = [1, 4, 6, 7, 8, 10, 14, 5, 17, 19, 20, 24, 23] # Aqui tenemos una lista de números.

using_filter = list(filter(lambda filter_value: filter_value % 2 == 0, number_list_Filter)) # Usamos filter para aplicar la función lambda que filtra los números pares de la lista. Le coloque una condicion para que solo retorne los números pares.

print(using_filter)

print("\n")

# ========================= # Reduce # ========================= #

# Reduce para aplicar una función acumulativa a los elementos de una lista, para este es necesario importar reduce del módulo functools.

from functools import reduce # Importamos reduce del módulo functools.

number_reduce = [1, 6, 7, 8, 10, 14, 5, 17, 19, 20, 24, 23] 

using_reduce = reduce(lambda x , y: x + y, number_reduce) # Usamos reduce para aplicar la función lambda que suma todos los elementos de la lista.
# La función lambda toma dos argumentos x e y, y devuelve su suma. Reduce aplica esta función a los elementos de la lista de izquierda a derecha, acumulando el resultado.

print(using_reduce)

print("\n")







