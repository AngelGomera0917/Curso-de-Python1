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

print("\n")

# Ahora vamos hacer ejercicios de Set y luego de diccionarios...

my_set = {"Black", "White", "Blue", "Red", "Yellow", "Orange"}

my_set2 = {3,6,9,5,1,4,1,8}

my_sorted = sorted(my_set, reverse=True)

print(my_set)

print("\n")

my_dict1 = {
    "Name": "Angel Antonio Gomera Romero",
    "Edad": 24,
    "Universidad": "ITLA",
    "Vivienda": {
            "Tipo": "Apartamento",
            "Piso": 3,
            "Condicion": "Excelente"
        },
    "Habitaciones": 3,
    "Lugar": "La Jacobo Macluta"
}

print(my_dict1.items())
print("\n")
print(my_dict1.keys())
print("\n")
print(my_dict1.values())

print("\n")

print(my_dict1)

print(my_dict1["Name"])

print("\n")

my_dict1["Name"] = "Michael Jakson"

print(my_dict1["Name"])
print(my_dict1)

print("\n")

nueva = dict.fromkeys({"Vehiculo", "Calzado"})

print(nueva)

print("\n")

print("\n")

print( """
    ========================== * =============================
        Vamos a realizar varios ejercicios sobre funciones
    ========================== * =============================
    """)

print("\n")

def promedio(*numeros):
    
    suma = sum(numeros)
    
    contar = len(numeros)
    
    
    if contar == 0:
        return (" === No es posible la division entre 0 === ")
    
    else:
        calcular_promedio = suma / contar
        return calcular_promedio

answer = promedio(10, 20, 30, 40)

print(answer)

print("\n")