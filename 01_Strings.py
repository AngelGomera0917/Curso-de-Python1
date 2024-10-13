#Strings
from lib2to3.pgen2.driver import Driver


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
a, b, c, d, e = angel

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

contrario = angel[::-1]
print(contrario)


#FUNCIONES
print("\n")

diaz = "Darli es la mejor maestra del planeta ❤❤🙌👩‍🏫👩‍🏫👨‍🎓\n"

print(diaz.capitalize()) # Pone la primera letra mayuscula.
print(diaz.count("a")) # Cuenta las palabras que le indiques
print(diaz.isnumeric()) # Estas preguntando si la variable diaz es numerica
print(diaz.upper()) # Lo pone todo en mayuscula
print(diaz.isupper()) # Estas preguntando si la variable diaz esta todo en mayuscula
print(diaz.upper().isupper()) # Primero pongo todo en mayuscula y luego le pregunto para que de TRUE
print(diaz.lower()) # Lo pone todo en minuscula
print(diaz.islower()) # Estas preguntando si la variable diaz esta todo en minuscula
print(diaz.isdecimal()) # Estas preguntando si la variable diaz es un decimal
print(diaz.split("e", 3)) # Cuando necesitas dividir una cadena en subcadenas, puedes utilizar el método split().
print(diaz.title())

print("\n")
colores = "azul, rojo, amarillo, naranja"
print(colores.split(", ", 2)) 
print("\n")

#BUSQUEDA
print("\n")

mariela = diaz.find("maestra")
print(mariela)

print("\n")

# Ejercicio 1: 

# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero, 
# e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

'''print("\n")

nombre = input("Ingrese su nombre: ")  

numero = int(input("Ingrese un numero entero: "))

resultado = ((" " + nombre + "\n ")  * (numero))

print(resultado) '''


# Ejercicio 2:

''' Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla 
el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas
y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre 
combinando mayúsculas y minúsculas como quiera.'''

'''print("\n")

nombre_completo = input("Introduzca su nombre completo: ")

minúsculas = nombre_completo.lower() 

mayuscula = nombre_completo.upper()

alguna = nombre_completo.title()


print ("\n ", minúsculas)
print("\n")

print (" ", mayuscula)
print("\n")

print (" ", alguna) 
print("\n") '''

'''Ejercicio 3: 

Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca
muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas, 
y <n> es el número de letras que tienen el nombre. '''

'''print("\n")

nombre = input("Ingrese su nombre: ")   


print(f"\n {nombre.upper()} tiene {len(nombre)} letras. ")'''



''' Ejercicio 4:

Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension  donde el prefijo 
es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato y muestre 
por pantalla el número de teléfono sin el prefijo y la extensión. '''

'''print("\n")

telefono = input("Introduzca su numero de telefono con el formato, +xx-xxxxxxxxxx-xx: ")

print(f"\n El numero de telefono es: {telefono [4:-3]} ")'''


'''Ejercicio 5: 

Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla
la frase invertida. '''

'''print("\n")

frase = input(" Escribir una frase de su preferencia: ")

print("\ ",frase[::-1])'''

''' Ejercicio 6:

Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula. '''

'''print("\n")

frase = input("Escribir una frase de su preferencia: ") 

vocal = input("\n Escribir una vocal: ")

print("\n", frase.replace(vocal, vocal.upper()))'''


'''Ejercicio 7: 

Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla
otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es. '''

print("\n")

#email = input("Ingrese su correo electronico: ")
#print(email.replace())


#print("\n", email.split("@") [0] + "@ceu.es")


'''.'''





