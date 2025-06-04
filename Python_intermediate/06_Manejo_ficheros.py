
# ========================= Manejo de Ficheros ========================= #

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
buffer.seek(0)  # Mover el cursor al inicio del fichero, para que pueda leer desde el principio
print(buffer.read(28)) # Imprime el contenido del fichero
buffer.close() # Cierra el buffer

# Leer el archivo 
buffer = open("fichero.txt", "r+")
bu = buffer.readline() # Lee la primera línea del fichero
print(bu)
print(buffer.read())  # Imprime el resto del contenido del fichero
# buffer.close() # Cierra el buffer

# Añadir contenido al archivo
buffer.write("Mi color favorito es Black.\n")  # Añade una nueva línea al 
buffer.write("Soy un excelente estudiante.\n")  # Añade una nueva línea al 
buffer.write("Amo la programacion\n")  # Añade una nueva línea al 
buffer.write("Mi objetivo es ser un desarrollador Full-Stack.\n")  # Añade una nueva línea al 
buffer.seek(0) # Mueve el cursor al inicio del fichero

for contenido_lineas in buffer.readlines():  # La lista que me pasa el readlines(), la vuelvo iterable con el bucle for
    print(contenido_lineas)  # Imprime cada línea del fichero

# readlines() # Devuelve una lista con todas las líneas del fichero.
# readline() # Devuelve una línea del fichero.

# os.remove("fichero.txt")  # Elimina el fichero creado.



