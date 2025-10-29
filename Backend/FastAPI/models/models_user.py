
# Import FastAPI y pydantic para crear una aplicación web y manejar datos
# Importando BaseModel de pydantic para definir modelos de datos
from pydantic import BaseModel


# Entidad user_profile
# Definimos un modelo de datos para representar un usuario
class user_profile(BaseModel):
    Name: str
    Age: int
    # Surname: str
    # id_user: int