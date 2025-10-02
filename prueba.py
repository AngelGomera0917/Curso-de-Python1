# Este es un proyecto de autenticacion de usuario.

from fastapi import FastAPI, Depends, HTTPException, status

from pydantic import BaseModel

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

OAuth2 = OAuth2PasswordBearer(tokenUrl = "login")

# Aqui creamos el modelo de datos del usuario

class User(BaseModel):
    username: str        # Nombre de usuario
    full_name: str       # Nombre completo
    age: int             # Edad
    disabled: bool 

class UserDB(User):
    password: str        # Hereda de User, pero además agrega el campo password

# Esto es la simulacion de la base de datos del usuario.

database_users = {
    "darlin8777": {
        "username": "darlin8777",
        "full_name": "Darlin Hernandez",
        "age": 19,
        "disabled": False,
        "password": "123456"
    },
    "angel0917": {
        "username": "angel0917",
        "full_name": "Angel Antonio Peralta",
        "age": 27,
        "disabled": True,
        "password": "654321"
    }
}

# Funcion que me permite buscar el usuario que le pasamos y verificarlo en la base de datos.
def search_user(Username: str): 
    
    if Username in database_users:
        return UserDB(database_users[Username])


# Funcion que me permite autenticar el usuario.

@app.post("/login", status_code = 201)
async def login(form : OAuth2PasswordRequestForm = Depends()):
    
    user_db = database_users.get(form.username)
    
    if not user_db:
        # Si el usuario no existe -> 404 Not Found
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, 
            detail = "El usuario no es correcto ❌"
        )
        
    user = search_user(form.username)
    
    if not user.password == form.password:
        # Si la contraseña es incorrecta -> 400 Bad Request
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, 
            detail = "La contraseña no es correcta ❌"
        )
        
    return {
        "access_Token": user.username,   # Aquí el "token" es simplemente el username.
        "Token_Type": "Bearer"           # Tipo de token usado en OAuth2
    }

# Funcion que me permite obtener el usuario actual.

@app.get("/users/me")
async def me (user : User = Depends()):
    return user