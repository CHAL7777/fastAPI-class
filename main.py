from fastapi import FastAPI
import os
app = FastAPI()

students = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Sara"}
]

@app.get("/students")
def get_students():
    return students