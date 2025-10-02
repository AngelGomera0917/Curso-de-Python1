


# -------------------- IMPORTACIONES --------------------

from fastapi import FastAPI, Depends, HTTPException, status  
# APIRouter -> permite crear rutas organizadas como un "módulo" dentro de la app.
# Depends -> se usa para inyectar dependencias (por ejemplo, funciones de autenticación).
# HTTPException -> sirve para devolver errores HTTP controlados.
# status -> contiene constantes para códigos de estado HTTP (401, 404, etc.).

from pydantic import BaseModel  
# BaseModel -> clase de Pydantic para definir modelos de datos (valida tipos automáticamente).

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm  
# OAuth2PasswordBearer -> define el esquema de seguridad que espera un "token" en la cabecera Authorization.
# OAuth2PasswordRequestForm -> recibe datos de login en formato formulario (username + password).


# -------------------- CONFIGURACIÓN DEL ROUTER --------------------


app = FastAPI()  
# APIRouter -> permite agrupar rutas bajo el prefijo "/OAuth".
# tags -> etiqueta usada en la documentación automática de FastAPI.


# -------------------- CONFIGURACIÓN DE OAUTH2 --------------------

OAuth2 = OAuth2PasswordBearer(tokenUrl="login")  
# OAuth2PasswordBearer -> espera un token enviado en el header Authorization: Bearer <token>.
# tokenUrl="login" -> indica cuál es el endpoint que entrega el token (en este caso "/OAuth/login").


# -------------------- MODELOS DE USUARIO --------------------

class User(BaseModel):
    username: str        
    full_name: str       
    age: int             
    disabled: bool       

class UserDB(User):
    password: str        


# -------------------- Simulacion de BASE DE DATOS --------------------

database_users = {
    "darlin8777": {
        "username": "darlin8777",
        "full_name": "Darlin Hernandez",
        "age": 19,
        "password": "123456",
        "disabled": False
    },
    "angel0917": {
        "username": "angel0917",
        "full_name": "Angel Antonio Peralta",
        "age": 27,
        "password": "654321",
        "disabled": True
    }
}
# Se simula una "base de datos" con dos usuarios:
# - darlin8777 (activo)
# - angel0917 (deshabilitado)
