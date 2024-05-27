from pydantic import BaseModel


class ReadBudgets(BaseModel):
    user: str
    value: float


class ReadBudget(BaseModel):
    user: str
    value: float


class AddBudget(BaseModel):
    # user_id: int
    value: float
    user_id: int = 1
