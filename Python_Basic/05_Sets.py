
# Sets #

print("\n")

my_sets = set() # Crear un set vacio
sets = {} 

print(type(my_sets))
print(type(sets)) # Inicialmente es un diccionario.

sets = {1, 2, 3, 4,"23", 5, 6, 7, "Blanco", 9, 10} # Ahora es un sets con los valores.
print(type(sets)) 


print(len(sets))


# print(sets[0]) # No se puede acceder a los elementos de un set por posición. (Error)

print("\n")

sets.add("Negro") # Add se utiliza para agregarle valores a mi Set.

print(sets) # Un set es una estructura desordenada, me agrega mi valor en cualquier posicion.

sets.add("Negro")

print(sets) # Los Sets no aceptan valores repetidos, por eso el color negro no esta 2 veces en la lista

print("\n")

print("Blanco" in sets) # Aqui me pregunta si el color blanco existe dentro del set. Asi realizamos busquedas.

print("Azul" in sets) # Aqui vemos que da falso porque AZUL no es parte del set. 


sets.remove("Blanco") # Si puedes eliminar valores, porque los puede modificar tambien..

print(sets)

se = sets.copy() # Copio la lista del Sets y lo guardo en la nueva variable llamada SE.

sets.clear() # Limpia el set, vacia todos los elementos del set, pero la variable sigue creada.

print(se)

# del se # Esto elimina la variable con todo y contenido. Es una funcionalidad de Python DEL...
# print(se) NameError: name 'se' is not defined. Did you mean: 'set'?



My_sets = {"JavaScript", " C#", "Python", "Kotlin"}

my_other_set = {"23", 22, "Debugging"}


my_new_sets = My_sets.union(my_other_set).union({"Lenguaje Maquina"})   # Con UNION podemos unir los set, # Agregamos valores sin la necesidad de crear variables nuevas.

print("\n")

print(my_new_sets)  


print(my_new_sets.difference(My_sets))  # Aqui me muestra los diferentes valores de my_new_sets, que no estan en my_set

print("\n")

print(my_new_sets.union({"Desarrollador"}))  # Agregamos otro valor


print(my_new_sets.difference(My_sets))  # Buscamos nuevamente la diferencia entre my_new_sets y my_set

# Aqui en el resultado observamos que no aparece lo nuevo que agregamos que fue desarrollador, eso pasa porque no lo guardamos dentro de una variable como lo hicimos anteriormente, sino que que lo agregamo en el print directamente. Ahi pudimos ver una diferencia

# del my_new_sets[1] - # Me borra la variable completa con todo y contenido. (Error)

print("\n")

my_new_sets.add("angel") # ADD se utiliza para agregarle valores a mi Set.

print(my_new_sets)

print("\n")

sorted_programming_languages = {"Python", "Java", "C++", "C#", "JavaScript", "PHP", "Ruby", "Swift", "Go", "Kotlin"}

print(sorted(sorted_programming_languages)) # Aqui creamos una lista ordenada del set, pero no cambiamos su naturaleza de ser desordenados... 

print(sorted_programming_languages) # En este caso no se modifica el set, porque no lo guardamos en una variable, solo lo ordenamos para mostrarlo.

print("\n")
