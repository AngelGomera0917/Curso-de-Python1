### Bucles - Loops - Ciclos ###

# Bucles For
""" Los bucles for son utilizados para iterar sobre una secuencia de elementos.
La secuencia puede ser una lista, una tupla, un diccionario, un set, o una cadena de texto.
El bucle for se ejecuta una vez por cada elemento de la secuencia."""

# Bucles While
""" Los bucles while se utilizan para repetir un bloque de codigo mientras una condicion sea verdadera.
El bucle while se ejecuta mientras la condicion sea verdadera."""

# Bucles Anidados
""" Los bucles anidados son bucles dentro de otros bucles.
Esto se utiliza para iterar sobre multiples secuencias de elementos."""

# Bucles Infinitos
""" Los bucles infinitos son bucles que nunca terminan.
Esto se utiliza para iterar sobre multiples secuencias de elementos."""

# Bucles con else
""" Los bucles con else se utilizan para ejecutar un bloque de codigo una vez que el bucle haya terminado.
El bloque de codigo se ejecuta una vez que la condicion del bucle sea falsa."""

# Bucles con break
    # El break se utiliza para salir de un bucle cuando se cumple una condicion.
    
# Bucles con continue
    # El continue se utiliza para saltar a la siguiente iteracion del bucle.
    
# Bucles con pass
    # El pass se utiliza para evitar que el bucle tire un error cuando no tiene codigo a ejecutar.
    
# Bucles con range
    # El range se utiliza para generar una secuencia de numeros.
    
# Bucles con enumerate
    # El enumerate se utiliza para agregar un indice a cada elemento de una secuencia.
    
# Bucles con map
    # El map se utiliza para aplicar una funcion a cada elemento de una secuencia.
    
# Bucles con zip
    # El zip se utiliza para combinar dos o mas secuencias de elementos en una sola secuencia.
    
# Bucles con iter
    # El iter se utiliza para convertir una secuencia en un iterable.
    
print("\n")

# i = 13

# while i > 10: # Bucle infinito, porque la condicion siempre sera verdadera.
#     print(i) # Imprimo el valor de i.
#     i += 12 # Incremento el valor de i en 1.

                                                        # Bucle While #

my_condition = 0

while my_condition < 10:
    
    print(my_condition,"\n") # Imprimo el valor de my_condition.
    my_condition += 2 # Incremento el valor de my_condition en 2.

else: # Este else pertenece al bucle while.
    print(" Mi condicion es mayor o igual a", my_condition) # No todos los lengujes de programacion tienen la funcionalidad de ELSE en los bucles.
    
print("\n")

while my_condition < 20:
    my_condition += 2 # Incremento el valor de my_condition en 2.
    
    if my_condition == 18:
        print(" Mi condicion es igual a", my_condition,"\n") # Imprimo el valor de my_condition.
        break # Salgo del bucle con break. Esto es para parar el bucle
    
    print(my_condition,"\n") # Imprimo el valor de my_condition.
    
    
print("\n")

contador = 0

while contador < 10:
    contador += 1 # Incremento el valor de contador en 1.
    
    if contador == 5:
        break # Salgo del bucle con break. Esto es para parar el bucle
    
    print(contador,"\n") # Imprimo el valor de contador.

print("\n")

contador2 = 0

while contador2 < 10:
    contador2 += 1 # Incremento el valor de contador en 1.
    
    if contador2 == 7:
        continue # Salto a la siguiente iteracion del bucle. Esto es para saltar a la siguiente iteracion del bucle.
    
    print(contador2,"\n") # Imprimo el valor de contador.

print("\n")




                                            # bUcle For #

My_list = list([6, 2, 10, 8, 9, 1, 7, 4, 5, 3])

for i in My_list: # Itero sobre la lista My_list.
    print(i,"\n") # Imprimo el valor de i.

print("\n")

my_tupla = (1,7, "Gomera" ,5, "Angel", 9, 6)

for i in my_tupla: # Itero sobre la lista my_tupla.
    
    print(i,"\n") # Imprimo el valor de i.


print("\n")
my_dict = {
    
    "Nombre": "Darli", 
    "Apellido": "Gomera Romero", 
    3: 5.7, 
    "Sexo": "Masculino",  # No importa que aqui le agregue un string al diccionario.
    "Correo": "antoniogomera12@gmail.com",
    "Vehiculos": {"Carro", "Moto", "Bicicleta"} # No importa que aqui le agregue un set al diccionario.
    
    }

for i in my_dict: # Itero sobre la lista my_dict.  
    print(i,"\n") # Imprimo el valor de i. Solo me imprime las claves...
    
    if i == "Correo":
        break # Salgo del bucle con break. Esto es para parar el bucle. se para en CORREO Y NO IMPRIME MAS. 
    
    
print("\n")
my_dict = {
    
    "Color": "Blanco",
    "Lenguajes": ["Python", "JavaScript", "C#", "Kotlin"], # No importa que aqui le agregue una lista al diccionario
    "Edad": 23,
    "Casa": {
        "Piso": 1,
        "Apartamento": 201,
        "Dirección": "Calle 123, Numero 456"
    }
}

for i in my_dict.values(): # Itero sobre la lista my_dict.  
    print(i,"\n") # Imprimo el valor de i. Solo me imprime los valores porque los especifique...
    
else:
    print("No hay mas elementos en mi diccionario.") # Imprimo un mensaje cuando ya no hay mas elementos en mi diccionario.
    
print("\n")


print("\n")
my_dict = {
    
    "Nombre": "Darli", 
    "Apellido": "Gomera Romero", 
    3: 5.7, 
    "Sexo": "Masculino",  # No importa que aqui le agregue un string al diccionario.
    "Correo": "antoniogomera12@gmail.com",
    "Vehiculos": {"Carro", "Moto", "Bicicleta"} # No importa que aqui le agregue un set al diccionario.
    
    }

for i in my_dict: # Itero sobre la lista my_dict.  
    print("\n",i) # Imprimo el valor de i. Solo me imprime las claves...
    
    if i == "Correo":
        continue
    # print("\n",i)
    print("Valido") # Salto a la siguiente iteracion del bucle. Esto es para saltar a la siguiente iteracion del bucle.

print("\n")

for i in range(10): # Con RANGE le indicamos que imprima en un rango hasta 10
    print(i)
    
print("\n")

for i in range(5,20): # Aqui contamos desde 5 hasta 20
    print(i,"\n")
    
print("\n")

for i in range(5,20,2): # Aqui contamos desde 5 hasta 20 con saltos de 2
    print(i)
    
print("\n")

# Vamos a crear la tabla numerica del 3, del 1 al 10.

for i in range(1, 11):
    resultado = 3 * i
    print(f"{3} * {i} = {resultado}\n")
    

# Tabla de multiplicar donde pasaremos el numero de multiplicar por teclado

numero = int(input("Ingrese un numero: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}\n")
    
# Otra forma de hacer esta misma tabla seria

def tabla_multiplicar(tabla,limite):
    
    for i in range(1,limite + 1):
        result = tabla * i
        print(f" {tabla} * {i} = {result}")
        
number = int(input(" Ingrese que tabla desea verificar: "))
max_multiplier = int(input(" Ingrese hasta que numero desea la multiplicacion: "))

tabla_multiplicar(number,max_multiplier)