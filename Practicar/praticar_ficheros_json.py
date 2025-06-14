# Praticar Ficheros .json

print(" Ficheros Json...\n")

import json

computer = {
    "Producto_1": {
        "Nombre" : "Teclado",
        "Precio" : 1200,
        "Unidad" : 3
    },
    
    "Producto_2": {
        "Nombre" : "Mouse",
        "Precio" : 880,
        "Unidad" : 5
    },
    
}
computer["Producto_3"] = {
        "Nombre" : "Monitor",
        "Precio" : 13690,
        "Unidad" : 1
    } # Aqui agregamos un nuevo producto al diccionario computer. Este producto es un monitor con un precio de 13690 y una unidad.

computer["Producto_4"] = {
        "Nombre" : "CPU",
        "Precio" : 25000,
        "Unidad" : 1
    } # Aqui agregamos otro producto al diccionario computer. Este producto es una CPU con un precio de 25000 y una unidad.

with open ("practicar/venta_productos.json", "w") as file_json:
    json.dump(computer,file_json, indent = 4) # Guarda el diccionario computer en un archivo JSON llamado "venta_productos.json". El parámetro indent = 4 se usa para dar formato al JSON con una sangría de 4 espacios, lo que lo hace más legible.

with open ("practicar/venta_productos.json", "r") as file_loader:
        leer_json = json.load(file_loader) # Carga el contenido del archivo JSON en un diccionario de Python, load se usa para leer el archivo y convertirlo en un objeto de Python.
        
        for clave in leer_json:
            print(clave, ":", leer_json[clave]) # Imprime cada clave y su valor en el diccionario JSON
            
        print("\n")
        for clave in leer_json.items(): # Aqui usamos .items() para obtener las claves y valores de un diccionario.
            print(clave)
            
        print("\n")
        for clave, valor in leer_json["Producto_1"].items(): #Aqui usamos .items() para obtener las claves y valores de un diccionario anidado.
            print(clave, ":", valor)

print("\n")


print("🔥 Primera práctica básica con JSON: Crear, leer, modificar, agregar datos.\n")

print("✅ Ejercicio 1: Crear un archivo JSON simple\n")

# 🎯 Objetivo:
# Crea un archivo llamado datos.json que contenga este diccionario en formato JSON:
# Lee este archivo y muestra su contenido como diccionario en Python.

import json

# 1. Creamos el archivo JSON
datos = {
    "Nombre": "Angel",
    "Apellido": "Gomera",
    "Edad": 30,
    "Ciudad": "Santo Domingo"
}


with open('practicar/datos.json', 'w+') as file_1:
    json.dump(datos, file_1, indent = 4)  # indent para que se vea bonito

# 2. Leemos el archivo JSON
with open('practicar/datos.json', 'r') as file_handler:
    contenido = json.load(file_handler)

print("Contenido del archivo JSON como diccionario:\n")

for llave,valor in contenido.items():
    print(llave, ":", valor)

print("\n")

print("✅ Ejercicio 2: Modificar un valor existente 📝\n")

# 1. Abre el archivo datos.json.

# 2. Cambia el valor de "ciudad" a "Barcelona".

# 3. Guarda los cambios.

with open('practicar/datos.json', 'w') as file_2:
    
    datos["Ciudad"] = "Barcelona"
    
    json.dump(datos,file_2,indent = 4)
    

with open('practicar/datos.json', 'r+') as file_read:
    reader = json.load(file_read)
    
    for attribute_key,attribute_value in reader.items():
        print(attribute_key, ":", attribute_value)

print("\n")

print("✅ Ejercicio 3: Agregar una nueva clave-valor 📝\n")

# Abre el archivo datos.json.

# Agrega la clave "profesion" con el valor "Desarrollador de Software".

# Guarda los cambios.

with open('practicar/datos.json', 'w') as file_3:
    
    datos["Profesion"] = "Desarrollador de Software"
    
    json.dump(datos, file_3, indent = 4)
    
with open('practicar/datos.json', 'r') as file_to_read:
    json_data = json.load(file_to_read)
    
    for field_ke,data_value in json_data.items():
        print(field_ke, ":", data_value)
        

print("\n")

print("✅ Ejercicio 4: Eliminar una clave 📝 \n")

# Abre el archivo datos.json.

# Elimina la clave "edad".

# Guarda los cambios.

with open('practicar/datos.json', 'w') as file_4:
    
    datos.pop("Apellido")
    
    json.dump(datos, file_4, indent = 4)
    
with open('practicar/datos.json', 'r') as file_loader:
    loader = json.load(file_loader)
    
    for key_json,value_json in loader.items():
        print(key_json, ":", value_json)
    

print("\n")

print("✅ Ejercicio 5 (Nivel intermedio): Leer lista de diccionarios 📝\n")

# Cambia el archivo datos.json para que contenga una lista de usuarios:

# Lee el JSON e imprime todos los nombres de los usuarios.

# 1. Creamos la lista de diccionarios (usuarios)
usuarios = [
    {"Nombre": "Dayelin Diaz", "Edad": 21, "Ciudad": "Madrid"},
    {"Nombre": "Angel Gomera", "Edad": 25, "Ciudad": "Valencia"},
    {"Nombre": "Darli M.", "Edad": 24, "Ciudad": "Toronto"}
]

# 2. Guardamos esta lista en un archivo JSON
with open('practicar/usuarios.json', 'w') as usuarios_file:
    json.dump(usuarios, usuarios_file, indent=4)  # indent para que se vea bonito

# 3. Leemos el archivo JSON
with open('practicar/usuarios.json', 'r') as usuarios_file_read:
    lista_usuarios_read = json.load(usuarios_file_read)

# 4. Imprimimos SOLO los nombres de cada usuario
print("Nombres de los usuarios:\n")
for usuario in lista_usuarios_read:
    print(usuario['Nombre'])

print("\n")