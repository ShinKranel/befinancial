from pydantic import EmailStr
from datetime import datetime

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from src.budjet.models import Budget


# Enums --------------------------------


# Tables -------------------------------
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True)
    name: Mapped[str] = mapped_column(unique=True)
    passhash: Mapped[str]
    email: Mapped[EmailStr] = mapped_column(unique=True)
    budgets: Mapped[list[Budget]] = [None]
    registered_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

