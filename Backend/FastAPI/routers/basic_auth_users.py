
"""
                            ===========================================================
                            * AUTENTICACIÓN EN FASTAPI USANDO OAuth2 (Ejemplo Básico) *
                            ===========================================================

Este ejemplo muestra cómo implementar autenticación en FastAPI 
utilizando el flujo OAuth2 con contraseña (password flow) y portador 
(bearer token). 

Incluye:
    - Uso de `OAuth2PasswordBearer` y `OAuth2PasswordRequestForm`.
    - Generación y validación de tokens de acceso (JWT).
    - Manejo de usuarios y contraseñas simulados.
    - Protección de endpoints mediante dependencias de seguridad.

Cada línea está comentada en detalle para comprender el propósito 
de las importaciones, parámetros y funciones.

"""

# -------------------- IMPORTACIONES --------------------

from fastapi import APIRouter, Depends, HTTPException, status  
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

router = APIRouter(prefix="/OAuth", tags=["Autenticacion"])  
# APIRouter -> permite agrupar rutas bajo el prefijo "/OAuth".
# tags -> etiqueta usada en la documentación automática de FastAPI.


# -------------------- CONFIGURACIÓN DE OAUTH2 --------------------

OAuth2 = OAuth2PasswordBearer(tokenUrl="login")  
# OAuth2PasswordBearer -> espera un token enviado en el header Authorization: Bearer <token>.
# tokenUrl="login" -> indica cuál es el endpoint que entrega el token (en este caso "/OAuth/login").


# -------------------- MODELOS DE USUARIO --------------------

class User(BaseModel):
    username: str        # Nombre de usuario
    full_name: str       # Nombre completo
    age: int             # Edad
    disabled: bool       # Estado del usuario (True si está deshabilitado)

class UserDB(User):
    password: str        # Hereda de User, pero además agrega el campo password


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


# -------------------- FUNCIONES DE BÚSQUEDA DE USUARIO --------------------

def search_user(Username: str):
    # Devuelve un objeto User (sin contraseña) si existe en la base de datos.
    if Username in database_users:
        return User(**database_users[Username])  
        # ** -> operador "unpacking", convierte el diccionario en parámetros nombrados.
        # Ejemplo: {"username":"x"} -> User(username="x")

def search_user_db(Username: str):
    # Devuelve un objeto UserDB (con contraseña incluida) si existe en la base de datos.
    if Username in database_users:
        return UserDB(**database_users[Username])


# -------------------- DEPENDENCIA PARA VALIDAR TOKEN --------------------

async def current_user(token: str = Depends(OAuth2)):
    # token -> será automáticamente extraído del header Authorization.
    # Depends(OAuth2) -> inyecta la función OAuth2PasswordBearer para validar el token.
    
    user_token = search_user(token)  # Se busca el usuario con el "token" recibido.
    
    if not user_token:
        # Si no se encuentra, se devuelve un error 401 (no autorizado).
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED, 
            detail="Token no válido ❌"
        )
    
    if user_token.disabled:
        # Si el usuario está marcado como deshabilitado, se devuelve un error 400.
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, 
            detail="El usuario está deshabilitado ❌"
        )
    
    return user_token  # Devuelve el usuario autenticado.


# -------------------- ENDPOINT DE LOGIN --------------------

@router.post("/login", status_code = 201)
async def login(form: OAuth2PasswordRequestForm = Depends()):
    # form -> representa los datos enviados en un formulario con campos:
    # form.username y form.password
    
    user_db = database_users.get(form.username)  # Busca el usuario en la "base de datos"
    
    if not user_db:
        # Si el usuario no existe -> 404 Not Found
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, 
            detail="El usuario no es correcto ❌"
        )
    
    user = search_user_db(form.username)  # Se obtiene el usuario con su contraseña
    
    if not form.password == user.password:
        # Si la contraseña no coincide -> error 404
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, 
            detail="La contraseña es incorrecta ❌"
        )
    
    # Si pasa las validaciones -> se devuelve un "access token".
    return {
        "access_Token": user.username,   # Aquí el "token" es simplemente el username.
        "Token_Type": "Bearer"           # Tipo de token usado en OAuth2
    }


# -------------------- ENDPOINT DE USUARIO AUTENTICADO --------------------

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    # user -> se obtiene automáticamente gracias a Depends(current_user)
    # Es decir, antes de entrar aquí, FastAPI validará el token.
    
    return user  # Devuelve los datos del usuario autenticado.



