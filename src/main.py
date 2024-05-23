import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/unprotected-route")
def protected_route():
    return f"Hello, anonym!"


@app.get("/users")
def read_users():
    return {"users": "users"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )

