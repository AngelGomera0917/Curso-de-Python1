#Strings



print("\n")

my_linea_string = "Esto es un string\ncon salto de linea"
print(my_linea_string)

my_tabulacion_string = "\tEsta es un string con tabulacion"
print(my_tabulacion_string)

my_linea_string = "\tEsta es un string\nescapado"
print(my_linea_string)

#Formateo
print("\n") 

name, apellido, edad = "Darli", "Diaz", 22

print("Mi nombre es {} {}, y tengo {} años de edad.".format(name,apellido,edad))
print("Mi nombre es %s %s, y tengo %d años de edad."%(name,apellido,edad))
print(f"Mi nombre es {name} {apellido}, y tengo {edad} años de edad.")
print(f"{4+4}")

#Desempaqueado de carateres
print("\n")

angel = "Darli"
a, b, c, d, e = angel # Con esto desempaquetamos los caracteres de la variable angel.

print(a)
print(c)

#Extracion 
print("\n")

romero = angel[2:] 
print(romero)
todo = angel[0:]
print(todo)
meno = angel[-2]
print(meno)

#Alreves 
print("\n")

contrario = angel[::-1] # Con este invertimos todo.
print(contrario)

#Desempaqueado de carateres

#FUNCIONES
print("\n")

diaz = "Darli es la mejor maestra del planeta ❤❤🙌👩‍🏫👩‍🏫👨‍🎓\n"

print(diaz.capitalize()) # Pone la primera letra mayuscula...
print(diaz.count("a")) # Cuenta las palabras que le indiques
print(diaz.isnumeric()) # Estas preguntando si la variable diaz es numerica
print(diaz.upper()) # Lo pone todo en mayuscula
print(diaz.isupper()) # Estas preguntando si la variable diaz esta todo en mayuscula
print(diaz.upper().isupper()) # Primero pongo todo en mayuscula y luego le pregunto para que de TRUE
print(diaz.lower()) # Lo pone todo en minuscula
print(diaz.islower()) # Estas preguntando si la variable diaz esta todo en minuscula
print(diaz.isdecimal()) # Estas preguntando si la variable diaz es un decimal
print(diaz.split("e", 3)) # Cuando necesitas dividir una cadena en subcadenas, puedes utilizar el método split().
print(diaz.title()) # Con este podemos poner cada inicial de una palabra en mayuscula.
print(diaz.startswith("D")) # Con este podemos preguntar si la variable diaz empieza con la letra que le indiquemos.
print("\n")
colores = "azul, rojo, amarillo, naranja"
print(colores.split(", ", 2)) 
print("\n")

# BUSQUEDA
print("\n")

mariela = diaz.find("maestra") # Con el FIND podemos encontrar la posision en la que se encuentra.
print(mariela)

print("\n")
# Extraccion
extraer = diaz[15:22] # Con esto podemos extraer una palabra de la cadena.
print(extraer)

print("\n")

remplazar =  colores.replace("naranja", "verde") # Con el REPLACE podemos reemplazar una palabra por otra.

print(remplazar)

                                            # Metodo JOIN and Split
print("\n")

# Split este me genera una lista de cadenas a partir de un String.
# Join este me genera un String a partir de una lista de cadenas.

my_split = "Hyunda, Toyota, Nissan, Honda and Civic, Ford, Chevrolet, Mercedes, BMW, Audi"

print(my_split.split(", ")) # Con esto divido la cadena en una lista de cadenas. Mi identificador para separarlo es la coma y el espacio (, ).

print("\n")

my_join = ["nissan", "honda", "civic", "ford", "chevrolet", "mercedes", "bmw", "audi"] # Con esto genero una lista de cadenas.

new_join = ", ".join(my_join) # Con esto genero una cadena a partir de la lista de cadenas. Mi identificador para unirlo es la coma y el espacio (, ).

print(new_join) # Imprimo la cadena generada a partir de la lista de cadenas.

print("\n")