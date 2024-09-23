from fastapi import FastAPI 
from pydantic import BaseModel
app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor:str
    paginas:int
    editorial:str

@app.get("/")
def index():
    return {"message":"Hola, Xd"}

@app.get("/book/{id}")
def mostrar_libros(id:int):
    return {"data":id}

@app.post("/books")
def insertar_libro(libro:Libro):
    return{"message":f"libro, {libro.titulo} insertado"}