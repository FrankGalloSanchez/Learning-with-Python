from fastapi import FastAPI 
from src.routers.book_router import book_router
from src.routers.securizacion_jwt_router import booksecurity

app = FastAPI()

@app.get("/", tags=["Home"])
def index():
    return {"Welcome":"API books"}

app.include_router(router=booksecurity)
app.include_router(prefix='/book',router=book_router)