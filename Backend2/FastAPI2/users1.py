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

@app2.get("/user/{id}")
async def user_one(id: int):
    # Filtramos la lista de usuarios para encontrar el usuario con el id especificado.
    user_list = filter(lambda user: user.id == id , users_data) 
    # Retornamos la lista de usuarios filtrada, que debería contener solo el usuario con el id especificado.
    try:
        return list(user_list)[0]
    except:
        return {"Error" : "Usuario no encontrado"}
    
    
@app2.get("/userQuery/")
async def user_one(id: int):
    # Filtramos la lista de usuarios para encontrar el usuario con el id especificado.
    user_list = filter(lambda user: user.id == id , users_data) 
    # Retornamos la lista de usuarios filtrada, que debería contener solo el usuario con el id especificado.
    try:
        return list(user_list)[0]
    except:
        return {"Error" : "Usuario no encontrado"}