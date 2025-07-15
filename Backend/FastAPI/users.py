
# Import FastAPI y pydantic para crear una aplicación web y manejar datos
from fastapi import FastAPI

# Importando BaseModel de pydantic para definir modelos de datos
from pydantic import BaseModel

# Creando una instancia de la aplicación FastAPI
app = FastAPI()

@app.get("/userjson")

# Creamos un modelo de datos para representar un usuario
async def user_json():
    return [{"Name": "Angel","Surname": "Gomera", "Age": 22, "Carrera_Universitaria": "Desarrollo de Software", "Url": "https://github.com/AngelGomera0917/Curso-de-Python1"}, 
            
            {"Name": "Darli","Surname": "Diaz", "Age": 21, "Carrera_Universitaria": "Lenguas Moderna", "Url": "https://github.com/darli/Curso-de-Python1"}, 
            
            {"Name": "Antonio","Surname": "Romero", "Age": 28, "Carrera_Universitaria": "Medicina", "Url": "https://github.com/antonio/Curso-de-Python1"} ]


# Entidad Usuario
# Definimos un modelo de datos para representar un usuario
class Usuario(BaseModel):
    Name: str
    Surname: str
    Age: int
    Carrera_universitaria: str
    Url: str

@app.get("/user") # Creamos una ruta para retornar un usuario específico

# Llamamos la clase Usuario y retornamos un objeto de tipo Usuario
async def root_users1():
    return Usuario(Name = "Angel", Surname = "Gomera", Age = 23, Carrera_universitaria = "Desarrollo de Software", Url = "https://github.com/AngelGomera0917/Curso-de-Python1" )


# Esta es otra forma de definir un modelo de datos utilizando la clase BaseModel de pydantic para representar un usuario
class Usuario(BaseModel): # Definimos un modelo de datos para representar un usuario
    Name: str
    Surname: str 
    Age: int
    Carrera_universitaria: str
    Url: str

# Creamos una lista de usuarios utilizando la clase Usuario
user_list = [Usuario(Name = "Angel", Surname = "Gomera", Age = 23, Carrera_universitaria = "Desarrollo de Software", Url = "https://github.com/AngelGomera0917/Curso-de-Python1" ),

Usuario(Name = "Darli", Surname = "Diaz", Age = 23, Carrera_universitaria = "Lenguas Moderna", Url = "https://github.com/darli/Curso-de-Python1" ),

Usuario(Name = "Alexander", Surname = "Romero", Age = 23, Carrera_universitaria = "Medicina", Url = "https://github.com/alexander/Curso-de-Python1" )

]

@app.get("/user_class")
async def root_users2():
    return user_list


@app.get("/user_class2")
async def root_users3():
    return user_list
