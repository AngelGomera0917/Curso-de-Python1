
# Import FastAPI y pydantic para crear una aplicación web y manejar datos
from fastapi import FastAPI

# Importando BaseModel de pydantic para definir modelos de datos
from pydantic import BaseModel

# Creando una instancia de la aplicación FastAPI
app = FastAPI()

# Get, se utiliza para obtener datos del servidor. En este caso, se utiliza para obtener una lista de usuarios en formato JSON.
@app.get("/user_json")

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
async def root_user1():
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
async def root_user2():
    return user_list


class user_profile(BaseModel):
    id_user: int
    Name: str
    Surname: str
    Age: int
    
user_database = [user_profile(id_user = 1, Name = "Emma Elena", Surname = "Gomez Diaz", Age = 25),
                user_profile(id_user = 2, Name = "Marileisy", Surname = "Peralta Sanchez", Age = 42),
                user_profile(id_user = 3, Name = "Katherin", Surname = "De Los Santos", Age = 29),]

# Directorio raiz de la ruta
@app.get("/")
async def root():
    return user_database

# Path, se pasa como parte de la URL y es una ruta que permite acceder a un recurso específico en la aplicación web.
@app.get("/user_path/{id_user}") # Se define una ruta que recibe un parámetro id_user
async def root_class(id_user: int):
    find_user = list(filter(lambda root_class: root_class.id_user == id_user, user_database))
    
    try:
        return find_user[0] # [0] Devuelve el primer (y único) objeto que coincide.
    
    except:
        return {"Error ❌": " El usuario no existe "}


# Query, se pasa como parte de la URL, pero no es parte de la ruta y es una forma de enviar parámetros a la ruta para filtrar o modificar la respuesta.

@app.get("/user_query/")
async def root_class(id_user: int):
    find_user = list(filter(lambda root_class: root_class.id_user == id_user, user_database))
    try:
        return find_user[0] # [0] Devuelve el primer (y único) objeto que coincide.
    
    except:
        return {"Error ❌": " Usuario no encontrado "} 


# Post, se utiliza para enviar datos al servidor y crear un nuevo recurso. En este caso, se utiliza para crear un nuevo usuario.
@app.post("/user_post/")
async def root_post(user: user_profile): # Recibe un objeto de tipo user_profile):

    # Verifica si el usuario ya existe en la base de datos
    for existing_user in user_database:
        if existing_user.id_user == user.id_user:
            return {"Error ❌": " Ya existe un ususario con este ID"}
        
        if existing_user.Name == user.Name or existing_user.Surname == user.Surname:
            return {"Error ❌": " Ya existe un usuario con el mismo nombre o apellido "}
        
        # Si el usuario ya existe, retorna un mensaje de error
        if user.Name == "" or user.Surname == "" or user.Age <= 0: # Verifica si el nombre, apellido y edad son válidos
            return {"Error ❌": " El nombre, apellido y edad deben ser válidos "}
            
        # Si el usuario no existe, lo agrega a la base de datos
        if user.id_user <= 0: # Verifica si el id_user es válido
            return {"Error ❌": " El id_user debe ser mayor que 0 "}
    
    user_database.append(user) # Agrega el usuario a la base de datos
    return {"Mensaje": "Usuario creado exitosamente ✅", "Nuevo Usuario": user} # Retorna un mensaje de éxito y el usuario creado


# Put, se utiliza para actualizar un recurso existente. En este caso, se utiliza para actualizar un usuario existente.

@app.put("/user_put/")
async def root_put(user: user_profile):
    # index es para encontrar el índice del usuario en la base de datos y Enumerate es para recorrer la lista de usuarios
    for index, saved_user in enumerate(user_database): # Recorre la base de datos de usuarios
        # Verifica si el usuario existe
        if saved_user.id_user == user.id_user:
            user_database[index] = user # Actualiza el usuario en la base de datos
            return {"Mensaje": "Usuario actualizado exitosamente ✅", "Usuario Actualizado": user}
        
    return {"Error ❌": " Usuario no encontrado "}


# Delete, se utiliza para eliminar un recurso existente. En este caso, se utiliza para eliminar un usuario existente.

@app.delete("/user_delete/{id_user}")
async def root_delete(id_user : int):
    for eliminar in user_database:
        if eliminar.id_user == id_user: 
            user_database.remove(eliminar)
            return {"Usuario eliminado": eliminar}

    return {"Error ❌": "Usuario no encontrado para ser eliminado"}


# Esta es otra forma de definir el método delete, utilizando un objeto de tipo user_profile para identificar el usuario a eliminar.


# @app.delete("/user_delete/{id_user}")

# async def root_delete(id_user: int): # Recibe un parámetro id_user para identificar el usuario a eliminar
#     # Recorre la base de datos de usuarios
#     # Enumerate se utiliza para obtener el índice del usuario en la lista
#     for index, user in enumerate(user_database):
#         if user.id_user == id_user:
#             del user_database[index]
#             return {"Mensaje": "Usuario eliminado exitosamente ✅"}
        
#     return {"Error ❌": "El usuario no ha podido ser encontrado en la base de datos."}