
### Operadores Aritméticos ###

# Operaciones con enteros
print(3 + 4) # suma
print(3 - 4) 
print(3 * 4)
print(3 / 4)
print(10 % 3) # Modulo o Resto
print(10 // 3) # Division entera
print(2 ** 3) # Exponente
print(2 ** 3 + 3 - 7 / 1 // 4) # Operaciones mixtas

print("\n")

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5)) # Cambiamos el tipo

print("\n")

# Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))

print("\n")

my_float = 2.5 * 2
print("Hola " * int(my_float))

print("\n")

### Operadores Comparativos o Relacionales ###

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

print("\n")

# Operaciones con cadenas de texto
print("Hola" > "Python") # Orden alfabetico
print("Hola" < "Python")
print("aaaa" >= "abaa")
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

print("\n") 


### Operadores Lógicos ###

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python") # Conjuncion
print(3 > 4 or "Hola" > "Python") # Disyuncion 
print(3 < 4 and "Hola" < "Python") 
print(3 < 4 or "Hola" > "Python") 
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4)) # Negacion.