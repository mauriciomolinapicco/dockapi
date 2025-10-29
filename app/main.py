from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(title="fastapi-microservices-lab")

class Payload(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Hola desde FastAPI"}

