# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# importamos el framework
from fastapi import FastAPI, Body, Query

# Generamos una variable instanciando el framework
app = FastAPI()

# Models


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


# Iniciamos el decorador en el path home
# Path operation decorator
@app.get("/")
# Path operation function
def home():
    # Y retornamos el valor que deseamos
    return {"Hello": "Gaby"}

# Request and Response Body

# Decorador con función post y su path


@app.post("/person/new")
# Para retornar los datos hacemos que el parametro
# sea de tipo la clase que generamos anteriormente
def create_person(person: Person = Body(...)):
    return person

# Validaciones: Query paramethers


# Lo que el usuario ingresa es un Query paramether
# Debido a que estos son opcionales se utilizará la libreria
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: Optional[str] = Query(...)
):
    return {name: age}
