# Curso de FastAPI: Fundamentos

### ¿Qué es FastAPI?
Es un framework de desarrollo backend para Python, especialmente APIs (Application Programming Interface) el cual te permite conectarte entre las distintas partes de la aplicación, es más rápido respecto a velocidad que otros, superando incluso a alternativas clásicas como GO o Node.js.
Creado por [Sebastian Ramirez](https://twitter.com/tiangolo), es de código abierto, se encuentra en Github y es utilizado por empresas como Windows, Uber, Netflix y Office

### Ubicación de FastAPI en el ecosistema de Python
- Uvicorn 🦄: Una librería que funciona como servidor, permite que cualquier computadora se convierta en servidor.
- Starlette ⭐: Un framework de desarrollo web de bajo nivel, FastAPI le añade funciones para facilitar su uso.
- Pydantic ❔: Framework que permite trabajar con datos, tal como Pandas, se caracteriza por poder crear modelos

### Creación del entorno
Creamos nuestro entorno de desarrollo de forma convencional
> Git bash
> `git init`
> `python -m venv venv`
> `venv/sripts/activate`
> `pip install fastapi uvicorn`

### Hello World!
Crearemos nuestro primer Hello World! a través de FastAPI.
Lo primero que debemos hacer es crear nuestro archivo a utilizar, en este caso `main.py`
Dentro del mismo, habiéndolo abierto con VSCode y verificando que el virtual environment está actualmente activo comenzamos:

```
# importamos el framework
from fastapi import FastAPI

# Generamos una variable instanciando el framework
app = FastAPI()

# Iniciamos el decorador en el path home
@app.get("/")
def home():
    # Y retornamos el valor que deseamos
    return {"Hello": "World"}
```
Y luego iniciamos el proyecto en nuestra consola a través del código
> `uvicorn main:app --reload`

|uvicorn| main|:app| --reload|
|--|--|--|--|
|Librería que permite el deploy web|Nombre del archivo|Nombre de la instancia|Permite la recarga ante cambios|

El resultado http://127.0.0.1:8000/ en entonces será:
> `{"Hello": "World"}`

### Documentación interactiva de una API
FastAPI funciona con múltiples librerías previas, entre ellas OpenAPI, esta se trata de un conjunto de reglas que permite definir cómo describir, crear y visualizar APIs, esta es entonces un conjunto de reglas para definir la API correctamente, una especificación.
OpenAPI necesita de software para funcionar, como Swagger, este es un conjunto de programas que permiten trabajar con APIs, una de sus partes, SwaggerUI funciona en conjunto a OpenAPI para poder generar de forma interactiva la documentación de la API

Acceder a la documentación interactiva con Swagger UI:  
> `{localhost}/docs`  

Acceder a la documentación interactiva con Redoc:  
> `{localhost}/redoc`

### Path operations
*¿Que es un path?*
Lo mismo que un route o endpoint, la dirección en la que apunta el link luego de nuestro dominio separado por slashes "/" o en el caso de un proyecto local utiliza IPs y puertos

|myproject.com|index|
|---|---|
|127.0.0.1|:8000|

*¿Qué son las operations?*
Al igual que los métodos HTTP, las operations nos permiten tener métodos, tales como GET, POST, PUT, DELETE
|Métodos populares|Traducción|
|---|---|
|GET|Obtener|
|POST|Envío|
|PUT|Actualizar|
| DELETE|Borrar|

Ya habíamos utilizado una path operation en el proyecto antes, get
> `@app.get("/")`

### Path Parameters
Un Path paramater es una variable definida dentro de un endpoint se utilizan para evitar codear la grabación de nuevas entradas con métodos menos eficientes, cada vez que defino un path paramether es obligatorio pasarlo luego para acceder, el no hacerlo dará error.
Una dirección puede contener múltiples path parameters

|/tweets/|{tweet_id}|
|---|---|

### Query Parameters
Un Query Patameter es un conjunto de elementos opcionales los cuales son añadidos al finalizar la ruta, con el objetivo de definir contenido o acciones en la url, estos elementos se añaden después de un ? para agregar más query parameters utilizamos &

Ejemplo de link:
> `../user/{tweet_id}/?age=18&?height=184`

../|users/|{tweet_id}/|?|age=18|&|height=184|
|--|--|--|--|--|--|--|
|path a completar|--|path operation (variable)|iniciar un parámetro|query parameter|símbolo agregar|query parameter|

### Request Body y Response Body
Recordando a HTTP/ReST estas se componen por un HEAD y un BODY, este último mediante JSON.

Por otra parte, se considera un Request cuando un cliente *pide/solicita* a un servidor y un Response cuando este *responde* a la llamada.
Por lo tanto Request Body y Response Body son las llamadas de body, tanto de ida como de vuelta respecto al servidor respectivamente.

Dentro de nuestro código si queremos hacer una Request o envío de datos lo hacemos mediante el método `post` a partir de un path decorator.
> `@app.post("/person/new")`

### Models
En el mundo real una entidad puede ser cualquier objeto, como una persona, una mascota, un mouse. Un modelo es una representación de una entidad en código, al menos de una forma descriptiva.
Crearemos los modelos a través de la librería `Pydantic > BaseModel`
Los mismos se harán en tipado estático para delimitar la respuesta, y el método que se utilizará es post

> Clase generada para creación del modelo o tipo
![enter image description here](https://i.imgur.com/JLXoaQc.png)
Método que obtiene sus datos a partír de dicha clase
![enter image description here](https://i.imgur.com/l5XXvlJ.png)

### Validaciones: Query Parameters
Para que lo que nos llegue de la API sean datos que realmente queremos, nuestros parámetros tienen que estar validados, esto mediante restricciones o indicaciones de formato, por ejemplo:

> `50 > name => 1` == name no puede ser mayor a 50 ni menor a 1

*Recordar que los datos a ingresar son Query Parameters, por lo tanto opcionales, si necesitamos que sea obligatorio debería ser un Path paramether*

> Método que obtiene los datos restringidos a partir de Query paramethers, (Opcional y obligatorio respectivamente)
![enter image description here](https://i.imgur.com/BlFG71g.png)

Existen múltiples parámetros para validar nuestros elementos string

|Funciones|Acción|
|---|---|
|max_length|Máximo largo de un string|
|min_lenght|Mínimo largo de un string|
|regex|Método que permite validar a través de patrones|

Y también con los enteros 

|Funciones|Acción|
|---|---|
|ge|greater or equal than >= (Mayor igual que)|
|le|less or equal than <= (Menor igual que)|
|gt|greater than > (Mayor que)|
|lt|less than < (Menor que)|

También es posible dar mayor contexto a nuestra documentación. Se deben usar los parámetros  **title**  y  **description**.

-   **title**  _: Para definir un título al parámetro._
-   **description**  _: Para especificar una descripción al parámetro._

### Validaciones: Path Parameters
### Validaciones: Request Body
Es la primera vez utilizando el método Put (actualizar), en este caso dentro del path paramether `person_id` 
> `@app.put("/person/detail/{person_id}")`

![enter image description here](https://i.imgur.com/rWBQud6.png)

Si generáramos más modelos y quisiéramos hacer una request body múltiple podemos hacerlo al añadir éste nuevo diccionario al previo y por lo tanto generar un diccionario de diccionarios el cual FastAPI retornará un único diccionario con todos los datos

```
results = person.dict()
results.update(location.dict())
```

