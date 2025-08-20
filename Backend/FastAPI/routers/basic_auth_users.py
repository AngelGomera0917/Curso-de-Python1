

from fastapi import APIRouter, Depends, HTTPException

from pydantic import BaseModel

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix = "/OAuth", tags = ["Autenticacion"])

OAuth2 = OAuth2PasswordBearer(tokenUrl = "login")

class User(BaseModel):
    username: str
    full_name: str 
    age: int 
    disabled: bool

class UserDB(User):
    password: str

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

def search_user(Username: str):
    if Username in database_users:
        return User(**database_users[Username])
    
def search_user_db(Username: str):
    if Username in database_users:
        return UserDB(**database_users[Username])


async def current_user(token: str = Depends(OAuth2)):
    user_token = search_user(token)
    
    if not user_token:
        raise HTTPException(status_code = 401, detail = "Token no válido ❌")
    
    if user_token.disabled:
        raise HTTPException(status_code = 400, detail = "El usuario está deshabilitado ❌")
    
    return user_token

@router.post("/login")
async def login(form : OAuth2PasswordRequestForm = Depends()):
    user_db = database_users.get(form.username)
    
    if not user_db:
        raise HTTPException(status_code = 400, detail = "El usuario no es correcto ❌")
    
    user = search_user_db(form.username)
    
    if not form.password == user.password:
        raise HTTPException(status_code = 404, detail = "La contraseña es incorrecta ❌")
    
    return {"access_Token": user.username ,"Token_Type": "Bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    
    return user





