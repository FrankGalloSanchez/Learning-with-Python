from fastapi import FastAPI 
from src.routers.book_router import book_router

app = FastAPI()

@app.get("/", tags=["Home"])
def index():
    return {"Welcome":"API books"}

app.include_router(prefix='/book',router=book_router)