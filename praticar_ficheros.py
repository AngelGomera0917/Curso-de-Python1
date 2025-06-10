
# Praticar Ficheros .txt

import csv

computer = {
    "producto_1": {
        "Nombre": "Teclado",
        "Precio": 1235},  
    
    "producto_2": {
        "Nombre": "Mouse",
        "Precio": 900},   
    
}

computer["producto_3"] = {
    "Nombre": "Monitor",
    "Precio": 12800 }

with open("nota.csv", "w") as file_csv:
    guardar_csv = csv.writer(file_csv)
    
    guardar_csv.writerow(["Producto", "Precio", "Cantidad"])
    guardar_csv.writerow(["Teclado", 1235, 2])
    guardar_csv.writerow(["Mouse", 980, 1])
    guardar_csv.writerow(["Monitor", 14850, 2])

with open("nota.csv", "r") as reader_csv:
    imprimir_csv = csv.reader(reader_csv)

    for index in reader_csv:
        print(index)