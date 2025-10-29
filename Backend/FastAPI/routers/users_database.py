
# Cambie fastapi por apirouter para manejar las rutas de la aplicación

# Importando las librerías necesarias y http_exception para manejar las excepciones HTTP.

from fastapi import APIRouter, HTTPException

from Database.client_db import db_client

from models.models_user import user_profile

# Creando una instancia de la aplicación FastAPI
router = APIRouter(prefix="/users_db", tags=["Users wih Database MongoDB"])

user_database = []

# Get, se utiliza para obtener datos del servidor. En este caso, se utiliza para obtener una lista de usuarios en formato JSON.
@router.get("/")
async def user_all():
    return user_database


# Directorio raiz de la ruta
@router.get("/")
async def root():
    return user_database

# Path, se pasa como parte de la URL y es una ruta que permite acceder a un recurso específico en la aplicación web.
@router.get("/path/{id_user}") # Se define una ruta que recibe un parámetro id_user
async def root_class(id_user: int):
    find_user = list(filter(lambda root_class: root_class.id_user == id_user, user_database))
    
    try:
        return find_user[0] # [0] Devuelve el primer (y único) objeto que coincide.
    
    except:
        raise HTTPException(status_code = 400, detail = {"Error ❌": " El usuario no existe "})
        


# Query, se pasa como parte de la URL, pero no es parte de la ruta y es una forma de enviar parámetros a la ruta para filtrar o modificar la respuesta.

@router.get("/query/")
async def root_class(id_user: int):
    find_user = list(filter(lambda root_class: root_class.id_user == id_user, user_database))
    try:
        return find_user[0] # [0] Devuelve el primer (y único) objeto que coincide.
    
    except:
        raise HTTPException(status_code = 404, detail = {"Error ❌": " El usuario no encontrado "})


# Post, se utiliza para enviar datos al servidor y crear un nuevo recurso. En este caso, se utiliza para crear un nuevo usuario.
@router.post("/post/", response_model = user_profile, status_code = 201)
async def root_post(user: user_profile): # Recibe un objeto de tipo user_profile):

    # # Verifica si el usuario ya existe en la base de datos
    # for existing_user in user_database:
    #     if existing_user.id_user == user.id_user:
    #         raise HTTPException(status_code = 404, detail = {"Error ❌": " Ya existe un ususario con este ID"})
            
        
    #     if existing_user.Name == user.Name or existing_user.Surname == user.Surname:
    #         raise HTTPException(status_code = 400, detail = {"Error ❌": " Ya existe un usuario con el mismo nombre o apellido "})
            
        
    #     # Si el usuario ya existe, retorna un mensaje de error
    #     if user.Name == "" or user.Surname == "" or user.Age <= 0: # Verifica si el nombre, apellido y edad son válidos
    #         raise HTTPException(status_code = 404, detail = {"Error ❌": " El nombre, apellido y edad deben ser válidos "})
            
            
    #     # Si el usuario no existe, lo agrega a la base de datos
    #     if user.id_user <= 0: # Verifica si el id_user es válido
    #         raise HTTPException(status_code = 400, detail = {"Error ❌": " El id_user debe ser mayor que 0 "})
    # user_dict = user.dict()
    nuevo = db_client.local.users.insert_one(user.dict())
    return {"id" : str(nuevo.inserted_id), **user.dict()}
    
    # user_database.append(user) # Agrega el usuario a la base de datos
    # return {"Mensaje": "Usuario creado exitosamente ✅", "Nuevo Usuario": user} # Retorna un mensaje de éxito y el usuario creado


# Put, se utiliza para actualizar un recurso existente. En este caso, se utiliza para actualizar un usuario existente.

@router.put("/put/")
async def root_put(user: user_profile):
    # index es para encontrar el índice del usuario en la base de datos y Enumerate es para recorrer la lista de usuarios
    for index, saved_user in enumerate(user_database): # Recorre la base de datos de usuarios
        # Verifica si el usuario existe
        if saved_user.id_user == user.id_user:
            user_database[index] = user # Actualiza el usuario en la base de datos
            return {"Mensaje": "Usuario actualizado exitosamente ✅", "Usuario Actualizado": user}
        
    raise HTTPException(status_code = 404, detail = {"Error ❌": " Usuario no encontrado "})
    


# Delete, se utiliza para eliminar un recurso existente. En este caso, se utiliza para eliminar un usuario existente.

@router.delete("/delete/{id_user}", response_model=user_profile)
async def root_delete(id_user : int):
    for eliminar in user_database:
        if eliminar.id_user == id_user: 
            user_database.remove(eliminar)
            return {"Usuario eliminado": eliminar}

    raise HTTPException(status_code = 404, detail = {"Error ❌": "Usuario no encontrado para ser eliminado"})
    


# Esta es otra forma de definir el método delete, utilizando un objeto de tipo user_profile para identificar el usuario a eliminar.


# @router.delete("/user_delete/{id_user}")

# async def root_delete(id_user: int): # Recibe un parámetro id_user para identificar el usuario a eliminar
#     # Recorre la base de datos de usuarios
#     # Enumerate se utiliza para obtener el índice del usuario en la lista
#     for index, user in enumerate(user_database):
#         if user.id_user == id_user:
#             del user_database[index]
#             return {"Mensaje": "Usuario eliminado exitosamente ✅"}
        
    # raise HTTPException(status_code = 404, detail = {"Error ❌": "El usuario no ha podido ser encontrado en la base de datos."})
