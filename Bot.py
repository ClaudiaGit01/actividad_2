# implementacion de libreria pydantic
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

print(usuario)  
print(usuario.nombre)
print(usuario.apellido)
print(usuario.pais)


