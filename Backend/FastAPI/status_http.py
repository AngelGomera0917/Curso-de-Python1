
#                                    Status Code HTTP en FastAPI

# Aqui vamos a trabajar con los estados de codigos HTTP en FastAPI, que son respuestas que el servidor envía al cliente para indicar el resultado de una solicitud HTTP.

# Raise HTTP Exception, es una función que se utiliza para lanzar una excepción HTTP personalizada en FastAPI. Esta función se utiliza para devolver un código de estado HTTP específico y un mensaje de error personalizado al cliente.

# Importando las librerías necesarias y http_exception para manejar las excepciones HTTP.
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

app = FastAPI()

class veterinary(BaseModel):
    id: int
    raza: str
    stock: int
    dueño: str
    
database_veterinary = [veterinary(id = 1, raza = "Leon", stock = 5, dueño = "Juan Perez"),
                        veterinary(id = 2, raza = "Bulldog", stock = 3, dueño = "Maria Lopez"),
                        veterinary(id = 3, raza = "Elefante", stock = 2, dueño = "Pedro Sanchez")
                        ]

@app.get("/")
async def root():
    return database_veterinary 

# # Ruta del path, se utiliza para acceder a un recurso específico en la aplicación web.
# @app.get("/veterinary_path/{id}")
# async def root_veterinary(id: int):
#     buscar = list(filter(lambda root_veterinary: root_veterinary.id == id, database_veterinary))
    
#     if buscar:
#         return {"Mensaje": "Animal encontrado exitosamente ✅", "Type": buscar[0]}
#     else:
#         return {"Error": "Lo sentimos, No hemos encontrado un Animal con este ID ❌"}
    
    
# # Ruta de la Query, se utiliza para enviar parámetros a la ruta para filtrar o modificar la respuesta.
# @app.get("/veterinary_query/")
# async def root_veterinary(id: int): 
#     buscar = list(filter(lambda root_veterinary: root_veterinary.id == id, database_veterinary))
    
#     if buscar:
#         return {"Mensaje": "Animal encontrado exitosamente ✅", "Type": buscar[0]}
#     else:
#         return {"Error": "Lo sentimos, No hemos encontrado un Animal con este ID ❌"}
    
# Manejo del Post, se utiliza para enviar datos al servidor y crear un nuevo recurso.
@app.post("/veterinary_post/", status_code=201) # status_code=201 indica que la solicitud se ha procesado correctamente y se ha creado un nuevo recurso.

async def root_post(animal: veterinary):
    
    for existing_veterinary in database_veterinary:
        if existing_veterinary.id == animal.id:
            raise HTTPException(status_code = 400, detail = "Ya existe un animal con este ID ❌") #400 indica que la solicitud es incorrecta.
        
        
        if existing_veterinary.raza == animal.raza:
            raise HTTPException(status_code = 404, detail = "Ya existe un animal con esta raza ❌") # 404 indica que el recurso solicitado no se ha encontrado.
    
    database_veterinary.append(animal)
    return {"Mensaje": "Animal agregado exitosamente ✅", "Type": animal}


# # Manejo del Put, se utiliza para actualizar un recurso existente en el servidor.
# @app.put("/veterinary_put/")
# async def root_put(animal: veterinary):
    
#     for index, update_animal in enumerate(database_veterinary):
#         if update_animal.id == animal.id:
#             database_veterinary[index] = animal
#             return {"Mensaje": "Animal actualizado exitosamente ✅", "Type": animal}
        
#     return {"Error": "Lo sentimos, No hemos encontrado un Animal con este ID ❌"} 


# # Manejo del Delete, se utiliza para eliminar un recurso existente en el servidor.
# @app.delete("/veterinary_delete/{id}") 
# async def root_delete(id: int):
    
#     for index, delete_animal in enumerate(database_veterinary):
#         if delete_animal.id == id:
#             del database_veterinary[index]
#             return {"Mensaje": "Animal eliminado exitosamente ✅"}
        
#     return {"Error": "Lo sentimos, No hemos encontrado un Animal con este ID ❌"}