
# Praticar Ficheros .txt

print("\n")

print("Ejercicio_1:\n")

with open('practicar/log.txt', 'r+') as file_log:
    
    file_log.seek(0, 2) # Mueve el cursor al final del archivo para agregar contenido.
    # file_log.write("\nFin del Programa.") # Descomentar para agregar "Fin del Programa." al final del archivo log.txt.
    
    file_log.seek(0) 
    
    read_log = file_log.read() 
    
    print(read_log) # Imprime el contenido del archivo log.txt, que ahora incluye "Fin del Programa." al final del archivo.


print("\n")

print("Ejercicio Siguiente:\n")

with open('practicar/lista.txt', "w" ) as file_lista:
    file_lista.write("Primero\n")
    file_lista.write("Tercero\n")
    file_lista.write("Cuarto\n")
    
with open('practicar/lista.txt', 'r+') as file_lista_read:
    lista_read = file_lista_read.read() # Leemos todo el contenido del archivo como una cadena.
    
    convertir = lista_read.split("\n") # Convertimos la cadena en una lista separada por saltos de línea.
    
    convertir.insert(1, "Segundo") # Insertamos "Segundo" en la segunda posición de la lista.
    
    modified_string = "\n".join(convertir) # Unimos la lista de nuevo en una cadena separada por saltos de línea.    
    
    print(type(modified_string)) # Imprime el tipo de la variable letras, que será una cadena (str).
    
print("\n")
    
with open('practicar/lista.txt', "w+" ) as file_lista:
    file_lista.write(modified_string) # Escribimos la cadena modificada de nuevo en el archivo lista.txt.
    
    file_lista.seek(0)
    
    for i in file_lista.readlines(): # Leemos el archivo línea por línea.
        print(i)
    

print("\n")

print("Mismo ejercicio del anterior, pero de otra forma diferente y mas corta:\n")

with open('practicar/lista.txt', "w" ) as file_lista:
    file_lista.write("Primero\n")
    file_lista.write("Tercero\n")
    file_lista.write("Cuarto\n")
    
with open('practicar/lista.txt', 'r+') as file_lista_read:
    lista_read = file_lista_read.readlines()
    
    lista_read.insert(1, "Segundo\n")
    
    # Volvemos al inicio del archivo para reescribir
    file_lista_read.seek(0)
    
    # Escribimos todas las líneas (incluyendo la modificada)
    file_lista_read.writelines(lista_read)
    
    # Si quieres truncar el archivo en caso de que el nuevo contenido sea más corto:
    file_lista_read.truncate()
    
with open('practicar/lista.txt', 'r') as file_lista_read:
    final_output = file_lista_read.read()
    print(final_output)
    
    
print("\n")

print("Ejercicio Siguiente:\n")

with open('practicar/mensaje.txt', 'w') as message_file:
    message_file.write("Hola, Angel Gomera.")

with open('practicar/mensaje.txt', 'r+') as message_reader:
    mensaje = message_reader.read()
    
    rem = mensaje.replace("Angel Gomera","Darli Mariela")
    
    # Volvemos al inicio del archivo para reescribir
    message_reader.seek(0)
    
    # Escribimos todas las líneas (incluyendo la modificada)
    message_reader.writelines(rem)
    
    # Si quieres truncar el archivo en caso de que el nuevo contenido sea más corto:
    message_reader.truncate()
    
with open('practicar/mensaje.txt', 'r+') as message_reader:
    reade_mensaje = message_reader.read() # Leemos el contenido del archivo mensaje.txt después de la modificación.
    print(reade_mensaje)
    
print("\n")

print("Ejercicio Siguiente:\n")

with open('practicar/reporte.txt', 'w+') as reporte_datos:
    reporte_datos.write("Inicio del Reporte\n")
    reporte_datos.write("Datos del Reporte\n")
    reporte_datos.write("Fin del reporte\n")
    
with open('practicar/reporte.txt', "r+") as reporte_read:
    initial_data = reporte_read.readline() # Leemos la primera línea del archivo reporte.txt.
    
    # Leemos el resto del archivo desde la segunda línea en adelante.
    rest_of_file = reporte_read.read()
    
    # Volvemos al inicio del archivo para reescribir
    reporte_read.seek(0)
    
    # Escribimos la primera línea, un resumen y el resto del archivo.
    Summary_text = "Resumen: Este es un resumen general.\n"
    
    # Escribimos todo junto
    # Escribimos la primera línea, el resumen y el resto del archivo.
    reporte_read.writelines(initial_data + Summary_text + rest_of_file)
    
    # Si quieres truncar el archivo en caso de que el nuevo contenido sea más corto:    
    reporte_read.truncate()
    
with open('practicar/reporte.txt', "r+") as reporte_read:
    final_report_data = reporte_read.read() # Leemos el contenido del archivo reporte.txt después de la modificación.
    
    print(final_report_data)  



print("\n")


# print(" Ficheros Excel...\n")
# import pandas as pd 
# # Crear un DataFrame de ejemplo
# data = {
#     'Producto': ['Teclado', 'Mouse', 'Monitor'],
#     'Precio': [1200, 880, 13690],
#     'Unidad': [3, 5, 1]
# }
# df = pd.DataFrame(data) 
# # Guardar el DataFrame en un archivo Excel
# df.to_excel('practicar/venta_productos.xlsx', index=False)  # Guarda el DataFrame en un archivo Excel llamado "venta_productos.xlsx". El parámetro index=False se usa para no incluir el índice del DataFrame en el archivo Excel.
# # Leer el archivo Excel
# df_excel = pd.read_excel('practicar/venta_productos.xlsx')  # Lee el archivo Excel y lo carga en un DataFrame.
# print("Contenido del archivo Excel:")
# print(df_excel)  # Imprime el contenido del DataFrame que se cargó desde el archivo Excel.
# print("\n")
# print(" Ficheros XML...\n")