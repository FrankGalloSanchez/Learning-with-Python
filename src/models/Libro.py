from pydantic import BaseModel, Field

class Libro(BaseModel):
    titulo: str
    autor:str
    paginas:int
    editorial:str = Field(min_length=5,max_length=200)