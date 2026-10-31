from fastapi import FastAPI

app2 = FastAPI()

@app2.get("/users_json")
async def users_json():
    return [{"name" : "Darli Mariela", "surname" : "Gomera", "Edad" : 30, "Pais" : "EEUU"},
            {"Usuario" : "Juan", "surname" : "Perez", "Edad" : 25, "Pais" : "RD"},
            {"Usuario" : "Maria", "surname" : "Lopez", "Edad" : 28, "Pais" : "Chile"}]