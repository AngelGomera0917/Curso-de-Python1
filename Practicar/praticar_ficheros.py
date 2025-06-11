
# Praticar Ficheros .json
import csv


with open ("practicar/venta.csv", "w") as file_csv:
    escribir = csv.writer(file_csv)
    escribir.writerow(["Producto", "Precio", "Cantidad"])
    escribir.writerow(["Teclado", 1235, 5])
    escribir.writerow(["Mouse", 980, 7])
    escribir.writerow(["Monitor", 7640, 2])

with open ("practicar/venta.csv", "r") as file_reader: 
    leer = csv.reader(file_reader)
    
    next(leer) # El Next Omite la cabecera y lee el resto. La cabecera es la primera fila.
    print("\nTotal Vendido por producto\n")
    precio_general = 0
    for venta in leer:
        producto = venta[0]
        precio = int(venta[1])
        cantidad = int(venta[2])
        total = precio * cantidad
        precio_general += total
        print(producto, ":", total)
        
    print("\nPrecio General de venta: ", precio_general)
    print("\n")

with open ("practicar/tareas.txt", "r+") as file_read:
    file_read.seek(16)
    print(file_read.read()) # 
    
print("\n")

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
    }
    
}

computer["Producto_3"] = {
        "Nombre" : "Monitor",
        "Precio" : 13690,
        "Unidad" : 1
    },

with open ("practicar/venta_productos.json", "w") as file_json:
    json.dump(computer,file_json, indent = 4)

with open ("practicar/venta_productos.json", "r") as reade_file:
        leer_json = json.load(reade_file)
        
        for clave in leer_json:
            print(clave, ":", leer_json[clave]) # Imprime cada clave y su valor en el diccionario JSON
            
        print("\n")
        for clave in leer_json.items():
            print(clave)
            
        print("\n")
        for clave, valor in leer_json["Producto_1"].items():
            print(clave, ":", valor)

print("\n")