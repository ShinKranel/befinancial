from datetime import datetime
from pydantic import BaseModel, EmailStr

from src.operations.models import OperationType


class ReadUsers(BaseModel):
    name: str
    email: EmailStr


class ReadUser(BaseModel):
    name: str
    email: EmailStr


class AddUser(BaseModel):
    name: str
    passhash: str
    email: EmailStr
