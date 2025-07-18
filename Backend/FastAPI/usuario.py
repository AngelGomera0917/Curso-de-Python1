from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

# Vamos a crear una app que me permita utilizar el metodo CRUD, para crear, leer, actualizar y eliminar un usuario.

class user_profile(BaseModel):
    id: int
    Name: str
    Surname: str
    Age: int
    Statura: float
    
user_datebase = [user_profile(id = 1, Name = "Mariela", Surname = "perez", Age = 21, Statura = 5.5),
                user_profile(id = 2, Name = "Darli", Surname = "Martinez", Age = 27, Statura = 3.8),
                user_profile(id = 3, Name = "Joel Alexander", Surname = "Ramirez", Age = 34, Statura = 7.2),
                ]


@app.get("/")

async def root():
    return user_datebase

# Path, se pasa como parametro a la URL, para asi filtrar informacion de manera especifica.

@app.get("/user_path/{id}")

async def root_path(id: int):
    filtro_list = list(filter(lambda root_path: root_path.id == id, user_datebase))
    
    try:
        return {"mensaje": "Su usuario fue encontrado de manera exitosa", "Usuario encontrado":filtro_list[0]}
    
    except:
        return {"Error": "Usuario no encontrado"}
    

# Query, se pasa como parametro a la URL, pero no es parte de la ruta y se utiliza para enviar parametro a la ruta y obtener resultado

@app.get("/user_query/")

async def root_query(id: int):
    filtro_list = list(filter(lambda root_query: root_query.id == id, user_datebase))
    
    try:
        return {"mensaje": "Su usuario fue encontrado de manera exitosa", "Usuario encontrado":filtro_list[0]}
    
    except:
        return {"Error": "Usuario no encontrado"}
    
    
# Ahora si vamos a crear el CRUD

# Post

@app.post("/user_post/")
async def root_post(user: user_profile):
    
    for add_user in user_datebase:
        if add_user.id == user.id:
            return {"Error": "Ya existe un usuario con este ID"}
        
        if add_user.Name == user.Name or add_user.Surname == user.Surname:
            return {"Error": "El nombre o apellido de este usuario ya existe en la base de datos"}
        
        if user.id <= 0:
            return {"Error": "El ID proporcionado debe ser mayor a 0"}
        
        
    user_datebase.append(user)
    return {"Nuevo Usuario Agregado": user}

# put

@app.put("/user_put/")

async def root_put(user: user_profile):
    for index, update_user in enumerate(user_datebase):
        if update_user.id == user.id:
            user_datebase[index] = user
            return {"Nuevo usuario Actualizado": update_user}

    return {"Error": "Usuario no encontrado para ser actualizado"}


# delete
# @app.delete("/user_delete/")
# async def root_delete(user: user_profile):
#     for eliminar in user_datebase:
#         if eliminar.id == user.id:
#             user_datebase.remove(eliminar)
#             return {"Usuario eliminado": eliminar}

#     return {"Error": "Usuario no encontrado para ser eliminado"}

@app.delete("/user_delete/{id}")
async def root_delete(user: user_profile):
    for eliminar in user_datebase:
        if eliminar.id == user.id:
            user_datebase.remove(eliminar)
            return {"Usuario eliminado": eliminar}

    return {"Error": "Usuario no encontrado para ser eliminado"}
