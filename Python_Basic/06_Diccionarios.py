### Diccionarios ###

print("\n")

my_dict = dict() # Creo un diccionario vacio.
my_other_dict = {} # Creo un diccionario vacio tambien de esta manera.

print(type(my_dict)) # Imprimo el tipo de dato que es un diccionario.
print(type(my_other_dict)) # Imprimo el tipo de dato que es un diccionario.

# Dentro de los diccionarios se pueden almacenar cualquier tipo de dato, incluso otros diccionarios.
# Los diccionarios se componen de claves y valores, las claves son los indices de los diccionarios por los que podemos aceder a ellos.

my_dict = {
    
    "Nombre": "Darli", 
    "Apellido": "Gomera Romero", 
    3: 5.7, 
    "Sexo": "Masculino",  # No importa que aqui le agregue un string al diccionario.
    "Correo": "antoniogomera12@gmail.com",
    "Vehiculos": {"Carro", "Moto", "Bicicleta"} # No importa que aqui le agregue un set al diccionario.
    
    } # Añado valores al diccionario.

my_other_dict = {
    
    "Color": "Blanco",
    "Lenguajes": ["Python", "JavaScript", "C#", "Kotlin"], # No importa que aqui le agregue una lista al diccionario
    "Edad": 23,
    "Casa": {
        "Piso": 1,
        "Apartamento": 201,
        "Dirección": "Calle 123, Numero 456"
    } # No importa que aqui le agregue otro diccionario al diccionario.
    
    
}

print("\n")

print(my_dict) # Imprimo el diccionario.

print("\n")


print(my_other_dict) # Imprimo el diccionario.

print("\n")

print(len(my_dict)) # Imprimo la longitud del diccionario. Esto se cuenta por clave.

print(len(my_other_dict)) # Imprimo la longitud del diccionario. Esto se cuenta por clave.

print("\n")

print(my_dict["Vehiculos"]) # Imprimo el valor de la clave. Asi podemos aceder a los valores de las claves.

print(my_other_dict["Casa"]) # Imprimo el valor de la clave.

print(my_other_dict["Lenguajes"]) # Imprimo el valor de la clave.

print("\n")

print(my_dict.get("Apellido")) # Imprimo el valor de la clave.

my_dict["Nombre"] = "Angel Antonio" # Modifico el valor de la clave.

print(my_dict["Nombre"]) # Imprimo el nombre del diccionario modificado.

del my_dict["Sexo"] # Elimino la clave y el valor del diccionario.

print(my_dict)

print("\n")

# Aqui me dara FALSE porque no podemos preguntar por un valor, sino que deberiamos preguntar si esa clave existe.
print("Blanco" in my_other_dict) # Aqui me pregunta si el color blanco existe dentro del diccionario. FORMA INCORRECTA

print("Python" in my_other_dict["Lenguajes"]) # Aqui me pregunta si el valor Python existe en el diccionario, pero especificando  dentro de la clave Lenguajes.

print("Lenguajes" in my_other_dict) # Aqui me pregunta si la clave Lenguajes existe dentro del diccionario. Esta es otra forma correcta de preguntar.

print("\n")

### Ahora vamos a ver algunas de las operaciones que podemos realizar con los diccionarios. ###

my_dict_union = my_dict.copy() # Copio el diccionario my_dict en la variable my_dict_union.

my_dict_union.update(my_other_dict) # Agrego los valores del diccionario my_other_dict al diccionario my_dict_union.

print(my_dict_union) # Imprimo el diccionario my_dict_union.

print("\n")

print() 

print(my_dict.keys()) # Imprimo las claves del diccionario solamente.
print(my_dict.values()) # Imprimo los valores del diccionario solamente.
print(my_dict.items()) # Imprimo las claves y los valores del diccionario por ITEMS.

print("\n")

print(my_dict.fromkeys(my_dict)) # FROMKEYS, lo que hace es que me crea un diccionario vacio.

my_new_dict = dict.fromkeys(("Cama", "Mesa", "Escuela", "Zize")) # FROMKEYS, lo que hace es que me crea un diccionario nuevo con los valores que le indique.  El valor DICT es un valor fijo de python, no de los diccionarios. por eso es que la manera correcta de utilizar esta funcion es con dict antes de fromkeys.

print(my_new_dict) # Imprimo el diccionario my_new_dict.

print(my_new_dict["Cama"]) # Imprimo el valor de la clave Cama, pero no me aparece nada porque esta vacio.

print("\n")

# Ahora voy a agregarles valores a mis claves 1 por 1.


my_new_dict["Cama"] = " 60 Pulgadas" # Le agrego el valor a la clave Cama.

my_new_dict["Mesa"] = " De Cristal" # Le agrego el valor a la clave Mesa.

my_new_dict["Escuela"] = " Los Chiki-Genios" # Le agrego el valor a la clave Escuela.

my_new_dict["Zize"] = " Medium" # Le agrego el valor a la clave Zize.

print(my_new_dict) # Imprimo el diccionario my_new_dict Actualizada.

print("\n")
