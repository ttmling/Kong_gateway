from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {
        "message": "Hello human!"
    }

@app.get("/users")
def users():
    return [
        {"id": 1, "name": "Linh"},
        {"id": 2, "name": "Tinh"}
    ]