
# ========================= Manejo de Ficheros ========================= #

# Escribir en el archivo
buffer = open("fichero.txt", "w")  # Abrir un fichero en modo escritura
buffer.write("Hola, este es un fichero de texto de Angel and Gomera...\n")
buffer.close() # Cierra el buffer

# Leer el archivo 
buffer = open("fichero.txt", "r")
bu = buffer.read(19)  # Lee los primeros 19 caracteres
print(bu)
buffer.close() # Cierra el buffer
