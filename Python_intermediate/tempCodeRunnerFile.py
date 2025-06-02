# Leer el archivo 
buffer = open("fichero.txt", "r")
bu = buffer.read(19)  # Lee los primeros 19 caracteres
print(bu)
buffer.close() # Cierra el buffer
