from fastapi import FastAPI

from pydantic import BaseModel

# Creando una instancia de la aplicación FastAPI
app2 = FastAPI()

# Entidad users_json que devuelve una lista de diccionarios con información de usuarios.
class User(BaseModel):
    name: str
    surname: str
    Edad: int
    Pais: str

@app2.get("/users_json")
async def users_json():
    return [{"name" : "Darli Mariela", "surname" : "Gomera", "Edad" : 30, "Pais" : "EEUU"},
            {"name" : "Juan", "surname" : "Perez", "Edad" : 25, "Pais" : "RD"},
            {"name" : "Maria", "surname" : "Lopez", "Edad" : 28, "Pais" : "Chile"}]