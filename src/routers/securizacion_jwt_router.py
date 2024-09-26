from fastapi import APIRouter,Depends
from src.data.User import users
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi.exceptions import HTTPException
from jose import jwt

booksecurity = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def encode_token(payload:dict) -> str:
    token = jwt.encode(payload, "my-secret", algorithm="HS256")
    return token

def decode_token(token:Annotated[str , Depends(oauth2_scheme)]) -> dict:
    data = jwt.decode(token, "my-secret" , algorithms = ["HS256"])
    user = users.get(data["username"])
    return user

@booksecurity.post("/token", tags=["Oauth"])
def login(form_data : Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users.get(form_data.username)
    if not user or form_data.password != user["password"]:
        raise HTTPException(status_code=400 , detail= "Incorrect username or password")
    token = encode_token({"username" : user["username"], "email" : user["email"]})
    return { "access_token" : token}

@booksecurity.get("/profile" , tags=["Oauth"])
def profile(my_user : Annotated[dict , Depends(decode_token)]):
    return my_user