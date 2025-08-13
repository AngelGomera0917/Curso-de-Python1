# Pimero instalar FastAPI e Uvicorn
# pip install "fastapi[ALL]"

# FastAPI es un framework web moderno y rápido para construir APIs con Python 3.6+ basado en tipos de datos estándar de Python.
# FastAPI permite crear APIs RESTful de manera rápida y eficiente, aprovechando las características de Python como la tipificación estática y la validación automática de datos.
# Para ejecutar el servidor, puedes usar el siguiente comando en la terminal:
# uvicorn main:app --reload

# Uvicorn es un servidor ASGI que se utiliza para ejecutar aplicaciones web basadas en FastAPI.
# pip install uvicorn

# Importando FastAPI para crear una aplicación web
from fastapi import FastAPI
from routers import libreria, users, status_http

# Vamos a importar staticfiles para servir archivos estáticos como imágenes, CSS y JavaScript.
from fastapi.staticfiles import StaticFiles

# Creando una instancia de la aplicación FastAPI
app = FastAPI()

# Incluyendo el router de la librería
app.include_router(libreria.router) # Incluyendo el router de usuarios
app.include_router(users.router) # Incluyendo el router de status_http
app.include_router(status_http.router) # incluyendo el router de status_http

app.mount("/static", StaticFiles(directory="static"), name="static") # Montando la carpeta 'static' para servir archivos estáticos

# name="static" : Le da un nombre a la ruta montada, útil para url_for()

# StaticFiles(directory="static")
# Aquí se le está diciendo a FastAPI que los archivos que se van a servir están en una carpeta local llamada static.

# "/static"
# Es la ruta pública en la URL. 

# para incresar a la ruta de los archivos estáticos, puedes usar la URL: http://127.0.0.1:8000/static/images/Python.jpg

# Decorador que define la ruta raíz de la API
@app.get("/url")

# async es una palabra clave en Python que se utiliza para definir funciones asíncronas. Las funciones asíncronas permiten realizar operaciones de entrada/salida (I/O) sin bloquear el hilo principal, lo que mejora la eficiencia y la capacidad de respuesta de la aplicación.
async def root(): # Función que maneja la ruta raíz de la aplicación.
    
    # Retorna un mensaje de bienvenida.
    return {"message": "Bienvenido a mi API con FastAPI"}

# url local: http://127.0.0.1:8000


# inicicia el server: uvicorn main:app --reload
# Detener el server: CTRL + C

# Documentacion con Swagger: http://127.0.0.1:8000/docs
# Documentacion con Redocly: http://127.0.0.1:8000/redoc

# print(root())