# implementacion de libreria pydantic
from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel

class usuario(BaseModel):
    nombre: str
    apellido: str
    edad: int
    correo: str
    direccion: str
    ciudad: str
    departamento: str
    pais: str
    telefono: int
  
datos = {"nombre": "Claudia", "apellido": "Cardenas", "edad": 25, "correo": "v6sZu@example.com", "direccion": "Calle 123", "ciudad": "Medellin", "departamento": "Antioquia", "pais": "Colombia", "telefono": 123456789}
# crear instancia de la clase

usuario = usuario(**datos) 

@app.post("/crear usuario")
async def crear_usuario(usuario: usuario):
    return {"mensaje": f"usuario {usuario.nombre} creado con exito"}