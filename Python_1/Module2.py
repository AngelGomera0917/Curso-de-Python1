def planta(cuidado):
    
    if cuidado == "bajo":
        print ("Cactus")
    
    elif cuidado == "medio":
        print ("Suculenta")
    
    elif cuidado == "alto":
        print ("Orquídea")
    
    else:
        return "No se encontró ninguna planta"
    
# Evitar ejecución automática al importar
# if __name__ == "__main__":
#     planta("medio")  # Solo se ejecutará si corres Functionss.py directamente
#     retornar = planta("full")
#     print(retornar)