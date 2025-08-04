# Vamos a crear una API para una libreria que me permita Leer, agregar, actualizar y eliminar datos usando las cuatros operaciones basicas de una Base de Datos que es el CRUD 

# voy a vilver esto a una apirouter para que sea mas facil de manejar y entender, y poder correrla en el main.py que es el principal de la aplicacion

from fastapi import APIRouter

from pydantic import BaseModel

router = APIRouter(prefix="/libreria", tags=["Libreria"])

class library(BaseModel): 
    id : int
    titulo : str
    autor : str
    stock : int
    año_publicacion : int

database_library = [library(id = 1, titulo = "El señor de los Anillos", autor = "J.R.R Tolkien", stock = 3, año_publicacion = 2005),
                    library(id = 2, titulo = "Harry Potter y la piedra Filosofal", autor = "A.D.M Willian ", stock = 6, año_publicacion = 1987),
                    library(id = 3, titulo = "Cien años de soledad", autor = "Gabriel García Márquez", stock = 1, año_publicacion = 1927)
                    ]

# Ruta principal
@router.get("/")

async def root():
    return database_library

# Ruta del path

@router.get("/book_path/{id}")

async def root_book (id : int):
    
    try:
        buscar = list(filter(lambda root_book: root_book.id == id, database_library))
        return {"Mensaje": "Libro encontrado exitosamente ✅",
                "Book" : buscar[0]}
    except:
        return {"Error" : "Lo sentimos, No hemos encontrado un libro con este ID ❌"}
    
# Ruta de la Query

@router.get("/book_query/")

async def root_book (id : int):
    
    try:
        buscar = list(filter(lambda root_query: root_query.id == id, database_library))
        return {"Mensaje": "Libro encontrado exitosamente ✅",
                "Book" : buscar[0]}
    except:
        return {"Error" : "Lo sentimos, No hemos encontrado un libro con este ID ❌"}
    
    
# Manejo del Post

@router.post("/book_post/", status_code = 201)

async def root_post (book : library): 
    
    for corregir in database_library: 
        if corregir.id == book.id:
            return {"Error ❌" : "Ya existe un usuario con este ID"}
        
        if corregir.titulo == book.titulo:
            return {"Error ❌" : "Ya existe un usuario con este titulo"}

    database_library.append(book)
    return {"Mensaje": "Book agregado exitosamente ✅",
            "New Book": book} 


# Manejo del Put

@router.put("/book_put/")

async def root_put (book : library):

    for index, actualizar in enumerate(database_library):
        if actualizar.id == book.id:
            database_library[index] = book
            return {"Mensaje": "Book Actualizado exitosamente ✅", "New Book update": book} 

    return {"Error ❌" : "Libro no encontrado para ser actualizado"}



# Manejo del Delete

@router.delete("/book_delete/{id}")

async def root_delete (id : int): 


    for eliminar in database_library:
        if eliminar.id == id:
            database_library.remove(eliminar)
            return {"Mensaje": "Book Eliminado exitosamente ✅",
                    "Book Delete": eliminar} 

    return {"Error ❌" : "Libro no encontrado para ser Eliminado"} 


