# importamos el framework
from fastapi import FastAPI

# Generamos una variable instanciando el framework
app = FastAPI()

# Iniciamos el decorador en el path home
# Path operation decorator
@app.get("/")
# Path operation function
def home():
    # Y retornamos el valor que deseamos
    return {"Hello": "Gaby"}