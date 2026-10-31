from fastapi import FastAPI

from pydantic import BaseModel

# Creando una instancia de la aplicación FastAPI
app2 = FastAPI()

# Entidad users_json que devuelve una lista de diccionarios con información de usuarios.
class User(BaseModel):
    name: str
    surname: str
    age: int
    country: str

users_data = [User(name="Darli Mariela", surname="Gomera", age=30, country="EEUU"),
            User(name="Juan", surname="Perez", age=25, country="RD"),
            User(name="Maria", surname="Lopez", age=28, country="Chile")
        ]

@app2.get("/users_json")
async def users_json():
    return [{"name" : "Darli Mariela", "surname" : "Gomera", "Edad" : 30, "Pais" : "EEUU"},
            {"name" : "Juan", "surname" : "Perez", "Edad" : 25, "Pais" : "RD"},
            {"name" : "Maria", "surname" : "Lopez", "Edad" : 28, "Pais" : "Chile"}]

@app2.get("/users")
async def users():
    return users_data