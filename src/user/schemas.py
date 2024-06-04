from datetime import datetime

from pydantic import BaseModel, EmailStr


# initialises --------------------------
class AddUser(BaseModel):
    name: str
    passhash: str
    email: EmailStr


# responses -----------------------------
class ReadUser(BaseModel):
    name: str
    email: EmailStr
    registered_at: datetime
