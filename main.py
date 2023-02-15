from fastapi import FastAPI
from models.models import Data
app = FastAPI()


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.get("/hello/{data}")
def hello_world_with_args(data: Data):
    return {"data": data}
