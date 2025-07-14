
# Import FastAPI y pydantic para crear una aplicación web y manejar datos
from fastapi import FastAPI

# Importando BaseModel de pydantic para definir modelos de datos
from pydantic import BaseModel

# Creando una instancia de la aplicación FastAPI
app = FastAPI()

@app.get("/user")

# Creamos un modelo de datos para representar un usuario
async def user_json():
    return [{"name": "Angel","Surname": "Gomera", "Age": 22, "Carrera_Universitaria": "Desarrollo de Software", "Url": "https://github.com/AngelGomera0917/Curso-de-Python1"}, 
{"name": "Darli","Surname": "Diaz", "Age": 21, "Carrera_Universitaria": "Lenguas Moderna", "Url": "https://github.com/darli/Curso-de-Python1"}, 
{"name": "Antonio","Surname": "Romero", "Age": 28, "Carrera_Universitaria": "Medicina", "Url": "https://github.com/antonio/Curso-de-Python1"} ]