from src.models.Libro import Libro
from src.data.data import libros_db
from fastapi import APIRouter

book_router = APIRouter()

@book_router.get("/", tags=["Book"])
def get_all():
    return {"books" :libros_db}

@book_router.get("/title" , tags=["Book"])
def get_titulo(Titulo : str):
    for book in libros_db:
        if book['titulo'] == Titulo:
            return book
    return []

@book_router.get("/{id}" ,tags=["Book"])
def get_libro_by_id(id:int):
    for book in libros_db:
        if book['id'] == id:
            return book
    return []

@book_router.post("/" , tags=["Book"])
def save_book(libro:Libro):
    return{"message":f"libro, {libro.titulo} insertado"}

@book_router.put("/{id}", tags=["Book"])
def edit_by_id(id: int, libro: Libro):
    for book in libros_db:
        if book['id'] == id:
            book.update(libro.dict())
            return {"message": f"Libro con ID {id} actualizado", "book": book}
    return {"message": "Libro no encontrado"}

@book_router.delete("/{id}", tags=["Book"])
def delete_book(id: int):
    for index, book in enumerate(libros_db):
        if book['id'] == id:
            del libros_db[index]
            return {"message": f"Libro con ID {id} eliminado", "books": libros_db}
    return {"message": "Libro no encontrado", "books": libros_db}