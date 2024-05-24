from pydantic import BaseModel

from src.operations.models import OperationType


class AddOperation(BaseModel):
    amount: int
    type: OperationType
