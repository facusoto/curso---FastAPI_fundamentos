# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel, Field, EmailStr, IPvAnyAddress

# importamos el framework
from fastapi import FastAPI, Body, Query, Path

# Generamos una variable instanciando el framework
app = FastAPI()

# Models
# Modelo de especificación de colores de cabello
class HairColor(Enum):
    white = 'white'
    black = 'black'
    brown = 'brown'
    blonde = 'blonde'


class Location(BaseModel):
    city: str = Field(
        ...,
        max_length=150,
        min_length=1,
        example="Los Cardos"
    )
    state: str = Field(
        ...,
        max_length=150,
        min_length=1,
        example="Buenaventura"
    )
    country: str = Field(
        ...,
        max_length=150,
        min_length=1,
        example="Peluduestonia"
    )


class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Rodrigo"
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Martinez"
        )
    age: int = Field(
        ...,
        gt=0,
        le=115,
        example=23
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None, example=False)
    ip_address_str: IPvAnyAddress = Field(...)
    email: Optional[EmailStr] = Field(default=None)

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "first_name": "Facundo",
    #             "last_name": "Soto",
    #             "age": 25,
    #             "hair_color": "Brown",
    #             "is_married": False,
    #             "ip_address_str": "192.168.1.1",
    #             "email": "facusoto@hola.com"
    #         }
    #     }


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
def create_person(person: Person = Body(
    ...,
    title="Person creator",
    description="This is the person creator. It's made by Person object and required"
)):
    return person


# Validaciones: Query paramethers

# Lo que el usuario ingresa es un Query paramether
# Debido a que estos son opcionales se utilizará la libreria
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person name",
        description="This is the person name. It's beween 1 and 50 characters"
    ),
    age: Optional[str] = Query(
        ...,
        title="Person age",
        description="This is the person age. It's required"
    )
):
    return {name: age}


# Validaciones: Path paramethers

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person ID",
        description="This is the person ID. It's required"
    )
):
    return {person_id: "It exists!"}

#  Validaciones: Request Body

# Vamos a actualizar los datos de una person_id


@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return person
