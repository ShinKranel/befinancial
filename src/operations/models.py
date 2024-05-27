import enum
from datetime import datetime

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from src.db import Base


# Enums --------------------------------
class OperationType(enum.Enum):
    income = "income"
    outcome = "outcome"


# Tables -------------------------------
# class Base(DeclarativeBase):
#     pass


class Operation(Base):
    __tablename__ = "operation"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"))
    amount: Mapped[int]
    type: Mapped[OperationType]
    registered_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

    user: Mapped["User"] = relationship(back_populates="operations")
    budget: Mapped["Budget"] = relationship(back_populates="operations")
