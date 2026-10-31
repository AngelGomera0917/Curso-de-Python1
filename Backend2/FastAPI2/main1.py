from fastapi import FastAPI

app1 = FastAPI()

@app1.get("/")
async def darli():
    return {"message" : "Darli - Bienvenida a mi API con FastAPI"}

@app1.get("/url")
async def ruta():
    return {"message" : "https://fastapi.tiangolo.com/es/tutorial"}
