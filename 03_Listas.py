#Listas
print("\n")

darli = list()
diaz = []

darli: list = [1, 2, 3, 4, 5, 6]
print(darli)

darli = [1, 2, 3, 4, 5, 6]
print(darli)

darli = list([1, 2, 3, 4, 5, 6])
print(darli)

print("\n")

diaz = [7, 8, 9, 10, 10, "My Home", "My computer"]
print(diaz, type(diaz))

#COMO ACCEDER A ELEMENTOS INDEPENDIENTES DE LAS LISTAS.
print("\n")

print(diaz[0])
print(diaz[1])
print(diaz[2])
print(diaz[3])
print(diaz[4])
print(diaz[-2])
print(diaz[-1])
print(diaz.count(10), type(diaz))


print("\n")

mariela = [12, "angel", "javilla"]

edad, name, lugar = mariela

print(edad, name)

print("\n")

name, edad, lugar = mariela[1], mariela[0],mariela[2]

print(name)

print("\n")

print(darli + diaz + mariela)

print("\n")

#Funciones o elementos de las listas.
print("\n")

mariela.append("Hermosa") # Agrega lo que indiques en la ultima parte
print(mariela)

mariela.insert(2, "La mejor maestra es Darli") #Inserta lo que indiques y en que posicion
print(mariela)

mariela.remove("Hermosa") # Elimina por completo lo que le indiques, pero solo si conoces el valor a eliminar.  
print(mariela)

diaz.append("Bella") 
print(diaz)

diaz.pop() # Elimina el ultimo valor de la lista.
print(diaz)

print(diaz.pop(2)) # De esta forma eliminas el valor de la posicion deseada y lo puedes visualizar.
print(diaz)

gomera = diaz.pop(3) # De esta forma eliminas el valor de la posicion deseada y lo puedes visualizar.
print(gomera) # En otras palabras el elemonto se elimina, pero se retorna. Asi puedo saber el elemento que estoy eliminando
print(diaz)

del diaz[1] # Este elimina lo que le indiques.
print(diaz)

romero = diaz.copy()


diaz.clear() # Borra todo por completo.
print(diaz)
print(romero)

romero.append(10)
print(romero.count("My computer"))
print(romero)

romero.reverse()
print(romero)

romero.remove(10)
print(romero)

ca = [2, 3, 6, 7,10, 9, 4]

ca.sort()
print(ca)


#Cambio de tipo a la variable

mariela = "\n Hola Darli" # Antes esta variable era una lista, ahora es un Strings
print(mariela)
print(type(mariela))



