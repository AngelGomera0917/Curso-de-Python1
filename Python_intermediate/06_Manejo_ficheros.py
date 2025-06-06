
# ========================= Manejo de Ficheros ========================= #

# file .txt

import os # Módulo para interactuar con el sistema operativo
# El módulo os se importa para interactuar con el sistema operativo desde Python.
# Permite realizar tareas como:

# Trabajar con rutas y archivos (crear, borrar, mover, renombrar archivos y carpetas).
# Obtener información del sistema (como el directorio actual, variables de entorno).
# Ejecutar comandos del sistema.

# Escribir en el archivo
buffer = open("fichero.txt", "w+")  # Abrir un fichero en modo escritura
buffer.write("Hola, este es un fichero de texto de Angel and Gomera...\n")
buffer.write("Mi Lenguaje preferido es Python\n")
# buffer.seek(0)  # Mover el cursor al inicio del fichero, para que pueda leer desde el principio
print(buffer.read(28)) # Imprime el contenido del fichero
buffer.close() # Cierra el buffer

# Leer el archivo 
buffer = open("fichero.txt", "r+")
bu = buffer.readline() # Lee la primera línea del fichero
# print(bu)
# print(buffer.read())  # Imprime el resto del contenido del fichero
# buffer.close() # Cierra el buffer

# Añadir contenido al archivo
buffer.write("Mi color favorito es Black.\n")  # Añade una nueva línea al 
buffer.write("Soy un excelente estudiante.\n")  # Añade una nueva línea al 
buffer.write("Amo la programacion\n")  # Añade una nueva línea al 
buffer.write("Mi objetivo es ser un desarrollador Full-Stack.\n")  # Añade una nueva línea al 
# buffer.seek(0) # Mueve el cursor al inicio del fichero

for contenido_lineas in buffer.readlines():  # La lista que me pasa el readlines(), la vuelvo iterable con el bucle for
    print(contenido_lineas)  # Imprime cada línea del fichero

# readlines() # Devuelve una lista con todas las líneas del fichero.
# readline() # Devuelve una línea del fichero.

# os.remove("fichero.txt")  # Elimina el fichero creado.


# file .json

import json  # Importa el módulo json para trabajar con archivos JSON

# Crear un diccionario de ejemplo
my_json = {
    "nombre": "Angel",
    "edad": 25,
    "Casa": {
        "Piso": 1,
        "Apartamento": 201,
        "Direccion": "Calle 123, Numero 456"},
    "Correo": "antoniogomera12@gmail.com",
    "lenguajes_preferidos": ["Python", "JavaScript", "C#", "Kotlin"],
    "colores_favoritos": ["Black", "Blue", "Red"]
}

my_json["edad"] = 35 # Con esto actualizo el valor de la clave edad
my_json["colores_favoritos"].append("Pink") # Aqui agrego un dato mas a la lista de colores_favoritos


with open("fichero.json", "w+") as json_file:  # Abre el fichero JSON en modo escritura
    # El uso de 'with' asegura que el fichero se cierre automáticamente al finalizar el bloque.
    # Esto es una buena práctica para evitar fugas de recursos, y no usamos close().
    
    # Escribe el diccionario en el fichero JSON

    json.dump(my_json, json_file, indent = 4) # Dump es para escribir el diccionario en el fichero JSON
    # indent = 4 es para que el JSON se vea más bonito, con una sangría de 4 espacios.
    
# json_file.close() Aqui omito el close() porque ya lo hace el with automaticamente

# Leer el fichero JSON  
with open("fichero.json", "r") as json_file_loader:
    json_content = json.load(json_file_loader) # Carga el contenido del fichero JSON en una variable
# load se utiliza para leer el contenido de un fichero JSON y convertirlo en un objeto de Python.

    for i in json_content: # Itera sobre las claves del diccionario cargado desde el JSON
        
        print(i, ":", json_content[i]) # Imprime cada clave y su valor correspondiente del JSON de una manera mas dinamica.
        
print("\n")  # Imprime una línea en blanco para separar la salida

print(json_content,"\n")  # Imprime el contenido del fichero JSON
print(json_content["nombre"],"\n")  # Imprime el valor de la clave "nombre" del JSON
print(type(json_content))  # Imprime el tipo de dato del contenido del JSON (debería ser un diccionario)}

# El uso de 'with' es una buena práctica para manejar archivos, ya que garantiza que el archivo se cierre correctamente, incluso si ocurre un error durante la operación.

print("\n")



