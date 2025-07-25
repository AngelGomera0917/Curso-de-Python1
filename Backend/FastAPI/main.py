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

# Creando una instancia de la aplicación FastAPI
app = FastAPI()

# Decorador que define la ruta raíz de la API
@app.get("/")

# async es una palabra clave en Python que se utiliza para definir funciones asíncronas. Las funciones asíncronas permiten realizar operaciones de entrada/salida (I/O) sin bloquear el hilo principal, lo que mejora la eficiencia y la capacidad de respuesta de la aplicación.
async def root(): # Función que maneja la ruta raíz de la aplicación.
    
    # Retorna un mensaje de bienvenida.
    return {"message": "Bienvenido a mi API con FastAPI"}

# url local: http://127.0.0.1:8000

@app.get("/url")
async def root(): # Función que maneja la ruta raíz de la aplicación.
    
    # Retorna un mensaje de bienvenida.
    return {"url_curso": "https://github.com/AngelGomera0917/Curso-de-Python1"}

# url local: http://127.0.0.1:8000/url

# inicicia el server: uvicorn main:app --reload
# Detener el server: CTRL + C

# Documentacion con Swagger: http://127.0.0.1:8000/docs
# Documentacion con Redocly: http://127.0.0.1:8000/redoc

# print(root())