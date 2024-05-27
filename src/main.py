import uvicorn
from fastapi import FastAPI, Request

from src.operations.router import router as operations_router
from src.budget.router import router as budget_router
from src.user.router import router as user_router

app = FastAPI()


@app.get("/")
def protected_route():
    return f"Hello, anonym!"


app.include_router(operations_router, prefix="/operations", tags=["operations"])
app.include_router(budget_router, prefix="/budget", tags=["budget"])
app.include_router(user_router, prefix="/user", tags=["user"])


@app.get("/app")
def read_main(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='localhost',
        port=8000,
        reload=True
    )

