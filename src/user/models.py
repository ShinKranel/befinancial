from datetime import datetime

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from src.db import Base
from src.budget.models import Budget

# Enums --------------------------------


# Tables -------------------------------

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    passhash: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    registered_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

    budgets: Mapped[list["Budget"]] = relationship(back_populates="user")
    operations: Mapped[list["Operation"]] = relationship(back_populates="user")
