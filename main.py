from fastapi import FastAPI 
from models.Libro import Libro
from data.data import libros_db

app = FastAPI()

@app.get("/", tags=["Home"])
def index():
    return {"Welcome":"API books"}

@app.get("/books", tags=["Book"])
def get_all():
    return {"books" :libros_db}

@app.get("/books/" , tags=["Book"])
def get_titulo(Titulo : str):
    for book in libros_db:
        if book['titulo'] == Titulo:
            return book
    return []

@app.get("/book/{id}" ,tags=["Book"])
def get_libro_by_id(id:int):
    for book in libros_db:
        if book['id'] == id:
            return book
    return []

@app.post("/books" , tags=["Book"])
def save_book(libro:Libro):
    return{"message":f"libro, {libro.titulo} insertado"}

@app.put("/book/{id}", tags=["Book"])
def edit_by_id(id: int, libro: Libro):
    for book in libros_db:
        if book['id'] == id:
            book.update(libro.dict())
            return {"message": f"Libro con ID {id} actualizado", "book": book}
    return {"message": "Libro no encontrado"}

@app.delete("/book/{id}", tags=["Book"])
def delete_book(id: int):
    for index, book in enumerate(libros_db):
        if book['id'] == id:
            del libros_db[index]
            return {"message": f"Libro con ID {id} eliminado", "books": libros_db}
    return {"message": "Libro no encontrado", "books": libros_db}