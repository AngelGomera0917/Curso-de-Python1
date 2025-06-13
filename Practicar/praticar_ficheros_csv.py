# Praticar Ficheros .csv

import csv

with open ("practicar/venta.csv", "w", newline="" ) as file_csv: # newline="" se usa para evitar líneas en blanco adicionales en el archivo CSV.
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
        
    print("Precio General de venta: ", precio_general)

print("\n")