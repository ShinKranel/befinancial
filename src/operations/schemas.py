from pydantic import BaseModel

from src.operations.models import OperationType


class ReadOperation(BaseModel):
    value: int
    type: OperationType


class ReadOperations(BaseModel):
    data: list[ReadOperation]


class AddOperation(BaseModel):
    user_id: int
    budget_id: int
    amount: int
    type: OperationType
