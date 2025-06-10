
# Praticar Ficheros .json
import csv


with open ("venta.csv", "w") as file_csv:
    escribir = csv.writer(file_csv)
    escribir.writerow(["Producto", "Precio", "Cantidad"])
    escribir.writerow(["Teclado", 1235, 5])
    escribir.writerow(["Mouse", 980, 7])
    escribir.writerow(["Monitor", 7640, 2])

with open ("venta.csv", "r") as file_reader: 
    leer = csv.reader(file_reader)
    
    next(leer)
    print("\nTotal Vendido por producto\n")
    for venta in leer:
        producto = venta[0]
        precio = int(venta[1])
        cantidad = int(venta[2])
        total = precio * cantidad
        print(producto, ":", total)
        
    
    print("\n")
    for index in leer:
        print(", ".join(index))
        