
#                                    Status Code HTTP en FastAPI

# Aqui vamos a trabajar con los estados de codigos HTTP en FastAPI, que son respuestas que el servidor envía al cliente para indicar el resultado de una solicitud HTTP.

# Raise HTTP Exception, es una función que se utiliza para lanzar una excepción HTTP personalizada en FastAPI. Esta función se utiliza para devolver un código de estado HTTP específico y un mensaje de error personalizado al cliente.

# Importando las librerías necesarias y http_exception para manejar las excepciones HTTP.
from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router = APIRouter(prefix="/status_http", tags=["Status HTTP"])

class veterinary(BaseModel):
    id: int
    raza: str
    stock: int
    dueño: str
    
database_veterinary = [veterinary(id = 1, raza = "Leon", stock = 5, dueño = "Juan Perez"),
                        veterinary(id = 2, raza = "Bulldog", stock = 3, dueño = "Maria Lopez"),
                        veterinary(id = 3, raza = "Elefante", stock = 2, dueño = "Pedro Sanchez")
                        ]

@router.get("/")
async def root():
    return database_veterinary 

    
# Manejo del Post, se utiliza para enviar datos al servidor y crear un nuevo recurso.

# response_model es un parámetro que se utiliza para especificar el modelo de respuesta que se espera devolver al cliente. En este caso, se espera devolver un objeto de tipo veterinary, esto ayuda mas en la documentacion de Docs y la mejora.
# status_code es un parámetro que se utiliza para especificar el código de estado HTTP que
@router.post("/veterinary_post/", status_code=201, response_model=veterinary) # status_code=201 indica que la solicitud se ha procesado correctamente y se ha creado un nuevo recurso.

async def root_post(animal: veterinary): 
    
    for existing_veterinary in database_veterinary:
        if existing_veterinary.id == animal.id:
            raise HTTPException(status_code = 400, detail = "Ya existe un animal con este ID ❌") #400 indica que la solicitud es incorrecta.
        
        
        if existing_veterinary.raza == animal.raza:
            raise HTTPException(status_code = 404, detail = "Ya existe un animal con esta raza ❌") # 404 indica que el recurso solicitado no se ha encontrado.
    
    database_veterinary.append(animal)
    return animal

