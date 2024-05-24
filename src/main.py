import uvicorn
from fastapi import FastAPI

from src.operations.router import router as operations_router

app = FastAPI()


@app.get("/unprotected-route")
def protected_route():
    return f"Hello, anonym!"


app.include_router(operations_router, prefix="/operations", tags=["operations"])


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host='localhost',
        port=8000,
        reload=True
    )

