
# En este vamos a trabajar con jwt, para mantener nuestro password encriptado y tambien nuestro token

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

from jose import jwt, JWTError # Librería para crear y verificar JSON Web Tokens (JWT).


from jose.exceptions import ExpiredSignatureError # Excepción específica para tokens expirados.

from passlib.context import CryptContext # Librería para hashing de contraseñas.

# utc para manejar las fechas en formato universal
from datetime import datetime, timedelta, UTC # Manejo de fechas y tiempos (para expiración de tokens).


# -------------------- Algoritmo de Firma para el TOKEN --------------------

ALGORITHM = "HS256" # Algoritmo de firma del token (HMAC con SHA-256).

# -------------------- CLAVE SECRETA PARA FIRMAR EL TOKEN --------------------

# Clave secreta usada para firmar y verificar el token (debe ser segura y secreta).
SECRET_KEY = "d8f3e5c6b7a9c0d1e2f3a4b5c6d7e8f9g0h1i2j3k4l5m6n7o8p9q0r1s2t3u4v5"

# -------------------- DURACION DEL TOKEN --------------------

ACCESS_TOKEN_DURATION = 1 # Duración del token en minutos (1 minuto)

# -------------------- CONFIGURACIÓN DEL hashing de contraseñas --------------------

crypt = CryptContext(schemes = ["bcrypt"], deprecated = "auto") # Configura PassLib para usar bcrypt como algoritmo de hashing.


# -------------------- CONFIGURACIÓN DEL ROUTER --------------------


router = APIRouter(prefix = "/jwt", tags = ["Autenticacion con JWT "])  
# APIRouter -> permite agrupar rutas bajo el prefijo "/OAuth".
# tags -> etiqueta usada en la documentación automática de FastAPI.


# -------------------- CONFIGURACIÓN DE OAUTH2 --------------------

OAuth2 = OAuth2PasswordBearer(tokenUrl = "login")  
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
        "password": "$2a$12$1fXYHkEGBeIGIRYWtglXo.p/4ChwYdMOl2rXbNJNFBYBx0D4u7d5W",
        "disabled": False
        
        # Mi password es "*****" (hashed con bcrypt)
    },
    "angel0917": {
        "username": "angel0917",
        "full_name": "Angel Antonio Peralta",
        "age": 27,
        "password": "$2a$12$SuQXFMjzj0zbPQDsltZdmeJQC1wJXpSssM3NjySyGO4TFfba1x4Ua",  
        "disabled": True
    }
    
    # Mi password es "*****" (hashed con bcrypt)
    
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
    # Devuelve un objeto User (sin contraseña) si existe en la base de datos.
    if Username in database_users:
        return UserDB(**database_users[Username])  
        # ** -> operador "unpacking", convierte el diccionario en parámetros nombrados.
        # Ejemplo: {"username":"x"} -> User(username="x")

# -------------------- DEPENDENCIA PARA VALIDAR TOKEN --------------------

async def oauth_user(token : str = Depends(OAuth2)):
    # token -> será automáticamente extraído del header Authorization.
    # Depends(OAuth2) -> inyecta la función OAuth2PasswordBearer para validar el token.
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM]) # Decodifica y verifica el token JWT.
        
        username = payload.get("sub") # Extrae el campo "sub" del payload (username).
        
        if username is None: # Si no existe el campo "sub", se devuelve un error 401 (no autorizado).
            raise HTTPException(
            status.HTTP_401_UNAUTHORIZED, 
            detail = " El campo Sub esta vacio ❌ "
        )
    
    # except JWTError:
    except ExpiredSignatureError: # Captura el error específico de token expirado.
        # I el token ya expiro, se devuelve un error 401 (no autorizado)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = " El Token ha expirado ❌ "
    )

    except JWTError: # Captura cualquier otro error relacionado con JWT.
        # Si no se encuentra, se devuelve un error 400 (Bad Resquest).
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = " Las credenciales del token son inválidas ❌ "
        )
    
    return search_user(username) # Devuelve el usuario encontrado o None si no existe.


async def current_user(user : User = Depends(oauth_user)): # 
    # user -> se obtiene automáticamente gracias a Depends(oauth_user)

    if user.disabled:
        # Si el usuario está marcado como deshabilitado, se devuelve un error 400.
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, 
            detail = " El usuario está deshabilitado ❌ "
        )
    
    return user  # Devuelve el usuario autenticado.

# -------------------- ENDPOINT DE LOGIN --------------------

@router.post("/login", status_code=status.HTTP_201_CREATED)
async def login(form : OAuth2PasswordRequestForm = Depends() ):
    # form -> representa los datos enviados en un formulario con campos:
    # form.username y form.password
    
    user_db = database_users.get(form.username) # Busca el usuario en la "base de datos"
    
    if not user_db: 
        # Si el usuario no existe -> 404 Not Found
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, 
            detail = " El usuario no es correcto ❌ "
        )
    
    user = search_user_db(form.username) # Obtiene el usuario como objeto UserDB
    
    if not crypt.verify(form.password, user.password): # Esto verifica la contraseña hasheada
        # Si la contraseña no coincide -> error 404
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, 
            detail = "La contraseña es incorrecta ❌"
        )
    
    access_token_expiration = timedelta(minutes = ACCESS_TOKEN_DURATION) # Duración del token
    
    # UTC -> Tiempo Universal Coordinado (zona horaria estándar)
    expire = datetime.now(UTC) + access_token_expiration # Tiempo de expiración del token

    payload = {
        "sub" : user.username,
        "exp" : expire
    } # Payload del token (datos que contiene) 
    
    # Si pasa las validaciones -> se devuelve un "access token".
    return {
        "Access_Token" : jwt.encode(payload, SECRET_KEY,  algorithm = ALGORITHM), # Genera el token JWT  
        "Token_type" : "bearer"             # Tipo de token usado en OAuth2
    }

# -------------------- ENDPOINT DE USUARIO AUTENTICADO --------------------

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    # user -> se obtiene automáticamente gracias a Depends(current_user)
    # Es decir, antes de entrar aquí, FastAPI validará el token.
    
    return user  # Devuelve los datos del usuario autenticado.
