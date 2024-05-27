from pydantic import BaseModel, EmailStr


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
