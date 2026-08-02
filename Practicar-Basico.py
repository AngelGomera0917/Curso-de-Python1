frase = "dando siempre Gracias por Todo al Dios y Padre, en el nombre de nuestro señor Jesucristo"

print(frase.capitalize())
print(frase.isnumeric())
print(frase.islower())
print(frase.isdecimal())
print(frase.count("D"))
print(frase.lower())
print(frase.title())
print(frase.startswith("D"))
print(frase.split("e", 3))
print(frase.upper())

print("\n")

my_split = "Hyunda, Toyota, Nissan, Honda and Civic, Ford, Chevrolet, Mercedes, BMW, Audi"

convertidor_Split = my_split.split(",")

print(convertidor_Split)

print("\n")

my_join = ["Nissan", "honda", "civic", "ford", "chevrolet", "mercedes", "bmw", "audi"]

convertidor_Join = " ".join(my_join)

print(convertidor_Join)
print(type(convertidor_Join))

print("\n")

# name = str(input("Introduce tu nombre completo: "))

print("\n")

# letra = len(name)

# print(f" Tu nombre completo es {name.upper()} , y tiene {letra} letras")

print("\n")

my_tupla = (1,7, "Gomera" ,5, "Angel", 9, 6, 4, 5)

print(my_tupla.index(5))
print("\n")
print(my_tupla.count(5))
print(my_tupla[::-1])

print("\n")

palabras = ["banana", "kiwi", "manzana", "uva"]

# Ordenar por longitud
print(sorted(palabras, key=len))

print("\n")

# Ordenar ignorando mayúsculas/minúsculas
nombres = ["Beto", "Ana", "Diana", "carlos"]
print(sorted(nombres, key=str.lower))

estudiantes = [
    {"nombre": "Carlos", "nota": 8},
    {"nombre": "Ana", "nota": 9.5},
    {"nombre": "Luis", "nota": 7},
]

# Con sorted() - crea una nueva lista
mejores = sorted(estudiantes, key=lambda e: e["nota"], reverse=True)
print(mejores[0]["nombre"])  # Ana



