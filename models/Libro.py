from pydantic import BaseModel

class Libro(BaseModel):
    titulo: str
    autor:str
    paginas:int
    editorial:str   