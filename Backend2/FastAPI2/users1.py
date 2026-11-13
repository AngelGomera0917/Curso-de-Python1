from fastapi import FastAPI

from pydantic import BaseModel

# Creando una instancia de la aplicación FastAPI
app2 = FastAPI()

# Entidad users_json que devuelve una lista de diccionarios con información de usuarios.
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    country: str

users_data = [User(id = 1, name = "Darli Mariela", surname = "Gomera", age = 30, country = "EEUU"),
            User(id = 2, name = "Juan", surname = "Perez", age = 25, country = "RD"),
            User(id = 3, name = "Maria", surname = "Lopez", age = 28, country = "Chile")
        ]  

@app2.get("/users_json")
async def users_json():
    return [{"name" : "Darli Mariela", "surname" : "Gomera", "Edad" : 30, "Pais" : "EEUU"},
            {"name" : "Juan", "surname" : "Perez", "Edad" : 25, "Pais" : "RD"},
            {"name" : "Maria", "surname" : "Lopez", "Edad" : 28, "Pais" : "Chile"}]

@app2.get("/users")
async def users():
    return users_data

@app2.get("/user/{id_one}")
async def user_one(id_one: int):
    # Filtramos la lista de usuarios para encontrar el usuario con el id especificado.
    user_list = filter(lambda user: user.id == id_one , users_data) 
    # Retornamos la lista de usuarios filtrada, que debería contener solo el usuario con el id especificado.
    try:
        return list(user_list)[0]
    except:
        return {"Error" : "Usuario no encontrado"}
    
    
@app2.get("/userQuery")
async def user_one(id: int):
    # Filtramos la lista de usuarios para encontrar el usuario con el id especificado.
    user_list = filter(lambda user: user.id == id , users_data) 
    # Retornamos la lista de usuarios filtrada, que debería contener solo el usuario con el id especificado.
    try:
        return list(user_list)[0]
    except:
        return {"Error" : "Usuario no encontrado"}

# Post

@app2.post("/user")
async def user_post(user: User):
    
    for existing_users in users_data:
        if existing_users.id == user.id:
            return {"Error" : "Usuario con el mismo ID ya existe"}

        elif existing_users.name == user.name or existing_users.surname == user.surname:
            return {"Error" : "Usuario con el mismo nombre o apellido ya existe"}
        
        elif user.name == "" or user.surname == "" or user.country == "" or user.age == "":
            return {"Error" : "Ninguno de los parametros pueden estar vacíos"}
        
        elif user.age <= 0:
            return {"Error" : "La edad debe ser mayor a 0"}
        
    # Agregamos el nuevo usuario a la lista de usuarios.
    users_data.append(user)
    return {"message" : "Usuario agregado correctamente ✅", "user" : user}


# Put

@app2.put("/user")
async def user_put(user: User):
    
    for inde, update in enumerate(users_data):
        if update.id == user.id:
            users_data[inde] = user
            return {"Mensaje": "Usuario actualizado exitosamente ✅", "Usuario Actualizado": user}
        
    return {"Error" : "No se ha encontrado un usuario con este ID"}

#delete

@app2.delete("/user/{id}")
async def user_delete(id: int):
    
    for eliminar in users_data:
        if eliminar.id == id: 
            users_data.remove(eliminar)
            return {"Usuario eliminado ✅": eliminar}